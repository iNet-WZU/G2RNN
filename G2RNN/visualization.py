#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from sklearn.metrics import mean_squared_error,mean_absolute_error
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import xlwt
def mape(y_pred,y_true):
    n = len(y_true)
    mape = sum(np.abs((y_true - y_pred) / y_true)) / n * 100
    return mape

def smape(y_pred,y_true):
    n = len(y_true)
    smape = sum(np.abs((y_true-y_pred)/(np.abs(y_pred)+np.abs(y_true)/2)))/n*100
    return smape

def mae_value(y_true,y_pred):
    n = len(y_true)
    mae = sum(np.abs(y_true - y_pred)) / n
    return mae


def rmse_value(y_pred,y_true):
    n = len(y_true)
    rmse = math.sqrt(sum(np.square(y_true - y_pred)) / n)
    return rmse

def plot_result(test_result,test_label1,path):

    workbook1 = xlwt.Workbook(encoding='utf-8')
    worksheet1 = workbook1.add_sheet('sheet1')
    workbook2 = xlwt.Workbook(encoding='utf-8')
    worksheet2 = workbook2.add_sheet('sheet1')
    workbook3 = xlwt.Workbook(encoding='utf-8')
    worksheet3 = workbook3.add_sheet('sheet1')
    workbook4 = xlwt.Workbook(encoding='utf-8')
    worksheet4 = workbook4.add_sheet('sheet1')
    workbook5 = xlwt.Workbook(encoding='utf-8')
    worksheet5 = workbook5.add_sheet('sheet1')
    workbook6 = xlwt.Workbook(encoding='utf-8')
    worksheet6 = workbook6.add_sheet('sheet1')
    workbook7 = xlwt.Workbook(encoding='utf-8')
    worksheet7 = workbook7.add_sheet('sheet1')

    ##all test result visualization
    fig1 = plt.figure(figsize=(7,1.5))
#    ax1 = fig1.add_subplot(1,1,1)
    a1_pred = test_result[:,0]
    a1_true = test_label1[:,0]
    MAE1 = mae_value(a1_true,a1_pred)
    RMSE1 = rmse_value(a1_pred,a1_true)
    MAPE1 = mape(a1_pred,a1_true)
    a2_pred = test_result[:,1]
    a2_true = test_label1[:,1]
    MAE2 = mae_value(a2_true,a2_pred)
    RMSE2 = rmse_value(a2_pred,a2_true)
    MAPE2 = smape(a2_pred,a2_true)
    a3_pred = test_result[:,2]
    a3_true = test_label1[:,2]
    MAE3 = mae_value(a3_true,a3_pred)
    RMSE3 = rmse_value(a3_pred,a3_true)
    MAPE3 = smape(a3_pred,a3_true)
    a4_pred = test_result[:,3]
    a4_true = test_label1[:,3]
    MAE4 = mae_value(a4_true,a4_pred)
    RMSE4 = rmse_value(a4_pred,a4_true)
    MAPE4 = smape(a4_pred,a4_true)
    a5_pred = test_result[:,4]
    a5_true = test_label1[:,4]
    MAE5 = mae_value(a5_true,a5_pred)
    RMSE5 = rmse_value(a5_pred,a5_true)
    MAPE5 = smape(a5_pred,a5_true)
    a6_pred = test_result[:,5]
    a6_true = test_label1[:,5]
    MAE6 = mae_value(a6_true,a6_pred)
    RMSE6 = rmse_value(a6_pred,a6_true)
    MAPE6 = mape(a6_pred,a6_true)
    a7_pred = test_result[:,6]
    a7_true = test_label1[:,6]
    MAE7 = mae_value(a7_true,a7_pred)
    RMSE7 = rmse_value(a7_pred,a7_true)
    MAPE7 = mape(a7_pred,a7_true)

    worksheet1.write(0,0,RMSE1)
    worksheet1.write(0,1,MAE1)
    worksheet1.write(0,2,MAPE1)
    worksheet2.write(0,0, RMSE2)
    worksheet2.write(0,1, MAE2)
    worksheet2.write(0,2,MAPE2)
    worksheet3.write(0,0, RMSE3)
    worksheet3.write(0,1, MAE3)
    worksheet3.write(0, 2, MAPE3)
    worksheet4.write(0,0, RMSE4)
    worksheet4.write(0,1, MAE4)
    worksheet4.write(0,2, MAPE4)
    worksheet5.write(0,0, RMSE5)
    worksheet5.write(0,1, MAE5)
    worksheet5.write(0,2, MAPE5)
    worksheet6.write(0,0, RMSE6)
    worksheet6.write(0,1, MAE6)
    worksheet6.write(0,2, MAPE6)
    worksheet7.write(0,0, RMSE7)
    worksheet7.write(0,1, MAE7)
    worksheet7.write(0,2, MAPE7)

    workbook1.save(path+'/st1.xls')
    workbook2.save(path+'/st2.xls')
    workbook3.save(path+'/st3.xls')
    workbook4.save(path+'/st4.xls')
    workbook5.save(path+'/st5.xls')
    workbook6.save(path+'/st6.xls')
    workbook7.save(path+'/st7.xls')

    fig1 = plt.figure(figsize=(7,1.5))
    plt.plot(a1_pred,'r-',label='prediction')
    plt.plot(a1_true,'b-',label='true')
    plt.legend(loc='best', fontsize=10)
    plt.savefig(path+'/st1.jpg')

    fig1 = plt.figure(figsize=(7,1.5))
    plt.plot(a2_pred,'r-',label='prediction')
    plt.plot(a2_true,'b-',label='true')
    plt.legend(loc='best', fontsize=10)
    plt.savefig(path+'/st2.jpg')

    fig1 = plt.figure(figsize=(7,1.5))
    plt.plot(a3_pred,'r-',label='prediction')
    plt.plot(a3_true,'b-',label='true')
    plt.legend(loc='best', fontsize=10)
    plt.savefig(path+'/st3.jpg')

    fig1 = plt.figure(figsize=(7,1.5))
    plt.plot(a4_pred,'r-',label='prediction')
    plt.plot(a4_true,'b-',label='true')
    plt.legend(loc='best', fontsize=10)
    plt.savefig(path+'/st4.jpg')
    fig1 = plt.figure(figsize=(7,1.5))

    plt.plot(a5_pred,'r-',label='prediction')
    plt.plot(a5_true,'b-',label='true')
    plt.legend(loc='best', fontsize=10)
    plt.savefig(path+'/st5.jpg')
    # fig1 = plt.figure(figsize=(7,1.5))

    plt.plot(a6_pred,'r-',label='prediction')
    plt.plot(a6_true,'b-',label='true')
    plt.legend(loc='best', fontsize=10)
    plt.savefig(path+'/st6.jpg')
    fig1 = plt.figure(figsize=(7,1.5))
    plt.plot(a7_pred,'r-',label='prediction')
    plt.plot(a7_true,'b-',label='true')
    plt.legend(loc='best', fontsize=10)
    plt.savefig(path+'/st7.jpg')


def plot_error(train_rmse,train_loss,test_rmse,test_acc,test_mae,path):
    ###train_rmse & test_rmse
    fig1 = plt.figure(figsize=(5,3))
    plt.plot(train_rmse, 'r-', label="train_rmse")
    plt.plot(test_rmse, 'b-', label="test_rmse")
    plt.legend(loc='best',fontsize=10)
    plt.savefig(path+'/rmse.jpg')
    # plt.show()
    #### train_loss & train_rmse
    fig1 = plt.figure(figsize=(5,3))
    plt.plot(train_loss,'b-', label='train_loss')
    plt.legend(loc='best',fontsize=10)
    plt.savefig(path+'/train_loss.jpg')
    # plt.show()

    fig1 = plt.figure(figsize=(5,3))
    plt.plot(train_rmse,'b-', label='train_rmse')
    plt.legend(loc='best',fontsize=10)
    plt.savefig(path+'/train_rmse.jpg')
    # plt.show()

    ### accuracy
    fig1 = plt.figure(figsize=(5,3))
    plt.plot(test_acc, 'b-', label="test_acc")
    plt.legend(loc='best',fontsize=10)
    plt.savefig(path+'/test_acc.jpg')
    # plt.show()
    ### rmse
    fig1 = plt.figure(figsize=(5,3))
    plt.plot(test_rmse, 'b-', label="test_rmse")
    plt.legend(loc='best',fontsize=10)
    plt.savefig(path+'/test_rmse.jpg')
    # plt.show()
    ### mae
    fig1 = plt.figure(figsize=(5,3))
    plt.plot(test_mae, 'b-', label="test_mae")
    plt.legend(loc='best',fontsize=10)
    plt.savefig(path+'/test_mae.jpg')
    # plt.show()


