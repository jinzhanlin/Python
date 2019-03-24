# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
Created on Sun Feb 24 15:45:38 2019

@author: lin
"""

import sys
import os
import glob
import re
import pandas as pd
import numpy as np
import os.path


"""***************************************************************************
------------------ Statistics ------------------------------------------------
***************************************************************************"""

"""========== Find Data Times in Array  ============================="""
def DataValueCounts(DtaNPArray, SetPrintResult): # 計算元素出現次數

    ValueCnts = pd.value_counts(DtaNPArray)  # 對表格中每个值进行计数并且排序

    if SetPrintResult == True:
        print("\n -----Value Counts，對表格中每個值排序並計數 -----\n", ValueCnts)

    return ValueCnts

"""========== Basic Statistic - Find Max Min Mean SD Var  ============================="""
def BasicStatistic(DtaNPArray, SetPrintResult): # 計算元素出現次數


    MaxValue = np.max(DtaNPArray)

    MinValue = np.min(DtaNPArray)

    Mean = np.mean(DtaNPArray)

    SD = np.std(DtaNPArray) # 标准差

    Var = np.var(DtaNPArray) # Var

    if SetPrintResult == 1: # Print All Result
        print("\n -----Max -----\n", MaxValue)
        print("\n -----Min -----\n", MinValue)
        print("\n -----Mean -----\n", Mean)
        print("\n -----SD  -----\n", SD)
        print("\n -----Var -----\n", Var)

    elif SetPrintResult == 2: # Print Max
        print("\n -----Max -----\n", MaxValue)

    elif SetPrintResult == 3: # Print Min
        print("\n -----Min -----\n", MinValue)

    elif SetPrintResult == 4: # Print Mean
        print("\n -----Mean -----\n", Mean)

    elif SetPrintResult == 5: # Print SD
        print("\n -----SD  -----\n", SD)

    elif SetPrintResult == 6: # Print Var
        print("\n -----Var -----\n", Var)


    return MaxValue, MinValue, Mean, SD, Var

