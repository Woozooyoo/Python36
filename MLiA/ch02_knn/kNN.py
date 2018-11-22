# coding=utf-8
"""
Created on Sep 16, 2010
kNN:k近邻

Input:      inX: 待分类向量 (1xN)
            dataSet: 先验数据集 (NxM)
            labels: 先验数据分类标签 (1xM vector)
            k: 参数：k个近邻 (should be an odd number)

Output:     分类标签
"""
from numpy import *
import operator
from os import listdir
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]  # 几行
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet  # 复制1000行的传入数据为矩阵 - 训练数据
    sqDiffMat = diffMat ** 2  # 距离公式  元素的平方
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5  # 开平方得真正距离
    sortedDistIndicies = distances.argsort()  # 按距离从小到大排序其索引 [4 2 3 1]
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]  # A? B?
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1  # classC[A]有则+1 没有则0+1
    # 按 [A:1, B:2] 每一个entry的value即 [1] 正序排序 再reverse
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]  # Map的第一个的第一个元素

def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

# # 简单分类器测试
# group, labels = createDataSet()
# res = classify0([3, 3], group, labels, 3)  # k取最近的3个
# print res

# 文件变矩阵
def file2matrix(filename):
    fr = open(filename)
    numberOfLines = len(fr.readlines())  # get the number of lines in the file
    returnMat = zeros((numberOfLines, 3))  # prepare matrix to return
    classLabelVector = []  # prepare labels return
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index, :] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat, classLabelVector


# 图形化展现
# datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
#
# # 二维图 丢失维度
# ax = plt.figure().add_subplot(111)
# # 第一个参数 横坐标集合 第二个参数纵坐标集合 第三个参数圆点大小 第四个参数
# ax.scatter(datingDataMat[:,0],datingDataMat[:,1],15.0*array(datingLabels),15.0*array(datingLabels))
# plt.show()

# 三维图 展示
# ax = plt.subplot(111, projection='3d')  # 创建一个三维的绘图工程
# #  将数据点分成三部分画，在颜色上有区分度
# ax.scatter(datingDataMat[:, 0], datingDataMat[:, 1], datingDataMat[:, 2], c=15.0 * array(datingLabels))  # 绘制数据点
# ax.set_zlabel('Z')  # 坐标轴
# ax.set_ylabel('Y')
# ax.set_xlabel('X')
# plt.show()

def autoNorm(dataSet):  # 归一化
    minVals = dataSet.min(0)  # 三列每一列的最小值   [0, 0, 10]
    maxVals = dataSet.max(0)  # 三列每一列的最大值   [1000,20,100]
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]  # dataSet是几行几列的第一个参数 即几行
    normDataSet = dataSet - tile(minVals, (m, 1))  # 复制 m行 [0, 0, 0] 再减
    normDataSet = normDataSet / tile(ranges, (m, 1))  # element wise divide
    return normDataSet, ranges, minVals

# 用50%数据来做测试，统计分类结果错误率  测试原来的label和学习得出的label差别
def datingClassTest():
    hoRatio = 0.50  # hold out 10%
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')  # load data setfrom file
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m * hoRatio)  # 500
    errorCount = 0.0
    for i in range(numTestVecs):  # b[-1] # 最后一行，等同于b[-1,:]
        # 遍历normMat[i, :] 第0第1..第numTestVecs(500)行, normMat[numTestVecs:m, :] numTestVecs到1000行的所有
        # datingLabels[numTestVecs:m] numTestVecs到1000行的所有的label ,k取前3
        classifierResult = classify0(normMat[i, :], normMat[numTestVecs:m, :], datingLabels[numTestVecs:m], 3)
        print("the classifier came back with: %d, the real answer is: %d" % (classifierResult, datingLabels[i]))
        if (classifierResult != datingLabels[i]): errorCount += 1.0
    print("the total error rate is: %f" % (errorCount / float(numTestVecs)))
    print(errorCount)


# 测试程序： 交互输入数据获取分类
def classifyPerson():
    resultList = ['not at all', 'in small doses', 'in large doses']
    percentTats = float(input("percentage of time spent playing video games?"))
    ffMiles = float(input("frequent flier miles earned per year?"))
    iceCream = float(input("liters of ice cream consumed per year?"))
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')  # load data setfrom file
    normMat, ranges, minVals = autoNorm(datingDataMat)
    inArr = array([ffMiles, percentTats, iceCream])
    classifierResult = classify0((inArr - minVals) / ranges, normMat, datingLabels, 3)
    print("You will probably like this person:", resultList[classifierResult - 1])


# datingClassTest()  # 约会对象分类效果测试
# classifyPerson()  # 约会对象实战分类


# 利用分类器进行手写数字识别测试   读取的数字文件是 32行 32列  -------------------------------------------------------------------------------
def img2vector(filename):
    returnVect = zeros((1, 1024))  # 1行 1024列 的0矩阵
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()  # 读到一行的字符List
        for j in range(32):
            # 第0行(returnVect只有一行) 第(32 * i + j)列等于这个位置的字符 例如第一行第一个为0 则在矩阵[0,0]位置为0
            # 一个[00000000001100000000000000000....]的只有一行的矩阵
            returnVect[0, 32 * i + j] = int(lineStr[j])
    return returnVect  # 返回1行 1024列 的矩阵

def handwritingClassTest():
    hwLabels = []
    trainingFileList = listdir('digits/trainingDigits')  # load the training set
    m = len(trainingFileList)  # m = train文件个数 每个数字约100个 10个数字
    trainingMat = zeros((m, 1024))  # m(1000左右)行 1024列 的0矩阵
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]  # take off .txt 如果5_104 的104需要业务逻辑的话有必要这样分
        classNumStr = int(fileNameStr.split('_')[0])  # 取出文件名的第一个元素即 数字
        hwLabels.append(classNumStr)  # 特征标签数字 加入对应index的List
        trainingMat[i, :] = img2vector('digits/trainingDigits/%s' % fileNameStr)  # 第i行=第i文件的1行 1024列 的矩阵
    testFileList = listdir('digits/testDigits')  # iterate through the test set
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]  # take off .txt 如果5_104 的104需要业务逻辑的话有必要这样分
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('digits/testDigits/%s' % fileNameStr)
        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)
        # print "the classifier came back with: %d, the real answer is: %d" % (classifierResult, classNumStr)
        if (classifierResult != classNumStr):
            errorCount += 1.0  # 方法得出的数字和实际文件名数字不同的话
            print("the classifier came back with: %d, the real answer is: %d" % (classifierResult, classNumStr))
    print("\nthe total number of errors is: %d" % errorCount)
    print("\nthe total error rate is: %f" % (errorCount / float(mTest)))


handwritingClassTest()
