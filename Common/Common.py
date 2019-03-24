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


"""========== Find Nearrest Value， 找陣列中最靠近輸入數值的值============================="""  
def FindNearest(array, value): # 找陣列中最靠近輸入數值的值    
    index = (np.abs(array-value)).argmin()
    
    return array[index], index # 回傳數值及位置

"""========== Get File Path  ============================="""  
def GetFilePath():  
    try:
       FilePath = sys.argv[1] # 取得從 Command Line 輸入的TXT所在的資料夾路徑
    except:
       FilePath = os.getcwd() # 取得Script當前目錄
    return FilePath

