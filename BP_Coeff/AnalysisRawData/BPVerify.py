# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
Created on Mon Mar 25 09:47:09 2019

@author: yh001360
"""

import os
import glob
import re
import pandas as pd
import numpy as np
import os.path


import sys;
sys.path.append("D:\GitSystem\Python\Common")
import Common as cm
import BPTool as bt

"""***************************************************************************
RealFuzzy

                /\
Systolic      /   \   Distolic
             /     \
            /       \
           /RealFuzzy\

QMS

                /\
Distolic      /   \   Systolic
             /     \
            /       \
           /   QMS   \
***************************************************************************"""



"""========== Get Data in QMS  ============================="""
def GetData(RawData_List, SetDtaGroupStarIndx, SetPrintResult):

    # 取資料
    RawData_Array = RawData_List[SetDtaGroupStarIndx][1:]
    RawData_Array = np.array(RawData_Array) # 加*  少一個[] 需詳查
    RawData_Array = list(map(int, RawData_Array))# 消去一個[] 需詳查

    if SetPrintResult == True:
        print("\n --- 取資料  RawData_List----\n", RawData_List[SetDtaGroupStarIndx][0])
        print("\n --- 取資料  RawData_Array----\n", RawData_Array)

    return RawData_Array

"""========== Closest Coeff AMP in QMS  ============================="""
def ClosestCoeffAMP(DtaNPArray, SetCoeff, SetMode, SetPrintResult):
    F_FindSameValue = 0

    # 找最靠近係數
    Max = bt.MaxAmp(DtaNPArray)
    Target_AMP = int(Max[0] * SetCoeff) # 無條件捨去
    Target_AMP = np.array(Target_AMP) # Turn to np array for np abs

    if SetMode == 1: # Calculate Distolic, Left
        DistolicArray = DtaNPArray[ 0:Max[1] ]
        DistolicArray = DistolicArray[0::2]

        index = (np.abs(DistolicArray - Target_AMP)).argmin()
        index = index*2

    elif SetMode == 0: # Calculate Systolic , Right
        SystolicArray = DtaNPArray[ Max[1]: ]
        SystolicArray = SystolicArray[0::2]

        index = (np.abs(SystolicArray - Target_AMP)).argmin()
        index = index*2

        FrontLen = len(DtaNPArray[ 0:Max[1] ])
        index = index + FrontLen

#    for i in range(0, int(Max[1]/2) ,1): # Max Amp Index /2
#
#        if DtaNPArray[i*2 +1] < DtaNPArray[Max[1]+1]: # Target mmHg < MaxAMP mmHg
#            index = (np.abs(DtaNPArray - Target_AMP)).argmin()


    # Check 是否有相同數值
    SameDistolicAMP = np.where(DtaNPArray == DtaNPArray[index])
    SameDistolicAMPLen = np.size(SameDistolicAMP)

    if SameDistolicAMPLen > 1:
        F_FindSameValue = 1
        print("\n Find Same Value in Distolic ",SameDistolicAMP)

    # 出現相同數值，都最靠近目標值，取最靠近AMP的值
    if F_FindSameValue == 1:
        for i in range(0,SameDistolicAMPLen,1):
            index = (np.abs(SameDistolicAMP[i] - Max[1])).argmin()


    # 找最靠近係數
    Distolic_AMP = DtaNPArray[index]
    Distolic_Pressure = DtaNPArray[index +1]
    RawData_ArrayLen = int(len(DtaNPArray) /2)


    if SetPrintResult == True:
        print("\n --- Max Amp =----\n", Max)
        print("\n --- Max Amp mmHg =----\n", DtaNPArray[Max[1]+1])
        print("\n --- Max Amp * Coeff, Target_AMP =----\n", Target_AMP)

        print("\n --- F_FindSameValue = 1 表示有重複數值 =----\n", F_FindSameValue)
        print("\n --- 最靠近係數 index=----\n", index)

        print("\n --- 最靠近係數AMP =----\n", Distolic_AMP)
        print("\n --- 最靠近係數mmHg =----\n", Distolic_Pressure)
        print("\n --- 陣列長度 =----\n", RawData_ArrayLen)

    return Distolic_AMP, Distolic_Pressure, RawData_ArrayLen, index, Target_AMP


"""========== Calculate Amp Interpolation in QMS  ============================="""
def AmpInterpolation(DtaNPArray, ClosestAMP, SetPrintResult):

    Distolic_AMP        = ClosestAMP[0]
    Distolic_Pressure   = ClosestAMP[1]
    RawData_ArrayLen    = ClosestAMP[2]
    index               = ClosestAMP[3]
    Target_AMP          = ClosestAMP[4]

    Target_AMPmmHg      = DtaNPArray[index+1]


    # 找最靠近係數 的 左右2邊數值

    # Get Left Value
    if index > 0:
        Distolic_AMP_Left = DtaNPArray[(index -2)]
        Distolic_Pressure_Left = DtaNPArray[index -1]
    else:
        Distolic_AMP_Left = 0
        Distolic_Pressure_Left = 0

    # Get Right Value
    if index < RawData_ArrayLen:
        Distolic_AMP_Right = DtaNPArray[(index +2)]
        Distolic_Pressure_Right = DtaNPArray[index +3]
    else:
        Distolic_AMP_Right = 0
        Distolic_Pressure_Right = 0


    # 找最靠近係數 的 左右2邊數值，誰最靠近係數

    # Calculate Left Value
    if Distolic_AMP_Left > 0:
        LeftSub = np.abs(Distolic_AMP_Left - Target_AMP)
        F_Interpolation_Left = 1
    else:
        LeftSub = 0
        F_Interpolation_Left = 0

    # Calculate Right Value
    if Distolic_AMP_Right > 0:
        RightSub = np.abs(Distolic_AMP_Right - Target_AMP)
        F_Interpolation_Right = 1
    else:
        RightSub = 0
        F_Interpolation_Right = 0

    # 作內插
    InterpolationSub =0
    PressureInterpolation =0
    AMPInterpolation =0

    if F_Interpolation_Right == 1 and F_Interpolation_Left == 1:

        if LeftSub < RightSub :
            AMPInterpolation = (Distolic_AMP_Left + Distolic_AMP) /2
            PressureInterpolation = (Distolic_Pressure_Left + Distolic_Pressure) /2

            # Calculate Interpolation
            InterpolationSub = np.abs(AMPInterpolation - Target_AMP)


        elif RightSub < LeftSub :
            AMPInterpolation = (Distolic_AMP_Right + Distolic_AMP) /2
            PressureInterpolation = (Distolic_Pressure_Right + Distolic_Pressure) /2

            # Calculate Interpolation
            InterpolationSub = np.abs(AMPInterpolation - Target_AMP)

        elif RightSub == LeftSub :
            LeftSub_mmHg = np.abs(Distolic_Pressure_Left - Target_AMPmmHg)
            RightSub_mmHg = np.abs(Distolic_Pressure_Right - Target_AMPmmHg)

            if LeftSub_mmHg < RightSub_mmHg:
                AMPInterpolation = (Distolic_AMP_Left + Distolic_AMP) /2
                PressureInterpolation = (Distolic_Pressure_Left + Distolic_Pressure) /2

            else:
                AMPInterpolation = (Distolic_AMP_Right + Distolic_AMP) /2
                PressureInterpolation = (Distolic_Pressure_Right + Distolic_Pressure) /2

            # Calculate Interpolation
            InterpolationSub = np.abs(AMPInterpolation - Target_AMP)



    elif F_Interpolation_Right == 0 and F_Interpolation_Left == 1:
        AMPInterpolation = (Distolic_AMP_Left + Distolic_AMP) /2
        PressureInterpolation = (Distolic_Pressure_Left + Distolic_Pressure) /2

        # Calculate Interpolation
        InterpolationSub = np.abs(AMPInterpolation - Target_AMP)

    elif F_Interpolation_Left == 0 and F_Interpolation_Right ==1:
        AMPInterpolation = (Distolic_AMP_Right + Distolic_AMP) /2
        PressureInterpolation = (Distolic_Pressure_Right + Distolic_Pressure) /2

        # Calculate Interpolation
        InterpolationSub = np.abs(AMPInterpolation - Target_AMP)

    else:
        AMPInterpolation =0
        PressureInterpolation =0



    # 內插數值，誰最靠近係數

    if F_Interpolation_Left == 1 or F_Interpolation_Right == 1:

        # Calculate Right Value
        Distolic_AMPSub = np.abs(Distolic_AMP - Target_AMP)

    elif F_Interpolation_Left == 0 and F_Interpolation_Right == 0:
        InterpolationSub = 0
        Distolic_AMPSub = np.abs(Distolic_AMP - Target_AMP)



    if Distolic_AMPSub < InterpolationSub:
        Distolic = Distolic_Pressure
    else:
        Distolic = PressureInterpolation



    if SetPrintResult == True:
        print("\n --- Distolic  = ----\n", Distolic)

        print("\n --- Distolic_AMP_Left  = ----\n", Distolic_AMP_Left)
        print("\n --- Distolic_Pressure_Left  = ----\n", Distolic_Pressure_Left)
        print("\n --- Distolic_AMP_Right  = ----\n", Distolic_AMP_Right)
        print("\n --- Distolic_Pressure_Right  = ----\n", Distolic_Pressure_Right)

        print("\n --- AMP Interpolation  = ----\n", AMPInterpolation)
        print("\n --- Pressure Interpolation  = ----\n", PressureInterpolation)

    return Distolic

"""========== Calculate Systolic or Distolic in QMS  ============================="""
def QMS_CalcuBPM(RawData_List, SetCntr, SetCoeff, SetDtaGroupStarIndx, SetMode, SetPrintResult): # Calculate Systolic Blood Pressure，格式須為 numpy array

    # 生成[] list
    Distolic = []

    if SetCntr == 0:
        SetCntr = 1

    for i in range(0,SetCntr,1):
        # 取資料
        RawData_Array = GetData(RawData_List, i+ SetDtaGroupStarIndx, False) # True False

        # 找最靠近係數
        ClosestAMP = ClosestCoeffAMP(RawData_Array, SetCoeff, SetMode, False)

        # 取找最靠近係數 的 左右2邊數值
        DistolicVal = AmpInterpolation(RawData_Array, ClosestAMP, False)
        Distolic.append(DistolicVal)


    if SetPrintResult == True:
        print("\n ---Distolic = ---\n", Distolic)


    return Distolic

"""========== Calculate Systolic or Distolic in QMS  ============================="""
def QMS_VerifyBPM(RawData_List, SetCntr, SetCoeffM, SetCoeffH, SetCoeffL, SetDtaGroupStarIndx, SetMode, SetPrintResult): # Calculate Systolic Blood Pressure，格式須為 numpy array

    # 生成[] list
    Result = []

    # For Debug
    SeparateResult = []
    SetCalcuBPMCntr = 0

    for i in range(0,SetCntr,1):

        ResultM = QMS_CalcuBPM(RawData_List, SetCalcuBPMCntr, SetCoeffM, i +SetDtaGroupStarIndx, SetMode, False)
        ResultH = QMS_CalcuBPM(RawData_List, SetCalcuBPMCntr, SetCoeffH, i +SetDtaGroupStarIndx, SetMode, False)
        ResultL = QMS_CalcuBPM(RawData_List, SetCalcuBPMCntr, SetCoeffL, i +SetDtaGroupStarIndx, SetMode, False)

        ResultM = np.array(ResultM)
        ResultH = np.array(ResultH)
        ResultL = np.array(ResultL)


        ResultAvg = int( (ResultM + ResultH + ResultL) /3)
        Result.append(ResultAvg)

        # For Debug
        CombineResult = np.hstack((ResultM, ResultH, ResultL))
        CombineResult = CombineResult.tolist()
        SeparateResult.append(CombineResult)

    if SetPrintResult == True:
        print("\n ---BPM Result = ---\n", Result)
        print("\n ---BPM  Separate Result = ---\n", SeparateResult)


    return Result































