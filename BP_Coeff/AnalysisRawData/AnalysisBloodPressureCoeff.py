# -*- coding: utf-8 -*-
#!/usr/bin/env python3

"""
Created on Sat Feb 16 11:01:27 2019

@author: lin
"""


import os
import glob
import re
import pandas as pd
import numpy as np
import os.path

import sys;
sys.path.append("F:\GitSystem\Python\Common")
import CommonTool as ct

import BPTool as bt




"""========== Define  ============================="""
SaveResult2CSV = False # True False



"""========== Load  ============================="""
InputPath = ct.GetFilePath()

"""
TXT Format

File Name
Data1
Data2
Data3
.
.
.
End

"""

"""========== Get Txt File Data  ============================="""
GetFilePath_List = []   # 定义一个列表，用来存放txt文件名
GetAllFileDta_List = []


""" 將 InputPath 路徑下 所有txt開啟並讀取 """
for InputFile in glob.glob(os.path.join(InputPath, '*.txt')):
        GetFilePath_List.append(InputFile)
        GetFileName = os.path.basename(InputFile)

        """ 依照txt檔名，存入個別變數  """
#        if GetFileName == '01_AMP_Reg_60_30_80_S1.txt':
#            with open(InputFile, 'r', newline = '') as filereader:
#                DtaFram_01_AMP_Reg_60_30_80_S1 = pd.read_csv(filereader) # Get Data and ignore first index and PutIn DataFrame format
#                DataArray = np.array(DtaFram_01_AMP_Reg_60_30_80_S1) # DataFrame format PutIn to Array format for turn to Value
#                Dta_01_AMP_Reg_60_30_80_S1 = list(map(int, DataArray)) # String to Value and PutIn List format
#                Dta_01_AMP_Reg_60_30_80_S1 = np.array(Dta_01_AMP_Reg_60_30_80_S1) # List turn to Array
#
#
#                DtaAmp_01_AMP_Reg_60_30_80_S1 = Dta_01_AMP_Reg_60_30_80_S1[0::2] # Divide Amp
#                DtaMMHg_01_AMP_Reg_60_30_80_S1 = Dta_01_AMP_Reg_60_30_80_S1[1::2] # Divide mmHg


        """Get All File Data"""
        with open(InputFile, 'r', newline = '') as filereader:
            for row in filereader:
                row = row.strip().split('\r\n') # Remove Blank then Remove \r\n
                GetAllFileDta_List.append(row)


#print(GetAllFileDta_List[32])

"""========== Arrange All File Data ，分割數據變成一行一行Data ============================="""
FileLength = len(GetAllFileDta_List)
RawDtaLen = 0

# 有幾個END = 幾組RawData，計算END數量 來決定 生成幾組 [] list
for i in range(0,FileLength,1):
    if GetAllFileDta_List[i] == ['END']:
       RawDtaLen = RawDtaLen +1

# 生成[] list分割儲存RawData
RawData_List=[]
RawData_List = [ []* 1 for i in range(RawDtaLen) ] # http://blog.hhjh.tn.edu.tw/biosomeday/?p=655
GroupCnt = 0

# 切割數據
for i in range(0,FileLength,1):

    if GetAllFileDta_List[i] == ['END']:
       GroupCnt = GroupCnt +1
    else:
       RawData_List[GroupCnt].append(GetAllFileDta_List[i])


#print(RawData_List[0][1:])
"""========== Group Raw Data by same Blood Pressure============================="""
# regex = \d{1,}_AMP_Reg_\d{1,}_\d{1,}_\d{1,}\D{0,}\d{1,}

#a= str(RawData_List[0][0]).strip('[]')
#aa ='_AMP'.join(RawData_List[0][0])
#b ='_AMP'
#c=aa+b
#
#
#c1='a'
#c2='b'
#cc=c1+c2
#print("\n c=",c) # AMP


"""========== Process Txt File Data  ============================="""

"""=================================  60 / 30 / 80  ============================"""
SetSystolic = 60
SetDistolic = 30
Cnt_60_30_80 = 10
SetDtaGroupStarIndx = 0

Systolic_60_30_80 = bt.SystolicProcess(SetSystolic, Cnt_60_30_80, RawData_List, SetDtaGroupStarIndx)
Distolic_60_30_80 = bt.DistolicProcess(SetDistolic, Cnt_60_30_80, RawData_List, SetDtaGroupStarIndx)

#AMP = bt.SeparateAmp(RawData_List, SetDtaGroupStarIndx)
#mmHg = bt.SeparateMMhg(RawData_List, 5)

#print("\n a=",Distolic_60_30_80)

"""================================================ 80 / 50 / 80  ==========================="""
SetSystolic = 80
SetDistolic = 50
Cnt_80_50_80 = 10
SetDtaGroupStarIndx = 10

Systolic_80_50_80 = bt.SystolicProcess(SetSystolic, Cnt_80_50_80, RawData_List, SetDtaGroupStarIndx)
Distolic_80_50_80 = bt.DistolicProcess(SetDistolic, Cnt_80_50_80, RawData_List, SetDtaGroupStarIndx)

#print("\n b=",Distolic_80_50_80)
"""================================================ 100 / 65 / 80  ==========================="""
SetSystolic = 100
SetDistolic = 65
Cnt_100_65_80 = 10
SetDtaGroupStarIndx = 20

Systolic_100_65_80 = bt.SystolicProcess(SetSystolic, Cnt_100_65_80, RawData_List, SetDtaGroupStarIndx)
Distolic_100_65_80 = bt.DistolicProcess(SetDistolic, Cnt_100_65_80, RawData_List, SetDtaGroupStarIndx)

#print("\n b=",Distolic_100_65_80)
"""================================================ 120 / 80 / 80  ==========================="""
SetSystolic = 120
SetDistolic = 80
Cnt_120_80_80 = 10
SetDtaGroupStarIndx = 30


Systolic_120_80_80 = bt.SystolicProcess(SetSystolic, Cnt_120_80_80, RawData_List, SetDtaGroupStarIndx)
Distolic_120_80_80 = bt.DistolicProcess(SetDistolic, Cnt_120_80_80, RawData_List, SetDtaGroupStarIndx)

#print("\n b=",Distolic_120_80_80)
"""================================================ 150 / 100 / 80  ==========================="""
SetSystolic = 150
SetDistolic = 100
Cnt_150_100_80 = 10
SetDtaGroupStarIndx = 40

Systolic_150_100_80 = bt.SystolicProcess(SetSystolic, Cnt_150_100_80, RawData_List, SetDtaGroupStarIndx)
Distolic_150_100_80 = bt.DistolicProcess(SetDistolic, Cnt_150_100_80, RawData_List, SetDtaGroupStarIndx)

#print("\n b=",Systolic_150_100_80)
"""================================================ 200 / 150 / 80  ==========================="""
SetSystolic = 200
SetDistolic = 150
Cnt_200_150_80 = 10
SetDtaGroupStarIndx = 50

Systolic_200_150_80 = bt.SystolicProcess(SetSystolic, Cnt_200_150_80, RawData_List, SetDtaGroupStarIndx)
Distolic_200_150_80 = bt.DistolicProcess(SetDistolic, Cnt_200_150_80, RawData_List, SetDtaGroupStarIndx)

#print("\n b=",Systolic_200_150_80)
"""================================================ 255 / 195 / 80  ==========================="""
SetSystolic = 255
SetDistolic = 195
Cnt_255_195_80 = 10
SetDtaGroupStarIndx = 50

Systolic_255_195_80 = bt.SystolicProcess(SetSystolic, Cnt_255_195_80, RawData_List, SetDtaGroupStarIndx)
Distolic_255_195_80 = bt.DistolicProcess(SetDistolic, Cnt_255_195_80, RawData_List, SetDtaGroupStarIndx)

#print("\n b=",Systolic_255_195_80)
"""================================================ Combine ALL Result  ==========================="""
SystolicResult = np.vstack((Systolic_60_30_80,
                            Systolic_80_50_80,
                            Systolic_100_65_80,
                            Systolic_120_80_80,
                            Systolic_150_100_80,
                            Systolic_200_150_80,
                            Systolic_255_195_80))    # vertical stack

DistolicResult = np.vstack((Distolic_60_30_80,
                            Distolic_80_50_80,
                            Distolic_100_65_80,
                            Distolic_120_80_80,
                            Distolic_150_100_80,
                            Distolic_200_150_80,
                            Distolic_255_195_80))    # vertical stack


#print("\n DistolicResult\n", DistolicResult)
"""================================================ Systolic Statistics  ==========================="""



SystolicCoeff_M = SystolicResult[:,5]
SystolicCoeff_H = SystolicResult[:,9]
SystolicCoeff_L = SystolicResult[:,13]



SystolicCoeff_All = np.hstack((SystolicCoeff_M, SystolicCoeff_H, SystolicCoeff_L))
SystolicCoeff_All_Vertical = np.vstack((SystolicCoeff_M, SystolicCoeff_H, SystolicCoeff_L))
#print("\n SystolicCoeff_All_Vertical \n", SystolicCoeff_All_Vertical)
#print("\n SystolicCoeff_All \n", SystolicCoeff_M)


SystolicCoeff_M_CntStatistic = pd.value_counts(SystolicCoeff_M) # 統計各元素出現次數
#print("\n ----- SystolicCoeff_M_CntStatistic -----\n", SystolicCoeff_M_CntStatistic)

SystolicCoeff_H_CntStatistic = pd.value_counts(SystolicCoeff_H) # 統計各元素出現次數
#print("\n ----- SystolicCoeff_H_CntStatistic -----\n", SystolicCoeff_H_CntStatistic)

SystolicCoeff_L_CntStatistic = pd.value_counts(SystolicCoeff_L) # 統計各元素出現次數
#print("\n ----- SystolicCoeff_L_CntStatistic -----\n", SystolicCoeff_L_CntStatistic)

SystolicCoeff_All_CntStatistic = pd.value_counts(SystolicCoeff_All) # 統計各元素出現次數
#print("\n ----- SystolicCoeff_All_CntStatistic -----\n", SystolicCoeff_All_CntStatistic)



print("\n ============== SystolicCoeff_M ==============\n")

SystolicCoeff_M_RemoveZero = filter(lambda x: x > 0, SystolicCoeff_M)
SystolicCoeff_M_RemoveZero = np.array(list(SystolicCoeff_M_RemoveZero))

# Max
Max_SystolicCoeff_M = np.max(SystolicCoeff_M_RemoveZero)
print("Max =", Max_SystolicCoeff_M)

# Min
Min_SystolicCoeff_M = np.min(SystolicCoeff_M_RemoveZero)
print("Min =", Min_SystolicCoeff_M)

# Mean
Mean_SystolicCoeff_M = np.mean(SystolicCoeff_M_RemoveZero)
print("Mean =", Mean_SystolicCoeff_M)

# 标准差
SD_SystolicCoeff_M = np.std(SystolicCoeff_M_RemoveZero)
print("SD =", SD_SystolicCoeff_M)

# Var
Var_SystolicCoeff_M = np.var(SystolicCoeff_M_RemoveZero)
print("Var =", Var_SystolicCoeff_M)


print("\n ============== SystolicCoeff_H ============== \n")

# lambda函数的形式是: lambda x: expression(x)
# lambda允许快速定义单行的最小函数，类似与C语言中的macro，这些叫做lambda的函数，是从LISP借用来的
#>>> g = lambda x: x * 2
#>>> g(3)
#6
SystolicCoeff_H_RemoveZero = filter(lambda x: x > 0, SystolicCoeff_H)
SystolicCoeff_H_RemoveZero = np.array(list(SystolicCoeff_H_RemoveZero))
#print("SystolicCoeff_H_RemoveZero=\n" , SystolicCoeff_H_RemoveZero)

# Max
Max_SystolicCoeff_H = np.max(SystolicCoeff_H_RemoveZero)
print("Max =", Max_SystolicCoeff_H)

# Min
Min_SystolicCoeff_H = np.min(SystolicCoeff_H_RemoveZero)
print("Min =", Min_SystolicCoeff_H)

# Mean
Mean_SystolicCoeff_H = np.mean(SystolicCoeff_H_RemoveZero)
print("Mean =", Mean_SystolicCoeff_H)

# 标准差
SD_SystolicCoeff_H = np.std(SystolicCoeff_H_RemoveZero)
print("SD =", SD_SystolicCoeff_H)

# Var
Var_SystolicCoeff_H = np.var(SystolicCoeff_H_RemoveZero)
print("Var =", Var_SystolicCoeff_H)



print("\n ============== SystolicCoeff_L ============== \n")

SystolicCoeff_L_RemoveZero = filter(lambda x: x > 0, SystolicCoeff_L)
SystolicCoeff_L_RemoveZero = np.array(list(SystolicCoeff_L_RemoveZero))

# Max
Max_SystolicCoeff_L = np.max(SystolicCoeff_L_RemoveZero)
print("Max =", Max_SystolicCoeff_L)

# Min
Min_SystolicCoeff_L = np.min(SystolicCoeff_L_RemoveZero)
print("Min =", Min_SystolicCoeff_L)

# Mean
Mean_SystolicCoeff_L = np.mean(SystolicCoeff_L_RemoveZero)
print("Mean =", Mean_SystolicCoeff_L)

# 标准差
SD_SystolicCoeff_L = np.std(SystolicCoeff_L_RemoveZero)
print("SD =", SD_SystolicCoeff_L)

# Var
Var_SystolicCoeff_L = np.var(SystolicCoeff_L_RemoveZero)
print("Var =", Var_SystolicCoeff_L)


print("\n ============== SystolicCoeff_ALL ============== \n")

SystolicCoeff_All_RemoveZero = filter(lambda x: x > 0, SystolicCoeff_All)
SystolicCoeff_All_RemoveZero = np.array(list(SystolicCoeff_All_RemoveZero))

# Max
Max_SystolicCoeff_All = np.max(SystolicCoeff_All_RemoveZero)
print("Max =", Max_SystolicCoeff_All)

# Min
Min_SystolicCoeff_All = np.min(SystolicCoeff_All_RemoveZero)
print("Min =", Min_SystolicCoeff_All)

# Mean
Mean_SystolicCoeff_All = np.mean(SystolicCoeff_All_RemoveZero)
print("Mean =", Mean_SystolicCoeff_All)

# 标准差
SD_SystolicCoeff_All = np.std(SystolicCoeff_All_RemoveZero)
print("SD =", SD_SystolicCoeff_All)

# Var
Var_SystolicCoeff_All = np.var(SystolicCoeff_All_RemoveZero)
print("Var =", Var_SystolicCoeff_All)


"""================================================ Distolic Statistics  ==========================="""


DistolicCoeff_M = DistolicResult[:,5]
DistolicCoeff_H = DistolicResult[:,9]
DistolicCoeff_L = DistolicResult[:,13]


DistolicCoeff_All = np.hstack((DistolicCoeff_M, DistolicCoeff_H, DistolicCoeff_L))
#print("\n SystolicCoeff_All \n", DistolicCoeff_All)


DistolicCoeff_M_CntStatistic = pd.value_counts(DistolicCoeff_M) # 統計各元素出現次數
#print("\n ----- DistolicCoeff_M_CntStatistic -----\n", SystolicCoeff_M_CntStatistic)

DistolicCoeff_H_CntStatistic = pd.value_counts(DistolicCoeff_H) # 統計各元素出現次數
#print("\n ----- DistolicCoeff_H_CntStatistic -----\n", DistolicCoeff_H_CntStatistic)

DistolicCoeff_L_CntStatistic = pd.value_counts(DistolicCoeff_L) # 統計各元素出現次數
#print("\n ----- DistolicCoeff_L_CntStatistic -----\n", DistolicCoeff_L_CntStatistic)

DistolicCoeff_All_CntStatistic = pd.value_counts(DistolicCoeff_All) # 統計各元素出現次數
#print("\n ----- DistolicCoeff_All_CntStatistic -----\n", DistolicCoeff_All_CntStatistic)


print("\n ============== DistolicCoeff_M ==============\n")

DistolicCoeff_M_RemoveZero = filter(lambda x: x > 0, DistolicCoeff_M)
DistolicCoeff_M_RemoveZero = np.array(list(DistolicCoeff_M_RemoveZero))

# Max
Max_DistolicCoeff_M = np.max(DistolicCoeff_M)
print("Max =", Max_DistolicCoeff_M)

# Min
Min_DistolicCoeff_M = np.min(DistolicCoeff_M)
print("Min =", Min_DistolicCoeff_M)

# Mean
Mean_DistolicCoeff_M = np.mean(DistolicCoeff_M)
print("Mean =", Mean_DistolicCoeff_M)

# 标准差
SD_DistolicCoeff_M = np.std(DistolicCoeff_M)
print("SD =", SD_DistolicCoeff_M)

# Var
Var_DistolicCoeff_M = np.var(DistolicCoeff_M)
print("Var =", Var_DistolicCoeff_M)


print("\n ============== DistolicCoeff_H ============== \n")


DistolicCoeff_H_RemoveZero = filter(lambda x: x > 0, DistolicCoeff_H)
DistolicCoeff_H_RemoveZero = np.array(list(DistolicCoeff_H_RemoveZero))
#print("SystolicCoeff_H_RemoveZero=\n" , SystolicCoeff_H_RemoveZero)

# Max
Max_DistolicCoeff_H = np.max(DistolicCoeff_H_RemoveZero)
print("Max =", Max_DistolicCoeff_H)

# Min
Min_DistolicCoeff_H = np.min(DistolicCoeff_H_RemoveZero)
print("Min =", Min_DistolicCoeff_H)

# Mean
Mean_DistolicCoeff_H = np.mean(DistolicCoeff_H_RemoveZero)
print("Mean =", Mean_DistolicCoeff_H)

# 标准差
SD_DistolicCoeff_H = np.std(DistolicCoeff_H_RemoveZero)
print("SD =", SD_DistolicCoeff_H)

# Var
Var_DistolicCoeff_H = np.var(DistolicCoeff_H_RemoveZero)
print("Var =", Var_DistolicCoeff_H)



print("\n ============== DistolicCoeff_L ============== \n")

DistolicCoeff_L_RemoveZero = filter(lambda x: x > 0, DistolicCoeff_L)
DistolicCoeff_L_RemoveZero = np.array(list(DistolicCoeff_L_RemoveZero))

# Max
Max_DistolicCoeff_L = np.max(DistolicCoeff_L_RemoveZero)
print("Max =", Max_DistolicCoeff_L)

# Min
Min_DistolicCoeff_L = np.min(DistolicCoeff_L_RemoveZero)
print("Min =", Min_DistolicCoeff_L)

# Mean
Mean_DistolicCoeff_L = np.mean(DistolicCoeff_L_RemoveZero)
print("Mean =", Mean_DistolicCoeff_L)

# 标准差
SD_DistolicCoeff_L = np.std(DistolicCoeff_L_RemoveZero)
print("SD =", SD_DistolicCoeff_L)

# Var
Var_DistolicCoeff_L = np.var(DistolicCoeff_L_RemoveZero)
print("Var =", Var_DistolicCoeff_L)


print("\n ============== DistolicCoeff_All ============== \n")

DistolicCoeff_All_RemoveZero = filter(lambda x: x > 0, DistolicCoeff_All)
DistolicCoeff_All_RemoveZero = np.array(list(DistolicCoeff_All_RemoveZero))

# Max
Max_DistolicCoeff_All = np.max(SystolicCoeff_All_RemoveZero)
print("Max =", Max_DistolicCoeff_All)

# Min
Min_DistolicCoeff_All = np.min(SystolicCoeff_All_RemoveZero)
print("Min =", Min_DistolicCoeff_All)

# Mean
Mean_DistolicCoeff_All = np.mean(SystolicCoeff_All_RemoveZero)
print("Mean =", Mean_DistolicCoeff_All)

# 标准差
SD_DistolicCoeff_All = np.std(SystolicCoeff_All_RemoveZero)
print("SD =", SD_DistolicCoeff_All)

# Var
Var_DistolicCoeff_All = np.var(SystolicCoeff_All_RemoveZero)
print("Var =", Var_DistolicCoeff_All)

"""================================================ Dump data to CSV  ==========================="""


if SaveResult2CSV == True:
    np.savetxt('Systolic.csv', SystolicResult, delimiter = ',')
    np.savetxt('Distolic.csv', SystolicResult, delimiter = ',')

#a = np.asarray([ [1,2,3], [4,5,6], [7,8,9] ])
#np.savetxt('new.csv', a, delimiter = ',')
