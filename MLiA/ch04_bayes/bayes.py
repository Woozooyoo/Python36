# coding=utf-8
"""
Created on Oct 19, 2010

@author: Peter
"""
from numpy import *
import feedparser


# 生成人造言论数据
def loadDataSet():
    postingList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1]  # 1 is abusive侮辱, 0 not
    return postingList, classVec


# 从整个样本空间中获取所有不重复的词，返回一个不重复所有词的列表
def createVocabList(dataSet):
    vocabSet = set([])  # create empty set
    for document in dataSet:
        vocabSet = vocabSet | set(document)  # union of the two sets
    return list(vocabSet)


# 将输入的句子变成一个词向量
def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0] * len(vocabList)  # 创建一个其中所含元素都为0的向量
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1  # index函数在字符串里找到字符第一次出现的位置
        else:
            print("the word: %s is not in my Vocabulary!" % word)
    return returnVec


# 输入trainMatrix是样本数据6,32向量化之后的结果，trainCategory是样本数据6的类别标签(0,1,0,0,1,0,1,1.....)
def trainNB0(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)  # 6
    numWords = len(trainMatrix[0])  # 32
    # 求Abusive 即1 类别的总概率
    pAbusive = sum(trainCategory) / float(numTrainDocs)
    p0Num = ones(numWords)
    p1Num = ones(numWords)  # change to ones()   #避免一个概率值为0,最后的乘积也为0
    p0Denom = 2.0  # 用于统计0类中的总数
    p1Denom = 2.0  # change to 2.0 用于统计1类中的总数
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = log(p1Num / p1Denom)  # change to log() 在类1中，每个次的发生概率
    p0Vect = log(p0Num / p0Denom)  # 避免下溢出或者浮点数舍入导致的错误   下溢出是由太多很小的数相乘得到的
    return p0Vect, p1Vect, pAbusive


def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)  # element-wise mult
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else:
        return 0


# 贝叶斯分类器 人造数据测试
def testingNB():
    listOPosts, listClasses = loadDataSet()
    myVocabList = createVocabList(listOPosts)
    print('myVocabList', myVocabList)
    trainMat = []
    for postinDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
    print('trainMat', trainMat)
    p0V, p1V, pAb = trainNB0(array(trainMat), array(listClasses))
    print(p0V, p1V, pAb)
    testEntry = ['love', 'my', 'dalmation']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print(testEntry, 'classified as: ', classifyNB(thisDoc, p0V, p1V, pAb))
    testEntry = ['stupid', 'garbage']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print(testEntry, 'classified as: ', classifyNB(thisDoc, p0V, p1V, pAb))


# 调用测试方法 ------------------------------------------------------------------------------------------------------
testingNB()


def bagOfWords2VecMN(vocabList, inputSet):
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
    return returnVec


# 邮件分类
def textParse(bigString):  # input is big string, #output is word list
    import re
    listOfTokens = re.split(r'\W+', bigString)  # 正则表达式进行文本解析
    return [tok.lower() for tok in listOfTokens if len(tok) > 2]  # 过滤长度小于3的


def spamTest():
    docList = []
    classList = []
    fullText = []
    for i in range(1, 26):  # 导入并解析文本文件
        wordList = textParse(open('email/spam/%d.txt' % i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)
        wordList = textParse(open('email/ham/%d.txt' % i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    vocabList = createVocabList(docList)  # create vocabulary
    trainingSet = list(range(50))  # 创建一个 0 50的索引Set
    testSet = []  # create test set
    for i in range(10):  # 随机构建训练集
        randIndex = int(random.uniform(0, len(trainingSet)))  # 得到0到50的随机数索引
        testSet.append(trainingSet[randIndex])  # 随机挑选一个文档索引号放入testSet
        del (trainingSet[randIndex])  # 从trainingSet删掉到testSet的 剩下要训练的索引
    trainMat = []
    trainClasses = []
    for docIndex in trainingSet:  # the classifier (get probs) trainNB0
        trainMat.append(bagOfWords2VecMN(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V, p1V, pSpam = trainNB0(array(trainMat), array(trainClasses))  # 得到训练出来的 probability
    errorCount = 0
    for docIndex in testSet:  # classify the remaining items
        wordVector = bagOfWords2VecMN(vocabList, docList[docIndex])
        if classifyNB(array(wordVector), p0V, p1V, pSpam) != classList[docIndex]:
            errorCount += 1
            print("classification error, real answer is:", classList[docIndex], docList[docIndex])
    print('the error rate is: ', float(errorCount) / len(testSet))
    # return vocabList,fullText


# 垃圾邮件分类数据测试  -------------------------------------------------------------------------------
spamTest()
