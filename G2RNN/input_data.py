# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 15:15:50 2018

@author: Administrator
"""

import numpy as np
import pandas as pd
import pickle as pkl


def load_st_data(dataset):
    st_adj = pd.read_csv(r'data/dis.csv',header=None)
    adj = np.mat(st_adj)

    st_tf = pd.read_csv(r'data/vpsdata1.csv')
    return st_tf, adj

def load_los_data(dataset):
    los_adj = pd.read_csv(r'data/los_adj.csv',header=None)
    adj = np.mat(los_adj)
    los_tf = pd.read_csv(r'data/los_speed.csv')
    return los_tf, adj


def preprocess_data(data, time_len, rate, seq_len, pre_len):
    train_size = int(time_len * rate)
    train_data = data[0:train_size]
    test_data = data[train_size:time_len]
    
    trainX, trainY, testX, testY = [], [], [], []
    for i in range(len(train_data) - seq_len - pre_len):
        a = train_data[i: i + seq_len + pre_len]
        trainX.append(a[0 : seq_len])
        trainY.append(a[seq_len : seq_len + pre_len])
        # trainY.append(a[:, -1])
    for i in range(len(test_data) - seq_len -pre_len):
        b = test_data[i: i + seq_len + pre_len]
        testX.append(b[0 : seq_len])
        testY.append(b[seq_len : seq_len + pre_len])
        # testY.append(b[:,-1])
        #
    trainX1 = np.array(trainX)
    trainY1 = np.array(trainY)

    testX1 = np.array(testX)
    testY1 = np.array(testY)
    return trainX1, trainY1, testX1, testY1
    
