# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
Created on Sun Feb 24 15:59:36 2019

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


"""========== Find Max Value in array  ============================="""
def MaxAmp(AmpArray): # 找最大值，格式須為 numpy array

    MaxAmpValue = np.max(AmpArray)
    MaxAmpIndex = np.argmax(AmpArray)
#   MaxAmpIndex = AmpArray.index(np.max(AmpArray)) # Using array is List format
    return MaxAmpValue, MaxAmpIndex  # 回傳最大值


"""========== Calculate Blood Pressure Coeff  ============================="""
def BP_Coeff(MaxAmp, BpAmp): # 算血壓係數
    Coeff = 1/(MaxAmp / BpAmp)
    Coeff = np.around(Coeff, decimals=2) #小數點第2位後作4捨5入
    return Coeff


"""========== Calculate Target mmHg, mmHgIndex, Amp, Coeff  ============================="""
def TargetmmHg_Coeff(AmpArray, mmHgArray, SetFindSystolic, MaxAmpValue): # 格式須為 numpy array

    Systolic_mmHg = ct.FindNearest(mmHgArray,SetFindSystolic)
    Systolic_mmHgValue = Systolic_mmHg[0]
    Systolic_mmHgIndex = Systolic_mmHg[1]

    Systolic_Amp = AmpArray[Systolic_mmHgIndex]
    Systolic_Coeff = BP_Coeff(MaxAmpValue[0],Systolic_Amp)
#    print(Systolic_mmHgIndex)
    return Systolic_mmHgValue, Systolic_mmHgIndex, Systolic_Amp, Systolic_Coeff


"""========== Calculate Near within Five of Blood Pressure Coeff  ============================="""
def ChkTargetmmHg_NearWithinFive(AmpArray, mmHgArray, SetSystolic, MaxAmpValue, SetSystolicIndex): # 找最大值位置，格式須為 numpy array

    Systolic_mmHg = mmHgArray[SetSystolicIndex]

    if np.abs(Systolic_mmHg - SetSystolic) <= 5:
        Target_mmHgIndx_Coeff = TargetmmHg_Coeff(AmpArray, mmHgArray, Systolic_mmHg, MaxAmpValue)
    else:
        Target_mmHgIndx_Coeff = np.zeros(4)

    return Target_mmHgIndx_Coeff


"""========== Calculate Systolic Coeff  ============================="""
def SystolicCoeffProcess(ArrayAmp, ArraymmHg, SetmmHg):

    # tuple format
    MaxAmpDta = MaxAmp(ArrayAmp)
    Systolic_M = TargetmmHg_Coeff(ArrayAmp, ArraymmHg, SetmmHg, MaxAmpDta)

    # 檢查Systolic後一位，是否超出範圍
    if (Systolic_M[1]+1) < len(ArraymmHg):
        Systolic_H = ChkTargetmmHg_NearWithinFive(ArrayAmp, ArraymmHg, SetmmHg, MaxAmpDta, Systolic_M[1]+1)
    else:
        Systolic_H = np.zeros(4)

    # 檢查Systolic前一位，是否超出範圍
    if (Systolic_M[1]-1) >= 0:
        Systolic_L = ChkTargetmmHg_NearWithinFive(ArrayAmp, ArraymmHg, SetmmHg, MaxAmpDta, Systolic_M[1]-1)
    else:
        Systolic_L = np.zeros(4)

    # Turn to nparray format
    MaxAmpDta  = np.array(MaxAmpDta,  dtype= float) # turn to nparray format float
    Systolic_M = np.array(Systolic_M, dtype= float) # turn to nparray format
    Systolic_H = np.array(Systolic_H, dtype= float) # turn to nparray format
    Systolic_L = np.array(Systolic_L, dtype= float) # turn to nparray format

#    np.set_printoptions(precision=3) # 設定Array顯示到小數點第三位，方便觀察用
    np.set_printoptions(suppress=True)# 不顯示科學符號

    """ AmpValue  ,AmpIndex  ,SystolicValue ,SystolicIndex  ,SystolicAmpValue  ,SystolicCoeff  , H*4 ,L*4   """
    # Horizontal Combine Result
    CombineResult_Horizontal = np.hstack((MaxAmpDta, Systolic_M, Systolic_H, Systolic_L))

    return CombineResult_Horizontal


"""========== Calculate Distolic Coeff  ============================="""
def DistolicCoeffProcess(ArrayAmp, ArraymmHg, SetmmHg):

    # tuple format
    MaxAmpDta = MaxAmp(ArrayAmp)
    Distolic_M = TargetmmHg_Coeff(ArrayAmp, ArraymmHg, SetmmHg, MaxAmpDta)

    # 檢查Distolic後一位，是否超出範圍
    if (Distolic_M[1]+1) < len(ArraymmHg):
        Distolic_H = ChkTargetmmHg_NearWithinFive(ArrayAmp, ArraymmHg, SetmmHg, MaxAmpDta, Distolic_M[1]+1)
    else:
        Distolic_H = np.zeros(4)

    # 檢查Distolic前一位，是否超出範圍
    if (Distolic_M[1]-1) >= 0:
        Distolic_L = ChkTargetmmHg_NearWithinFive(ArrayAmp, ArraymmHg, SetmmHg, MaxAmpDta, Distolic_M[1]-1)
    else:
        Distolic_L = np.zeros(4)


    # Turn to nparray format
    MaxAmpDta  = np.array(MaxAmpDta,  dtype= float) # turn to nparray format float
    Distolic_M = np.array(Distolic_M, dtype= float) # turn to nparray format
    Distolic_H = np.array(Distolic_H, dtype= float) # turn to nparray format
    Distolic_L = np.array(Distolic_L, dtype= float) # turn to nparray format


    """ AmpValue[0]  ,AmpIndex  ,SystolicValue ,SystolicIndex  ,SystolicAmpValue  ,SystolicCoeff[5]
        ,SystolicValue_H[6] ,SystolicIndex_H  ,SystolicAmpValue_H  ,SystolicCoeff_H[9]
        ,SystolicValue_L[10] ,SystolicIndex_L  ,SystolicAmpValue_L  ,SystolicCoeff_L[13]
    """
    # Horizontal Combine Result
    CombineResult_Horizontal = np.hstack((MaxAmpDta, Distolic_M, Distolic_H, Distolic_L))

    return CombineResult_Horizontal # 回傳數值及位置

"""========== Separate Raw Data -> Amp ============================="""
def SeparateAmp(RawData_List,i): # -> Amp

    # 生成[] list
    Amp_List = []

    # Amp
#    Amp_List.append(RawData_List[i][0]) # Add Title
    Amp_List.append(RawData_List[i][1::2])

    return Amp_List


"""========== Separate Raw Data -> mmHg ============================="""
def SeparateMMhg(RawData_List,i): # mmHg

    # 生成[] list
    mmHg_List = []

    # mmHG
#    mmHg_List.append(RawData_List[i][0]) # Add Title
    mmHg_List.append(RawData_List[i][2::2])

    return mmHg_List

"""========== Systolic Process  ============================="""
def SystolicProcess(SetSystolic, SetCntr, RawData_List, SetDtaGroupStarIndx):

    SystolicArray =np.zeros([SetCntr,14])
    GroupCnt = 0

    for i in range(0,SetCntr,1): #有幾組相同檔位資料，就運算幾次

        # Separate Data to AMP
        AMP = SeparateAmp(RawData_List, i+SetDtaGroupStarIndx)
        mmHg = SeparateMMhg(RawData_List, i+SetDtaGroupStarIndx)

        # List to np array
        ArrayAmp = np.array(*AMP) # 加*  少一個[] 需詳查
        ArrayAmp = list(map(int, ArrayAmp))
        ArrayAmp = np.array(ArrayAmp)

        ArraymmHg = np.array(*mmHg)
        ArraymmHg = list(map(int, ArraymmHg))
        ArraymmHg = np.array(ArraymmHg)

        # Calculate coeff
        SystolicResult = SystolicCoeffProcess(ArrayAmp, ArraymmHg, SetSystolic)

        # Put into array
        SystolicArray[GroupCnt] = SystolicResult

        GroupCnt = GroupCnt+1


    return SystolicArray


"""========== Systolic Process  ============================="""
def DistolicProcess(SetDistolic, SetCntr, RawData_List, SetDtaGroupStarIndx):

    DistolicArray =np.zeros([SetCntr,14])
    GroupCnt = 0

    for i in range(0,SetCntr,1):

        # Separate Data to AMP
        AMP = SeparateAmp(RawData_List, i+SetDtaGroupStarIndx)
        mmHg = SeparateMMhg(RawData_List, i+SetDtaGroupStarIndx)

        # List to np array
        ArrayAmp = np.array(*AMP) # 加*  少一個[] 需詳查
        ArrayAmp = list(map(int, ArrayAmp))
        ArrayAmp = np.array(ArrayAmp)

        ArraymmHg = np.array(*mmHg)
        ArraymmHg = list(map(int, ArraymmHg))
        ArraymmHg = np.array(ArraymmHg)

        # Calculate coeff
        DistolicResult = SystolicCoeffProcess(ArrayAmp, ArraymmHg, SetDistolic)

        # Put into array
        DistolicArray[GroupCnt] = DistolicResult

        GroupCnt = GroupCnt+1


    return DistolicArray



