# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 13:10:01 2018

@author: Administrator
"""

from MLiA.ch04_Naive_Bayes.Mail_filter import *

if __name__ == "__main__":

    wordlist, classlist = loadDataSet()
    
    myVoc = Create_wordVec(wordlist)
    print(myVoc)
    print(Words2Vec(myVoc, wordlist[0]))
    
    train_matrix = []
    for doc in wordlist:
        train_matrix.append(Words2Vec(myVoc, doc))
    
    print(train_matrix)
    p1,p2,p_pos = train_bayes(train_matrix, classlist)
    print(p1,p2,p_pos)
    
    Test_classify()
    Spam_filter('email')
