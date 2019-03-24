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
import Common as cm
import Statistics as Stat

import BPTool as bt


"""========== Define  ============================="""
SaveResult2CSV = False # True False

Print_SystolicAllCoeff = False
Print_DistolicAllCoeff = False

"""========== Load  ============================="""
InputPath = cm.GetFilePath()

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

Systolic_60_30_80 = bt.SystolicProcess(SetSystolic, Cnt_60_30_80, RawData_List, SetDtaGroupStarIndx, False)
Distolic_60_30_80 = bt.DistolicProcess(SetDistolic, Cnt_60_30_80, RawData_List, SetDtaGroupStarIndx, False)



print("\n ============== SystolicCoeff_M , 60 / 30 / 80 ==============\n")
SystolicCoeff_M = bt.GetCoeff_M(Systolic_60_30_80, 5, False)
AryRemoveZero = cm.FilterAryValue(SystolicCoeff_M, 0, False)
Stat.BasicStatistic(AryRemoveZero, True)


"""================================================ 80 / 50 / 80  ==========================="""
SetSystolic = 80
SetDistolic = 50
Cnt_80_50_80 = 10
SetDtaGroupStarIndx = 10

Systolic_80_50_80 = bt.SystolicProcess(SetSystolic, Cnt_80_50_80, RawData_List, SetDtaGroupStarIndx, False)
Distolic_80_50_80 = bt.DistolicProcess(SetDistolic, Cnt_80_50_80, RawData_List, SetDtaGroupStarIndx, False)

#print("\n b=",Distolic_80_50_80)
"""================================================ 100 / 65 / 80  ==========================="""
SetSystolic = 100
SetDistolic = 65
Cnt_100_65_80 = 10
SetDtaGroupStarIndx = 20

Systolic_100_65_80 = bt.SystolicProcess(SetSystolic, Cnt_100_65_80, RawData_List, SetDtaGroupStarIndx, False)
Distolic_100_65_80 = bt.DistolicProcess(SetDistolic, Cnt_100_65_80, RawData_List, SetDtaGroupStarIndx, False)

#print("\n b=",Distolic_100_65_80)
"""================================================ 120 / 80 / 80  ==========================="""
SetSystolic = 120
SetDistolic = 80
Cnt_120_80_80 = 10
SetDtaGroupStarIndx = 30


Systolic_120_80_80 = bt.SystolicProcess(SetSystolic, Cnt_120_80_80, RawData_List, SetDtaGroupStarIndx, False)
Distolic_120_80_80 = bt.DistolicProcess(SetDistolic, Cnt_120_80_80, RawData_List, SetDtaGroupStarIndx, False)

#print("\n b=",Distolic_120_80_80)
"""================================================ 150 / 100 / 80  ==========================="""
SetSystolic = 150
SetDistolic = 100
Cnt_150_100_80 = 10
SetDtaGroupStarIndx = 40

Systolic_150_100_80 = bt.SystolicProcess(SetSystolic, Cnt_150_100_80, RawData_List, SetDtaGroupStarIndx, False)
Distolic_150_100_80 = bt.DistolicProcess(SetDistolic, Cnt_150_100_80, RawData_List, SetDtaGroupStarIndx, False)

#print("\n b=",Systolic_150_100_80)
"""================================================ 200 / 150 / 80  ==========================="""
SetSystolic = 200
SetDistolic = 150
Cnt_200_150_80 = 10
SetDtaGroupStarIndx = 50

Systolic_200_150_80 = bt.SystolicProcess(SetSystolic, Cnt_200_150_80, RawData_List, SetDtaGroupStarIndx, False)
Distolic_200_150_80 = bt.DistolicProcess(SetDistolic, Cnt_200_150_80, RawData_List, SetDtaGroupStarIndx, False)

#print("\n b=",Systolic_200_150_80)
"""================================================ 255 / 195 / 80  ==========================="""
SetSystolic = 255
SetDistolic = 195
Cnt_255_195_80 = 10
SetDtaGroupStarIndx = 50

Systolic_255_195_80 = bt.SystolicProcess(SetSystolic, Cnt_255_195_80, RawData_List, SetDtaGroupStarIndx, False)
Distolic_255_195_80 = bt.DistolicProcess(SetDistolic, Cnt_255_195_80, RawData_List, SetDtaGroupStarIndx, False)

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
"""================================================ ALL Systolic Statistics  ==========================="""


SystolicCoeff_M = bt.GetCoeff_M(SystolicResult, 5, False)
SystolicCoeff_H = bt.GetCoeff_H(SystolicResult, 9, False)
SystolicCoeff_L = bt.GetCoeff_L(SystolicResult, 13, False)
SystolicCoeff_All = np.hstack((SystolicCoeff_M, SystolicCoeff_H, SystolicCoeff_L))


Stat.DataValueCounts(SystolicCoeff_M, False)
Stat.DataValueCounts(SystolicCoeff_H, False)
Stat.DataValueCounts(SystolicCoeff_L, False)
Stat.DataValueCounts(SystolicCoeff_All, False)


print("\n ============== SystolicCoeff_M  ,ALL==============\n")

AryRemoveZero = cm.FilterAryValue(SystolicCoeff_M, 0, False)
Stat.BasicStatistic(AryRemoveZero, Print_SystolicAllCoeff)


print("\n ============== SystolicCoeff_H ,ALL============== \n")

AryRemoveZero = cm.FilterAryValue(SystolicCoeff_H, 0, False)
Stat.BasicStatistic(AryRemoveZero, Print_SystolicAllCoeff)


print("\n ============== SystolicCoeff_L ,ALL============== \n")

AryRemoveZero = cm.FilterAryValue(SystolicCoeff_L, 0, False)
Stat.BasicStatistic(AryRemoveZero, Print_SystolicAllCoeff)


print("\n ============== SystolicCoeff_ALL ,ALL============== \n")

AryRemoveZero = cm.FilterAryValue(SystolicCoeff_All, 0, False)
Stat.BasicStatistic(AryRemoveZero, Print_SystolicAllCoeff)

"""================================================ Distolic Statistics  ==========================="""


DistolicCoeff_M = bt.GetCoeff_M(DistolicResult, 5, False)
DistolicCoeff_H = bt.GetCoeff_H(DistolicResult, 9, False)
DistolicCoeff_L = bt.GetCoeff_L(DistolicResult, 13, False)
DistolicCoeff_All = np.hstack((DistolicCoeff_M, DistolicCoeff_H, DistolicCoeff_L))

Stat.DataValueCounts(DistolicCoeff_M, False)
Stat.DataValueCounts(DistolicCoeff_H, False)
Stat.DataValueCounts(DistolicCoeff_L, False)
Stat.DataValueCounts(DistolicCoeff_All, False)

print("\n ============== DistolicCoeff_M, All ==============\n")

AryRemoveZero = cm.FilterAryValue(DistolicCoeff_M, 0, False)
Stat.BasicStatistic(AryRemoveZero, Print_DistolicAllCoeff)

print("\n ============== DistolicCoeff_H ,ALL============== \n")

AryRemoveZero = cm.FilterAryValue(DistolicCoeff_H, 0, False)
Stat.BasicStatistic(AryRemoveZero, Print_DistolicAllCoeff)

print("\n ============== DistolicCoeff_L ,ALL============== \n")

AryRemoveZero = cm.FilterAryValue(DistolicCoeff_L, 0, False)
Stat.BasicStatistic(AryRemoveZero, Print_DistolicAllCoeff)


print("\n ============== DistolicCoeff_All ,ALL============== \n")

AryRemoveZero = cm.FilterAryValue(DistolicCoeff_All, 0, False)
Stat.BasicStatistic(AryRemoveZero, Print_DistolicAllCoeff)

"""================================================ Dump data to CSV  ==========================="""


if SaveResult2CSV == True:
    np.savetxt('Systolic.csv', SystolicResult, delimiter = ',')
    np.savetxt('Distolic.csv', SystolicResult, delimiter = ',')

#a = np.asarray([ [1,2,3], [4,5,6], [7,8,9] ])
#np.savetxt('new.csv', a, delimiter = ',')
