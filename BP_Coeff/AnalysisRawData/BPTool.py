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



def MaxAmp(AmpArray): # 找最大值，格式須為 numpy array
    
    MaxAmpValue = np.max(AmpArray) 
    MaxAmpIndex = np.argmax(AmpArray)  
#   MaxAmpIndex = AmpArray.index(np.max(AmpArray)) # Using array is List format    
    return MaxAmpValue, MaxAmpIndex  # 回傳最大值


def BP_Coeff(MaxAmp, BpAmp): # 算血壓係數
    Coeff = 1/(MaxAmp / BpAmp)
    Coeff = np.around(Coeff, decimals=2) #小數點第2位後作4捨5入
    return Coeff # 回傳數值及位置


def SystolicDta(AmpArray, mmHgArray, SetFindSystolic, MaxAmpValue): # 找最大值位置，格式須為 numpy array
    
    Systolic_mmHg = ct.FindNearest(mmHgArray,SetFindSystolic)
    Systolic_mmHgValue = Systolic_mmHg[0] 
    Systolic_mmHgIndex = Systolic_mmHg[1]
    
    Systolic_Amp = AmpArray[Systolic_mmHgIndex]    
    Systolic_Coeff = BP_Coeff(MaxAmpValue[0],Systolic_Amp)
#    print(Systolic_mmHgIndex)    
    return Systolic_mmHgValue, Systolic_mmHgIndex, Systolic_Amp, Systolic_Coeff


def SystolicDta_NearWithinFive(AmpArray, mmHgArray, SetSystolic, MaxAmpValue, SetSystolicIndex): # 找最大值位置，格式須為 numpy array
    
    Systolic_mmHg = mmHgArray[SetSystolicIndex]
    
    if np.abs(Systolic_mmHg - SetSystolic) <= 5:
        Systolic = SystolicDta(AmpArray, mmHgArray, Systolic_mmHg, MaxAmpValue)
    else:
        Systolic = np.zeros(4)
        
    return Systolic



def SystolicProcessDta(ArrayAmp, ArraymmHg, SetmmHg):
    
    # tuple format
    MaxAmpDta = MaxAmp(ArrayAmp)
    Systolic_M = SystolicDta(ArrayAmp, ArraymmHg, SetmmHg, MaxAmpDta) 
    
    # 檢查Systolic後一位，是否超出範圍
    if (Systolic_M[1]+1) < len(ArraymmHg):
        Systolic_H = SystolicDta_NearWithinFive(ArrayAmp, ArraymmHg, SetmmHg, MaxAmpDta, Systolic_M[1]+1)
    else:
        Systolic_H = np.zeros(4)
        
    # 檢查Systolic前一位，是否超出範圍        
    if (Systolic_M[1]-1) >= 0:
        Systolic_L = SystolicDta_NearWithinFive(ArrayAmp, ArraymmHg, SetmmHg, MaxAmpDta, Systolic_M[1]-1)
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
    
    return CombineResult_Horizontal # 回傳數值及位置


def DistolicProcessDta(ArrayAmp, ArraymmHg, SetmmHg):
    
    # tuple format
    MaxAmpDta = MaxAmp(ArrayAmp)
    Distolic_M = SystolicDta(ArrayAmp, ArraymmHg, SetmmHg, MaxAmpDta) 
    
    # 檢查Distolic後一位，是否超出範圍
    if (Distolic_M[1]+1) < len(ArraymmHg):
        Distolic_H = SystolicDta_NearWithinFive(ArrayAmp, ArraymmHg, SetmmHg, MaxAmpDta, Distolic_M[1]+1)
    else:
        Distolic_H = np.zeros(4)
        
    # 檢查Distolic前一位，是否超出範圍     
    if (Distolic_M[1]-1) >= 0:
        Distolic_L = SystolicDta_NearWithinFive(ArrayAmp, ArraymmHg, SetmmHg, MaxAmpDta, Distolic_M[1]-1)
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
