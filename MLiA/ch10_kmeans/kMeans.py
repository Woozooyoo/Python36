#coding=utf-8
"""
Created on Feb 16, 2011
k Means Clustering for Ch10 of Machine Learning in Action
@author: Peter Harrington
"""
from numpy import *

def loadDataSet(fileName):      #general function to parse tab -delimited floats
    dataMat = []                #assume last column is target value
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        floatLine = list(map(float,curLine)) #map all elements from Str to float()
        dataMat.append(floatLine)
    return dataMat  # len80的list 每一个元素是一个len2(x,y)的list 即80行 2列

def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2))) #la.norm(vecA-vecB) 求两个向量之间的距离

def randCent(dataSet, k):   # 创造k(4)个随机点作为初始中心点
    n = shape(dataSet)[1]   # dataSet是几列  2
    centroids = mat(zeros((k,n)))  #create centroid mat
    for j in range(n):#create random cluster centers, within bounds of each dimension
        minJ = min(dataSet[:,j])    # 第 j列的最小值
        rangeJ = float(max(dataSet[:,j]) - minJ) # 第 j列的最大值和最小值的差
        centroids[:,j] = minJ + rangeJ * random.rand(k,1)  # 4行1列的随机0-1矩阵 * 范围值 + 最小值
    return centroids    # 4行2列的矩阵 即4个随机中心点

def kMeans(dataSet, k, distMeas=distEclud, createCent=randCent):
    m = shape(dataSet)[0]   # m 80
    clusterAssment = mat(zeros((m,2)))#create mat to assign data points
                                      #to a centroid, also holds SE of each point
    centroids = createCent(dataSet, k) # 创造k个随机点作为初始中心点
    clusterChanged = True   ## 用来判断是否收敛
    while clusterChanged:
        clusterChanged = False
        for i in range(m):   #for each data point assign it to the closest centroid
            minDist = inf
            minIndex = -1
            for j in range(k):  # 寻找出最近的质心
                distJI = distMeas(centroids[j,:],dataSet[i,:]) # 第j(0-3)个中心点到 第i(0-80)个点的距离
                if distJI < minDist:
                    minDist = distJI; minIndex = j  # 最小距离和 最小距离所属的中心点索引
            if clusterAssment[i,0] != minIndex: clusterChanged = True
            clusterAssment[i,:] = minIndex,minDist**2   # 算术平均数的平方根
        print(centroids)    # 通过这里发现几次迭代得到了中心点
        # 更新质心的位置
        for cent in range(k):#recalculate centroids
            # 哪几行是 符合 clusterAssment[:,0].A==cent 这个条件的
            pointsInClust = dataSet[nonzero(clusterAssment[:,0].A==cent)[0]]#依次得到所有中心索引为0\1\2\3的点 get all the point in this cluster
            centroids[cent,:] = mean(pointsInClust, axis=0) #按照一行一行的方向求所有点的平均值x,y坐标赋给这个中心点新值assign centroid to mean
    return centroids, clusterAssment

# 用测试数据及测试kmeans算法 -------------------------------------------------------------------------------
datMat = mat(loadDataSet('testSet.txt'))
myCentroids,clustAssing = kMeans(datMat,4) #4是分四类
print(myCentroids)
print(clustAssing)
import matplotlib.pyplot as plt
# 二维图
ax = plt.figure().add_subplot(111)
ax.scatter(datMat[:,0].tolist(),datMat[:,1].tolist(),15.0*array(clustAssing[:,0]+7),15.0*array(clustAssing[:,0])+50)
plt.show()


# Sum of Squared Error误差平方和优化 clusterAssment[:,1]越小越好 取出同一簇里sum(clusterAssment[:,1])最大的 对它使用2-means算法
# binaryKmeans 优化版的K均值
def biKmeans(dataSet, k, distMeas=distEclud):
    m = shape(dataSet)[0]   # m = 69 dataSet的行数69
    clusterAssment = mat(zeros((m,2)))
    centroid0 = mean(dataSet, axis=0).tolist()[0]   # 按一行一行取均值的转列表 取出列表内唯一个中心点坐标
    centList =[centroid0] #create a list with one centroid 创建一个初始所有点均值的簇
    for j in range(m):#calc initial Error
        clusterAssment[j,1] = distMeas(mat(centroid0), dataSet[j,:])**2
    while (len(centList) < k):
        lowestSSE = inf
        for i in range(len(centList)):  # 尝试划分每一簇
            ptsInCurrCluster = dataSet[nonzero(clusterAssment[:,0].A==i)[0],:]#get the data points currently in cluster i
            centroidMat, splitClustAss = kMeans(ptsInCurrCluster, 2, distMeas)
            sseSplit = sum(splitClustAss[:,1])#compare the SSE to the currrent minimum
            sseNotSplit = sum(clusterAssment[nonzero(clusterAssment[:,0].A!=i)[0],1]) #
            print("sseSplit, and notSplit: ", sseSplit, sseNotSplit)
            if (sseSplit + sseNotSplit) < lowestSSE:
                bestCentToSplit = i
                bestNewCents = centroidMat
                bestClustAss = splitClustAss.copy()
                lowestSSE = sseSplit + sseNotSplit
        bestClustAss[nonzero(bestClustAss[:,0].A == 1)[0],0] = len(centList) #change 1 to 3,4, or whatever
        bestClustAss[nonzero(bestClustAss[:,0].A == 0)[0],0] = bestCentToSplit  # 更新簇的分配结果
        print('the bestCentToSplit is: ', bestCentToSplit)
        print('the len of bestClustAss is: ', len(bestClustAss))
        centList[bestCentToSplit] = bestNewCents[0,:].tolist()[0]#replace a centroid with two best centroids
        centList.append(bestNewCents[1,:].tolist()[0])
        clusterAssment[nonzero(clusterAssment[:,0].A == bestCentToSplit)[0],:]= bestClustAss#reassign new clusters, and SSE
    return mat(centList), clusterAssment

import urllib
import json
def geoGrab(stAddress, city):
    apiStem = 'http://where.yahooapis.com/geocode?'  #create a dict and constants for the goecoder
    params = {}
    params['flags'] = 'J'#JSON return type
    params['appid'] = 'aaa0VN6k'
    params['location'] = '%s %s' % (stAddress, city)
    url_params = urllib.urlencode(params)
    yahooApi = apiStem + url_params      #print url_params
    print(yahooApi)
    c=urllib.urlopen(yahooApi)
    return json.loads(c.read())

from time import sleep
def massPlaceFind(fileName):
    fw = open('places.txt', 'w')
    for line in open(fileName).readlines():
        line = line.strip()
        lineArr = line.split('\t')
        retDict = geoGrab(lineArr[1], lineArr[2])
        if retDict['ResultSet']['Error'] == 0:
            lat = float(retDict['ResultSet']['Results'][0]['latitude'])
            lng = float(retDict['ResultSet']['Results'][0]['longitude'])
            print("%s\t%f\t%f" % (lineArr[0], lat, lng))
            fw.write('%s\t%f\t%f\n' % (line, lat, lng))
        else:print("error fetching")
        sleep(1)
    fw.close()

def distSLC(vecA, vecB):#Spherical Law of Cosines 球面余弦定理
    a = sin(vecA[0,1]*pi/180) * sin(vecB[0,1]*pi/180)
    b = cos(vecA[0,1]*pi/180) * cos(vecB[0,1]*pi/180) * \
                      cos(pi * (vecB[0,0]-vecA[0,0]) /180)
    return arccos(a + b)*6371.0 #pi is imported with numpy

import matplotlib
import matplotlib.pyplot as plt
def clusterClubs(numClust=5):
    datList = []
    for line in open('places.txt').readlines():
        lineArr = line.split('\t')
        datList.append([float(lineArr[4]), float(lineArr[3])])
    datMat = mat(datList)
    myCentroids, clustAssing = biKmeans(datMat, numClust, distMeas=distSLC)
    fig = plt.figure()
    rect=[0.1,0.1,0.8,0.8]
    scatterMarkers=['s', 'o', '^', '8', 'p','d', 'v', 'h', '>', '<']
    axprops = dict(xticks=[], yticks=[])
    ax0=fig.add_axes(rect, label='ax0', **axprops)
    imgP = plt.imread('Portland.png')
    ax0.imshow(imgP)
    ax1=fig.add_axes(rect, label='ax1', frameon=False)
    for i in range(numClust):
        ptsInCurrCluster = datMat[nonzero(clustAssing[:,0].A==i)[0],:]
        markerStyle = scatterMarkers[i % len(scatterMarkers)]
        ax1.scatter(ptsInCurrCluster[:,0].flatten().A[0], ptsInCurrCluster[:,1].flatten().A[0], marker=markerStyle, s=90)
    ax1.scatter(myCentroids[:,0].flatten().A[0], myCentroids[:,1].flatten().A[0], marker='+', s=300)
    plt.show()


clusterClubs(3)