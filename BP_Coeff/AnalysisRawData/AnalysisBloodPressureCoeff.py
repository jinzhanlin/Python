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
SaveResult = True # True False


InputPath = ct.GetFilePath()
    
    
"""========== Get Txt File Data  ============================="""    
GetFilePath_List = []   # 定义一个列表，用来存放txt文件名
GetAllFileDta_List = []  


b=np.array([])

""" 將 InputPath 路徑下 所有txt開啟並讀取 """
for InputFile in glob.glob(os.path.join(InputPath, '*.txt')):
        GetFilePath_List.append(InputFile)
        GetFileName = os.path.basename(InputFile) 
        GetFileData = pd.read_csv(r''+InputFile) # 原始為單斜線須為双斜線才行，或加上r后变为原始字符串
        #print(GetFileData)

        
        """ 依照txt檔名，存入個別變數  """
        if GetFileName == '01_AMP_Reg_60_30_80_S1.txt':
            with open(InputFile, 'r', newline = '') as filereader: 
                DtaFram_01_AMP_Reg_60_30_80_S1 = pd.read_csv(filereader) # Get Data and ignore first index and PutIn DataFrame format
                DataArray = np.array(DtaFram_01_AMP_Reg_60_30_80_S1) # DataFrame format PutIn to Array format for turn to Value
                Dta_01_AMP_Reg_60_30_80_S1 = list(map(int, DataArray)) # String to Value and PutIn List format
                Dta_01_AMP_Reg_60_30_80_S1 = np.array(Dta_01_AMP_Reg_60_30_80_S1) # List turn to Array 
                
#                GetArrayLength = len(Dta_01_AMP_Reg_60_30_80_S1)
                DtaAmp_01_AMP_Reg_60_30_80_S1 = Dta_01_AMP_Reg_60_30_80_S1[0::2] # Divide Amp
                DtaMMHg_01_AMP_Reg_60_30_80_S1 = Dta_01_AMP_Reg_60_30_80_S1[1::2] # Divide mmHg

#                print("Max Amp Index\n",np.where( DtaAmp_01_AMP_Reg_60_30_80_S1 == np.max(DtaAmp_01_AMP_Reg_60_30_80_S1) ))
#                print("Reg\n",Dta_01_AMP_Reg_60_30_80_S1) 
#                print("\nAMP\n",DtaAmp_01_AMP_Reg_60_30_80_S1)
#                print("\nmmHg\n",DtaMMHg_01_AMP_Reg_60_30_80_S1)
   
    
        elif GetFileName == '02_AMP_Reg_60_30_80_S2.txt':
            with open(InputFile, 'r', newline = '') as filereader: 
                ReadFile_DtaFram = pd.read_csv(filereader) # Get Data and PutIn DataFrame format
                DataArray = np.array(ReadFile_DtaFram) # DataFrame format turn to Array format
                DtaArray = list(map(int, DataArray)) # list, String to Value
                DtaArray = np.array(DtaArray) # List turn to Array 
                
                DtaAmp_02_AMP_Reg_60_30_80_S2 = DtaArray[0::2] # Divide Amp
                DtaMMHg_02_AMP_Reg_60_30_80_S2 = DtaArray[1::2] # Divide mmHg
   
    
        elif GetFileName == '03_AMP_Reg_60_30_80_S3.txt':
            with open(InputFile, 'r', newline = '') as filereader: 
                ReadFile_DtaFram = pd.read_csv(filereader) # Get Data and PutIn DataFrame format
                DataArray = np.array(ReadFile_DtaFram) # DataFrame format turn to Array format
                DtaArray = list(map(int, DataArray)) # list, String to Value
                DtaArray = np.array(DtaArray) # List turn to Array 
                
                DtaAmp_03_AMP_Reg_60_30_80_S3 = DtaArray[0::2] # Divide Amp
                DtaMMHg_03_AMP_Reg_60_30_80_S3 = DtaArray[1::2] # Divide mmHg
                
                
        elif GetFileName == '04_AMP_Reg_60_30_80_S4.txt':
            with open(InputFile, 'r', newline = '') as filereader: 
                ReadFile_DtaFram = pd.read_csv(filereader) # Get Data and PutIn DataFrame format
                DataArray = np.array(ReadFile_DtaFram) # DataFrame format turn to Array format
                DtaArray = list(map(int, DataArray)) # list, String to Value
                DtaArray = np.array(DtaArray) # List turn to Array 
                
                DtaAmp_04_AMP_Reg_60_30_80_S4 = DtaArray[0::2] # Divide Amp
                DtaMMHg_04_AMP_Reg_60_30_80_S4 = DtaArray[1::2] # Divide mmHg
   
    
        elif GetFileName == '05_AMP_Reg_60_30_80_S5.txt':
            with open(InputFile, 'r', newline = '') as filereader: 
                ReadFile_DtaFram = pd.read_csv(filereader) # Get Data and PutIn DataFrame format
                DataArray = np.array(ReadFile_DtaFram) # DataFrame format turn to Array format
                DtaArray = list(map(int, DataArray)) # list, String to Value
                DtaArray = np.array(DtaArray) # List turn to Array 
                
                DtaAmp_05_AMP_Reg_60_30_80_S5 = DtaArray[0::2] # Divide Amp
                DtaMMHg_05_AMP_Reg_60_30_80_S5 = DtaArray[1::2] # Divide mmHg
                
        elif GetFileName == '06_AMP_Reg_80_50_80_S1.txt':
            with open(InputFile, 'r', newline = '') as filereader: 
                ReadFile_DtaFram = pd.read_csv(filereader) # Get Data and PutIn DataFrame format
                DataArray = np.array(ReadFile_DtaFram) # DataFrame format turn to Array format
                DtaArray = list(map(int, DataArray)) # list, String to Value
                DtaArray = np.array(DtaArray) # List turn to Array 
                
                DtaAmp_06_AMP_Reg_80_50_80_S1 = DtaArray[0::2] # Divide Amp
                DtaMMHg_06_AMP_Reg_80_50_80_S1 = DtaArray[1::2] # Divide mmHg
   
    
        elif GetFileName == '07_AMP_Reg_80_50_80_S2.txt':
            with open(InputFile, 'r', newline = '') as filereader: 
                ReadFile_DtaFram = pd.read_csv(filereader) # Get Data and PutIn DataFrame format
                DataArray = np.array(ReadFile_DtaFram) # DataFrame format turn to Array format
                DtaArray = list(map(int, DataArray)) # list, String to Value
                DtaArray = np.array(DtaArray) # List turn to Array 
                
                DtaAmp_07_AMP_Reg_80_50_80_S2 = DtaArray[0::2] # Divide Amp
                DtaMMHg_07_AMP_Reg_80_50_80_S2 = DtaArray[1::2] # Divide mmHg
                
                
        elif GetFileName == '08_AMP_Reg_80_50_80_S3.txt':
            with open(InputFile, 'r', newline = '') as filereader: 
                ReadFile_DtaFram = pd.read_csv(filereader) # Get Data and PutIn DataFrame format
                DataArray = np.array(ReadFile_DtaFram) # DataFrame format turn to Array format
                DtaArray = list(map(int, DataArray)) # list, String to Value
                DtaArray = np.array(DtaArray) # List turn to Array 
                
                DtaAmp_08_AMP_Reg_80_50_80_S3 = DtaArray[0::2] # Divide Amp
                DtaMMHg_08_AMP_Reg_80_50_80_S3 = DtaArray[1::2] # Divide mmHg
   
    
        elif GetFileName == '09_AMP_Reg_80_50_80_S4.txt':
            with open(InputFile, 'r', newline = '') as filereader: 
                ReadFile_DtaFram = pd.read_csv(filereader) # Get Data and PutIn DataFrame format
                DataArray = np.array(ReadFile_DtaFram) # DataFrame format turn to Array format
                DtaArray = list(map(int, DataArray)) # list, String to Value
                DtaArray = np.array(DtaArray) # List turn to Array 
                
                DtaAmp_09_AMP_Reg_80_50_80_S4 = DtaArray[0::2] # Divide Amp
                DtaMMHg_09_AMP_Reg_80_50_80_S4 = DtaArray[1::2] # Divide mmHg
                
                
        elif GetFileName == '10_AMP_Reg_80_50_80_S5.txt':
            with open(InputFile, 'r', newline = '') as filereader: 
                ReadFile_DtaFram = pd.read_csv(filereader) # Get Data and PutIn DataFrame format
                DataArray = np.array(ReadFile_DtaFram) # DataFrame format turn to Array format
                DtaArray = list(map(int, DataArray)) # list, String to Value
                DtaArray = np.array(DtaArray) # List turn to Array 
                
                DtaAmp_10_AMP_Reg_80_50_80_S5 = DtaArray[0::2] # Divide Amp
                DtaMMHg_10_AMP_Reg_80_50_80_S5 = DtaArray[1::2] # Divide mmHg
                
        elif GetFileName == '11_AMP_Reg_100_65_80_S1.txt':
            with open(InputFile, 'r', newline = '') as filereader: 
                ReadFile_DtaFram = pd.read_csv(filereader) # Get Data and PutIn DataFrame format
                DataArray = np.array(ReadFile_DtaFram) # DataFrame format turn to Array format
                DtaArray = list(map(int, DataArray)) # list, String to Value
                DtaArray = np.array(DtaArray) # List turn to Array 
                
                DtaAmp_11_AMP_Reg_100_65_80_S1 = DtaArray[0::2] # Divide Amp
                DtaMMHg_11_AMP_Reg_100_65_80_S1 = DtaArray[1::2] # Divide mmHg
   
    
        elif GetFileName == '12_AMP_Reg_100_65_80_S2.txt':
            with open(InputFile, 'r', newline = '') as filereader: 
                ReadFile_DtaFram = pd.read_csv(filereader) # Get Data and PutIn DataFrame format
                DataArray = np.array(ReadFile_DtaFram) # DataFrame format turn to Array format
                DtaArray = list(map(int, DataArray)) # list, String to Value
                DtaArray = np.array(DtaArray) # List turn to Array 
                
                DtaAmp_12_AMP_Reg_100_65_80_S2 = DtaArray[0::2] # Divide Amp
                DtaMMHg_12_AMP_Reg_100_65_80_S2 = DtaArray[1::2] # Divide mmHg
                
                
        elif GetFileName == '13_AMP_Reg_100_65_80_S3.txt':
            with open(InputFile, 'r', newline = '') as filereader: 
                ReadFile_DtaFram = pd.read_csv(filereader) # Get Data and PutIn DataFrame format
                DataArray = np.array(ReadFile_DtaFram) # DataFrame format turn to Array format
                DtaArray = list(map(int, DataArray)) # list, String to Value
                DtaArray = np.array(DtaArray) # List turn to Array 
                
                DtaAmp_13_AMP_Reg_100_65_80_S3 = DtaArray[0::2] # Divide Amp
                DtaMMHg_13_AMP_Reg_100_65_80_S3 = DtaArray[1::2] # Divide mmHg
   
    
        elif GetFileName == '14_AMP_Reg_100_65_80_S4.txt':
            with open(InputFile, 'r', newline = '') as filereader: 
                ReadFile_DtaFram = pd.read_csv(filereader) # Get Data and PutIn DataFrame format
                DataArray = np.array(ReadFile_DtaFram) # DataFrame format turn to Array format
                DtaArray = list(map(int, DataArray)) # list, String to Value
                DtaArray = np.array(DtaArray) # List turn to Array 
                
                DtaAmp_14_AMP_Reg_100_65_80_S4 = DtaArray[0::2] # Divide Amp
                DtaMMHg_14_AMP_Reg_100_65_80_S4 = DtaArray[1::2] # Divide mmHg
                
                
        elif GetFileName == '15_AMP_Reg_100_65_80_S5.txt':
            with open(InputFile, 'r', newline = '') as filereader: 
                ReadFile_DtaFram = pd.read_csv(filereader) # Get Data and PutIn DataFrame format
                DataArray = np.array(ReadFile_DtaFram) # DataFrame format turn to Array format
                DtaArray = list(map(int, DataArray)) # list, String to Value
                DtaArray = np.array(DtaArray) # List turn to Array 
                
                DtaAmp_15_AMP_Reg_100_65_80_S5 = DtaArray[0::2] # Divide Amp
                DtaMMHg_15_AMP_Reg_100_65_80_S5 = DtaArray[1::2] # Divide mmHg
                
        elif GetFileName == '16_AMP_Reg_120_80_80_S1.txt':
            with open(InputFile, 'r', newline = '') as filereader: 
                ReadFile_DtaFram = pd.read_csv(filereader) # Get Data and PutIn DataFrame format
                DataArray = np.array(ReadFile_DtaFram) # DataFrame format turn to Array format
                DtaArray = list(map(int, DataArray)) # list, String to Value
                DtaArray = np.array(DtaArray) # List turn to Array 
                
                DtaAmp_16_AMP_Reg_120_80_80_S1 = DtaArray[0::2] # Divide Amp
                DtaMMHg_16_AMP_Reg_120_80_80_S1 = DtaArray[1::2] # Divide mmHg
   
    
        elif GetFileName == '17_AMP_Reg_120_80_80_S2.txt':
            with open(InputFile, 'r', newline = '') as filereader: 
                ReadFile_DtaFram = pd.read_csv(filereader) # Get Data and PutIn DataFrame format
                DataArray = np.array(ReadFile_DtaFram) # DataFrame format turn to Array format
                DtaArray = list(map(int, DataArray)) # list, String to Value
                DtaArray = np.array(DtaArray) # List turn to Array 
                
                DtaAmp_17_AMP_Reg_120_80_80_S2 = DtaArray[0::2] # Divide Amp
                DtaMMHg_17_AMP_Reg_120_80_80_S2 = DtaArray[1::2] # Divide mmHg
                
                
        elif GetFileName == '18_AMP_Reg_120_80_80_S3.txt':
            with open(InputFile, 'r', newline = '') as filereader: 
                ReadFile_DtaFram = pd.read_csv(filereader) # Get Data and PutIn DataFrame format
                DataArray = np.array(ReadFile_DtaFram) # DataFrame format turn to Array format
                DtaArray = list(map(int, DataArray)) # list, String to Value
                DtaArray = np.array(DtaArray) # List turn to Array 
                
                DtaAmp_18_AMP_Reg_120_80_80_S3 = DtaArray[0::2] # Divide Amp
                DtaMMHg_18_AMP_Reg_120_80_80_S3 = DtaArray[1::2] # Divide mmHg
   
    
        elif GetFileName == '19_AMP_Reg_120_80_80_S4.txt':
            with open(InputFile, 'r', newline = '') as filereader: 
                ReadFile_DtaFram = pd.read_csv(filereader) # Get Data and PutIn DataFrame format
                DataArray = np.array(ReadFile_DtaFram) # DataFrame format turn to Array format
                DtaArray = list(map(int, DataArray)) # list, String to Value
                DtaArray = np.array(DtaArray) # List turn to Array 
                
                DtaAmp_19_AMP_Reg_120_80_80_S4 = DtaArray[0::2] # Divide Amp
                DtaMMHg_19_AMP_Reg_120_80_80_S4 = DtaArray[1::2] # Divide mmHg
                
                
        elif GetFileName == '20_AMP_Reg_120_80_80_S5.txt':
            with open(InputFile, 'r', newline = '') as filereader: 
                ReadFile_DtaFram = pd.read_csv(filereader) # Get Data and PutIn DataFrame format
                DataArray = np.array(ReadFile_DtaFram) # DataFrame format turn to Array format
                DtaArray = list(map(int, DataArray)) # list, String to Value
                DtaArray = np.array(DtaArray) # List turn to Array 
                
                DtaAmp_20_AMP_Reg_120_80_80_S5 = DtaArray[0::2] # Divide Amp
                DtaMMHg_20_AMP_Reg_120_80_80_S5 = DtaArray[1::2] # Divide mmHg
                
        elif GetFileName == '21_AMP_Reg_150_100_80_S1.txt':
            with open(InputFile, 'r', newline = '') as filereader: 
                ReadFile_DtaFram = pd.read_csv(filereader) # Get Data and PutIn DataFrame format
                DataArray = np.array(ReadFile_DtaFram) # DataFrame format turn to Array format
                DtaArray = list(map(int, DataArray)) # list, String to Value
                DtaArray = np.array(DtaArray) # List turn to Array 
                
                DtaAmp_21_AMP_Reg_100_65_80_S1 = DtaArray[0::2] # Divide Amp
                DtaMMHg_21_AMP_Reg_100_65_80_S1 = DtaArray[1::2] # Divide mmHg
   
    
        elif GetFileName == '22_AMP_Reg_150_100_80_S2.txt':
            with open(InputFile, 'r', newline = '') as filereader: 
                ReadFile_DtaFram = pd.read_csv(filereader) # Get Data and PutIn DataFrame format
                DataArray = np.array(ReadFile_DtaFram) # DataFrame format turn to Array format
                DtaArray = list(map(int, DataArray)) # list, String to Value
                DtaArray = np.array(DtaArray) # List turn to Array 
                
                DtaAmp_22_AMP_Reg_150_100_80_S2 = DtaArray[0::2] # Divide Amp
                DtaMMHg_22_AMP_Reg_150_100_80_S2 = DtaArray[1::2] # Divide mmHg
                
                
        elif GetFileName == '23_AMP_Reg_150_100_80_S3.txt':
            with open(InputFile, 'r', newline = '') as filereader: 
                ReadFile_DtaFram = pd.read_csv(filereader) # Get Data and PutIn DataFrame format
                DataArray = np.array(ReadFile_DtaFram) # DataFrame format turn to Array format
                DtaArray = list(map(int, DataArray)) # list, String to Value
                DtaArray = np.array(DtaArray) # List turn to Array 
                
                DtaAmp_23_AMP_Reg_150_100_80_S3 = DtaArray[0::2] # Divide Amp
                DtaMMHg_23_AMP_Reg_150_100_80_S3 = DtaArray[1::2] # Divide mmHg
   
    
        elif GetFileName == '24_AMP_Reg_150_100_80_S4.txt':
            with open(InputFile, 'r', newline = '') as filereader: 
                ReadFile_DtaFram = pd.read_csv(filereader) # Get Data and PutIn DataFrame format
                DataArray = np.array(ReadFile_DtaFram) # DataFrame format turn to Array format
                DtaArray = list(map(int, DataArray)) # list, String to Value
                DtaArray = np.array(DtaArray) # List turn to Array 
                
                DtaAmp_24_AMP_Reg_150_100_80_S4 = DtaArray[0::2] # Divide Amp
                DtaMMHg_24_AMP_Reg_150_100_80_S4 = DtaArray[1::2] # Divide mmHg
                
                
        elif GetFileName == '25_AMP_Reg_150_100_80_S5.txt':
            with open(InputFile, 'r', newline = '') as filereader: 
                ReadFile_DtaFram = pd.read_csv(filereader) # Get Data and PutIn DataFrame format
                DataArray = np.array(ReadFile_DtaFram) # DataFrame format turn to Array format
                DtaArray = list(map(int, DataArray)) # list, String to Value
                DtaArray = np.array(DtaArray) # List turn to Array 
                
                DtaAmp_25_AMP_Reg_150_100_80_S5 = DtaArray[0::2] # Divide Amp
                DtaMMHg_25_AMP_Reg_150_100_80_S5 = DtaArray[1::2] # Divide mmHg
    
    
        elif GetFileName == '26_AMP_Reg_200_150_80_S1.txt':
            with open(InputFile, 'r', newline = '') as filereader: 
                ReadFile_DtaFram = pd.read_csv(filereader) # Get Data and PutIn DataFrame format
                DataArray = np.array(ReadFile_DtaFram) # DataFrame format turn to Array format
                DtaArray = list(map(int, DataArray)) # list, String to Value
                DtaArray = np.array(DtaArray) # List turn to Array 
                
                DtaAmp_26_AMP_Reg_200_150_80_S1 = DtaArray[0::2] # Divide Amp
                DtaMMHg_26_AMP_Reg_200_150_80_S1 = DtaArray[1::2] # Divide mmHg
                
                
        elif GetFileName == '27_AMP_Reg_200_150_80_S2.txt':
            with open(InputFile, 'r', newline = '') as filereader: 
                ReadFile_DtaFram = pd.read_csv(filereader) # Get Data and PutIn DataFrame format
                DataArray = np.array(ReadFile_DtaFram) # DataFrame format turn to Array format
                DtaArray = list(map(int, DataArray)) # list, String to Value
                DtaArray = np.array(DtaArray) # List turn to Array 
                
                DtaAmp_27_AMP_Reg_200_150_80_S2 = DtaArray[0::2] # Divide Amp
                DtaMMHg_27_AMP_Reg_200_150_80_S2 = DtaArray[1::2] # Divide mmHg
                
                
        elif GetFileName == '28_AMP_Reg_200_150_80_S3.txt':
            with open(InputFile, 'r', newline = '') as filereader: 
                ReadFile_DtaFram = pd.read_csv(filereader) # Get Data and PutIn DataFrame format
                DataArray = np.array(ReadFile_DtaFram) # DataFrame format turn to Array format
                DtaArray = list(map(int, DataArray)) # list, String to Value
                DtaArray = np.array(DtaArray) # List turn to Array 
                
                DtaAmp_28_AMP_Reg_200_150_80_S3 = DtaArray[0::2] # Divide Amp
                DtaMMHg_28_AMP_Reg_200_150_80_S3 = DtaArray[1::2] # Divide mmHg
                
        elif GetFileName == '29_AMP_Reg_200_150_80_S4.txt':
            with open(InputFile, 'r', newline = '') as filereader: 
                ReadFile_DtaFram = pd.read_csv(filereader) # Get Data and PutIn DataFrame format
                DataArray = np.array(ReadFile_DtaFram) # DataFrame format turn to Array format
                DtaArray = list(map(int, DataArray)) # list, String to Value
                DtaArray = np.array(DtaArray) # List turn to Array 
                
                DtaAmp_29_AMP_Reg_200_150_80_S4 = DtaArray[0::2] # Divide Amp
                DtaMMHg_29_AMP_Reg_200_150_80_S4 = DtaArray[1::2] # Divide mmHg
   
    
        elif GetFileName == '30_AMP_Reg_200_150_80_S5.txt':
            with open(InputFile, 'r', newline = '') as filereader: 
                ReadFile_DtaFram = pd.read_csv(filereader) # Get Data and PutIn DataFrame format
                DataArray = np.array(ReadFile_DtaFram) # DataFrame format turn to Array format
                DtaArray = list(map(int, DataArray)) # list, String to Value
                DtaArray = np.array(DtaArray) # List turn to Array 
                
                DtaAmp_30_AMP_Reg_200_150_80_S5 = DtaArray[0::2] # Divide Amp
                DtaMMHg_30_AMP_Reg_200_150_80_S5 = DtaArray[1::2] # Divide mmHg
                
                
        elif GetFileName == '31_AMP_Reg_255_195_80_S1.txt':
            with open(InputFile, 'r', newline = '') as filereader: 
                ReadFile_DtaFram = pd.read_csv(filereader) # Get Data and PutIn DataFrame format
                DataArray = np.array(ReadFile_DtaFram) # DataFrame format turn to Array format
                DtaArray = list(map(int, DataArray)) # list, String to Value
                DtaArray = np.array(DtaArray) # List turn to Array 
                
                DtaAmp_31_AMP_Reg_255_195_80_S1 = DtaArray[0::2] # Divide Amp
                DtaMMHg_31_AMP_Reg_255_195_80_S1 = DtaArray[1::2] # Divide mmHg
   
    
        elif GetFileName == '32_AMP_Reg_255_195_80_S2.txt':
            with open(InputFile, 'r', newline = '') as filereader: 
                ReadFile_DtaFram = pd.read_csv(filereader) # Get Data and PutIn DataFrame format
                DataArray = np.array(ReadFile_DtaFram) # DataFrame format turn to Array format
                DtaArray = list(map(int, DataArray)) # list, String to Value
                DtaArray = np.array(DtaArray) # List turn to Array 
                
                DtaAmp_32_AMP_Reg_255_195_80_S2 = DtaArray[0::2] # Divide Amp
                DtaMMHg_32_AMP_Reg_255_195_80_S2 = DtaArray[1::2] # Divide mmHg
                
                
        elif GetFileName == '33_AMP_Reg_255_195_80_S3.txt':
            with open(InputFile, 'r', newline = '') as filereader: 
                ReadFile_DtaFram = pd.read_csv(filereader) # Get Data and PutIn DataFrame format
                DataArray = np.array(ReadFile_DtaFram) # DataFrame format turn to Array format
                DtaArray = list(map(int, DataArray)) # list, String to Value
                DtaArray = np.array(DtaArray) # List turn to Array 
                
                DtaAmp_33_AMP_Reg_255_195_80_S3 = DtaArray[0::2] # Divide Amp
                DtaMMHg_33_AMP_Reg_255_195_80_S3 = DtaArray[1::2] # Divide mmHg
    
    
        elif GetFileName == '34_AMP_Reg_255_195_80_S4.txt':
            with open(InputFile, 'r', newline = '') as filereader: 
                ReadFile_DtaFram = pd.read_csv(filereader) # Get Data and PutIn DataFrame format
                DataArray = np.array(ReadFile_DtaFram) # DataFrame format turn to Array format
                DtaArray = list(map(int, DataArray)) # list, String to Value
                DtaArray = np.array(DtaArray) # List turn to Array 
                
                DtaAmp_34_AMP_Reg_255_195_80_S4 = DtaArray[0::2] # Divide Amp
                DtaMMHg_34_AMP_Reg_255_195_80_S4 = DtaArray[1::2] # Divide mmHg     
                
                
        elif GetFileName == '35_AMP_Reg_255_195_80_S5.txt':
            with open(InputFile, 'r', newline = '') as filereader: 
                ReadFile_DtaFram = pd.read_csv(filereader) # Get Data and PutIn DataFrame format
                DataArray = np.array(ReadFile_DtaFram) # DataFrame format turn to Array format
                DtaArray = list(map(int, DataArray)) # list, String to Value
                DtaArray = np.array(DtaArray) # List turn to Array 
                
                DtaAmp_35_AMP_Reg_255_195_80_S5 = DtaArray[0::2] # Divide Amp
                DtaMMHg_35_AMP_Reg_255_195_80_S5 = DtaArray[1::2] # Divide mmHg           
                

                    
        """Get All File Data"""    
        with open(InputFile, 'r', newline = '') as filereader:           
            for row in filereader:   
                 #line = line.strip().split()
                row = row.strip()
                GetAllFileDta_List.append(row.split(','))
                #print(GetAllTxtFileList)
                
 
"""========== Process Txt File Data  ============================="""                 
#print(type(DtaAmp_01_AMP_Reg_60_30_80_S1)) # 查變數格式
#BP_60_30_80 = np.zeros(11).reshape(1,11)

"""=================================  60 / 30 / 80  ============================"""
SetSystolic = 60
SetDistolic = 30


ArrayAmp = DtaAmp_01_AMP_Reg_60_30_80_S1
ArraymmHg = DtaMMHg_01_AMP_Reg_60_30_80_S1

SystolicResult1 = SystolicProcessDta(ArrayAmp, ArraymmHg, SetSystolic)
DistolicResult1 = DistolicProcessDta(ArrayAmp, ArraymmHg, SetDistolic)


ArrayAmp = DtaAmp_02_AMP_Reg_60_30_80_S2
ArraymmHg = DtaMMHg_02_AMP_Reg_60_30_80_S2

SystolicResult2 = SystolicProcessDta(ArrayAmp, ArraymmHg, SetSystolic)
DistolicResult2 = DistolicProcessDta(ArrayAmp, ArraymmHg, SetDistolic)

ArrayAmp = DtaAmp_03_AMP_Reg_60_30_80_S3
ArraymmHg = DtaMMHg_03_AMP_Reg_60_30_80_S3

SystolicResult3 = SystolicProcessDta(ArrayAmp, ArraymmHg, SetSystolic)
DistolicResult3 = DistolicProcessDta(ArrayAmp, ArraymmHg, SetDistolic)

ArrayAmp = DtaAmp_04_AMP_Reg_60_30_80_S4
ArraymmHg = DtaMMHg_04_AMP_Reg_60_30_80_S4

SystolicResult4 = SystolicProcessDta(ArrayAmp, ArraymmHg, SetSystolic)
DistolicResult4 = DistolicProcessDta(ArrayAmp, ArraymmHg, SetDistolic)

ArrayAmp = DtaAmp_05_AMP_Reg_60_30_80_S5
ArraymmHg = DtaMMHg_05_AMP_Reg_60_30_80_S5

SystolicResult5 = SystolicProcessDta(ArrayAmp, ArraymmHg, SetSystolic)
DistolicResult5 = DistolicProcessDta(ArrayAmp, ArraymmHg, SetDistolic)


# Vertical Combine Result    
Systolic_60_30_80_CombineResultVertical = np.vstack((SystolicResult1, SystolicResult2, SystolicResult3, SystolicResult4, SystolicResult5))    # vertical stack
Distolic_60_30_80_CombineResultVertical = np.vstack((DistolicResult1, DistolicResult2, DistolicResult3, DistolicResult4, DistolicResult5))    # vertical stack
#print(Systolic_60_30_80_CombineResultVertical)    






"""================================================ 80 / 50 / 80  ==========================="""
SetSystolic = 80
SetDistolic = 50


ArrayAmp = DtaAmp_06_AMP_Reg_80_50_80_S1
ArraymmHg = DtaMMHg_06_AMP_Reg_80_50_80_S1

SystolicResult1 = SystolicProcessDta(ArrayAmp, ArraymmHg, SetSystolic)
DistolicResult1 = DistolicProcessDta(ArrayAmp, ArraymmHg, SetDistolic)


ArrayAmp = DtaAmp_07_AMP_Reg_80_50_80_S2
ArraymmHg = DtaMMHg_07_AMP_Reg_80_50_80_S2

SystolicResult2 = SystolicProcessDta(ArrayAmp, ArraymmHg, SetSystolic)
DistolicResult2 = DistolicProcessDta(ArrayAmp, ArraymmHg, SetDistolic)

ArrayAmp = DtaAmp_08_AMP_Reg_80_50_80_S3
ArraymmHg = DtaMMHg_08_AMP_Reg_80_50_80_S3

SystolicResult3 = SystolicProcessDta(ArrayAmp, ArraymmHg, SetSystolic)
DistolicResult3 = DistolicProcessDta(ArrayAmp, ArraymmHg, SetDistolic)

ArrayAmp = DtaAmp_09_AMP_Reg_80_50_80_S4
ArraymmHg = DtaMMHg_09_AMP_Reg_80_50_80_S4

SystolicResult4 = SystolicProcessDta(ArrayAmp, ArraymmHg, SetSystolic)
DistolicResult4 = DistolicProcessDta(ArrayAmp, ArraymmHg, SetDistolic)

ArrayAmp = DtaAmp_10_AMP_Reg_80_50_80_S5
ArraymmHg = DtaMMHg_10_AMP_Reg_80_50_80_S5

SystolicResult5 = SystolicProcessDta(ArrayAmp, ArraymmHg, SetSystolic)
DistolicResult5 = DistolicProcessDta(ArrayAmp, ArraymmHg, SetDistolic)


# Vertical Combine Result    
Systolic_80_50_80_CombineResultVertical = np.vstack((SystolicResult1, SystolicResult2, SystolicResult3, SystolicResult4, SystolicResult5))    # vertical stack
Distolic_80_50_80_CombineResultVertical = np.vstack((DistolicResult1, DistolicResult2, DistolicResult3, DistolicResult4, DistolicResult5))    # vertical stack
#print(Systolic_80_50_80_CombineResultVertical)    

"""================================================ 100 / 65 / 80  ==========================="""
SetSystolic = 100
SetDistolic = 65


ArrayAmp = DtaAmp_11_AMP_Reg_100_65_80_S1
ArraymmHg = DtaMMHg_11_AMP_Reg_100_65_80_S1

SystolicResult1 = SystolicProcessDta(ArrayAmp, ArraymmHg, SetSystolic)
DistolicResult1 = DistolicProcessDta(ArrayAmp, ArraymmHg, SetDistolic)


ArrayAmp = DtaAmp_12_AMP_Reg_100_65_80_S2
ArraymmHg = DtaMMHg_12_AMP_Reg_100_65_80_S2

SystolicResult2 = SystolicProcessDta(ArrayAmp, ArraymmHg, SetSystolic)
DistolicResult2 = DistolicProcessDta(ArrayAmp, ArraymmHg, SetDistolic)

ArrayAmp = DtaAmp_13_AMP_Reg_100_65_80_S3
ArraymmHg = DtaMMHg_13_AMP_Reg_100_65_80_S3

SystolicResult3 = SystolicProcessDta(ArrayAmp, ArraymmHg, SetSystolic)
DistolicResult3 = DistolicProcessDta(ArrayAmp, ArraymmHg, SetDistolic)

ArrayAmp = DtaAmp_14_AMP_Reg_100_65_80_S4
ArraymmHg = DtaMMHg_14_AMP_Reg_100_65_80_S4

SystolicResult4 = SystolicProcessDta(ArrayAmp, ArraymmHg, SetSystolic)
DistolicResult4 = DistolicProcessDta(ArrayAmp, ArraymmHg, SetDistolic)

print("\n DtaAmp_14_AMP_Reg_100_65_80_S4 \n", ArrayAmp)
print("\n DtaMMHg_14_AMP_Reg_100_65_80_S4 \n", ArraymmHg)

ArrayAmp = DtaAmp_15_AMP_Reg_100_65_80_S5
ArraymmHg = DtaMMHg_15_AMP_Reg_100_65_80_S5

SystolicResult5 = SystolicProcessDta(ArrayAmp, ArraymmHg, SetSystolic)
DistolicResult5 = DistolicProcessDta(ArrayAmp, ArraymmHg, SetDistolic)


# Vertical Combine Result    
Systolic_100_65_80_CombineResultVertical = np.vstack((SystolicResult1, SystolicResult2, SystolicResult3, SystolicResult4, SystolicResult5))    # vertical stack
Distolic_100_65_80_CombineResultVertical = np.vstack((DistolicResult1, DistolicResult2, DistolicResult3, DistolicResult4, DistolicResult5))    # vertical stack
#print(Systolic_100_65_80_CombineResultVertical)    

"""================================================ 120 / 80 / 80  ==========================="""
SetSystolic = 120
SetDistolic = 80


ArrayAmp = DtaAmp_16_AMP_Reg_120_80_80_S1
ArraymmHg = DtaMMHg_16_AMP_Reg_120_80_80_S1

SystolicResult1 = SystolicProcessDta(ArrayAmp, ArraymmHg, SetSystolic)
DistolicResult1 = DistolicProcessDta(ArrayAmp, ArraymmHg, SetDistolic)


ArrayAmp = DtaAmp_17_AMP_Reg_120_80_80_S2
ArraymmHg = DtaMMHg_17_AMP_Reg_120_80_80_S2

SystolicResult2 = SystolicProcessDta(ArrayAmp, ArraymmHg, SetSystolic)
DistolicResult2 = DistolicProcessDta(ArrayAmp, ArraymmHg, SetDistolic)

ArrayAmp = DtaAmp_18_AMP_Reg_120_80_80_S3
ArraymmHg = DtaMMHg_18_AMP_Reg_120_80_80_S3

SystolicResult3 = SystolicProcessDta(ArrayAmp, ArraymmHg, SetSystolic)
DistolicResult3 = DistolicProcessDta(ArrayAmp, ArraymmHg, SetDistolic)

ArrayAmp = DtaAmp_19_AMP_Reg_120_80_80_S4
ArraymmHg = DtaMMHg_19_AMP_Reg_120_80_80_S4

SystolicResult4 = SystolicProcessDta(ArrayAmp, ArraymmHg, SetSystolic)
DistolicResult4 = DistolicProcessDta(ArrayAmp, ArraymmHg, SetDistolic)

ArrayAmp = DtaAmp_20_AMP_Reg_120_80_80_S5
ArraymmHg = DtaMMHg_20_AMP_Reg_120_80_80_S5

SystolicResult5 = SystolicProcessDta(ArrayAmp, ArraymmHg, SetSystolic)
DistolicResult5 = DistolicProcessDta(ArrayAmp, ArraymmHg, SetDistolic)


# Vertical Combine Result    
Systolic_120_80_80_CombineResultVertical = np.vstack((SystolicResult1, SystolicResult2, SystolicResult3, SystolicResult4, SystolicResult5))    # vertical stack
Distolic_120_80_80_CombineResultVertical = np.vstack((DistolicResult1, DistolicResult2, DistolicResult3, DistolicResult4, DistolicResult5))    # vertical stack
#print(Systolic_120_80_80_CombineResultVertical)  
 

"""================================================ 150 / 100 / 80  ==========================="""
SetSystolic = 150
SetDistolic = 100


ArrayAmp = DtaAmp_21_AMP_Reg_100_65_80_S1
ArraymmHg = DtaMMHg_21_AMP_Reg_100_65_80_S1

SystolicResult1 = SystolicProcessDta(ArrayAmp, ArraymmHg, SetSystolic)
DistolicResult1 = DistolicProcessDta(ArrayAmp, ArraymmHg, SetDistolic)


ArrayAmp = DtaAmp_22_AMP_Reg_150_100_80_S2
ArraymmHg = DtaMMHg_22_AMP_Reg_150_100_80_S2

SystolicResult2 = SystolicProcessDta(ArrayAmp, ArraymmHg, SetSystolic)
DistolicResult2 = DistolicProcessDta(ArrayAmp, ArraymmHg, SetDistolic)

ArrayAmp = DtaAmp_23_AMP_Reg_150_100_80_S3
ArraymmHg = DtaMMHg_23_AMP_Reg_150_100_80_S3

SystolicResult3 = SystolicProcessDta(ArrayAmp, ArraymmHg, SetSystolic)
DistolicResult3 = DistolicProcessDta(ArrayAmp, ArraymmHg, SetDistolic)

ArrayAmp = DtaAmp_24_AMP_Reg_150_100_80_S4
ArraymmHg = DtaMMHg_24_AMP_Reg_150_100_80_S4

SystolicResult4 = SystolicProcessDta(ArrayAmp, ArraymmHg, SetSystolic)
DistolicResult4 = DistolicProcessDta(ArrayAmp, ArraymmHg, SetDistolic)

ArrayAmp = DtaAmp_25_AMP_Reg_150_100_80_S5
ArraymmHg = DtaMMHg_25_AMP_Reg_150_100_80_S5

SystolicResult5 = SystolicProcessDta(ArrayAmp, ArraymmHg, SetSystolic)
DistolicResult5 = DistolicProcessDta(ArrayAmp, ArraymmHg, SetDistolic)


# Vertical Combine Result    
Systolic_150_100_80_CombineResultVertical = np.vstack((SystolicResult1, SystolicResult2, SystolicResult3, SystolicResult4, SystolicResult5))    # vertical stack
Distolic_150_100_80_CombineResultVertical = np.vstack((DistolicResult1, DistolicResult2, DistolicResult3, DistolicResult4, DistolicResult5))    # vertical stack
#print(Systolic_150_100_80_CombineResultVertical)  


"""================================================ 200 / 150 / 80  ==========================="""
SetSystolic = 200
SetDistolic = 150


ArrayAmp = DtaAmp_26_AMP_Reg_200_150_80_S1
ArraymmHg = DtaMMHg_26_AMP_Reg_200_150_80_S1

SystolicResult1 = SystolicProcessDta(ArrayAmp, ArraymmHg, SetSystolic)
DistolicResult1 = DistolicProcessDta(ArrayAmp, ArraymmHg, SetDistolic)


ArrayAmp = DtaAmp_27_AMP_Reg_200_150_80_S2
ArraymmHg = DtaMMHg_27_AMP_Reg_200_150_80_S2

SystolicResult2 = SystolicProcessDta(ArrayAmp, ArraymmHg, SetSystolic)
DistolicResult2 = DistolicProcessDta(ArrayAmp, ArraymmHg, SetDistolic)

ArrayAmp = DtaAmp_28_AMP_Reg_200_150_80_S3
ArraymmHg = DtaMMHg_28_AMP_Reg_200_150_80_S3

SystolicResult3 = SystolicProcessDta(ArrayAmp, ArraymmHg, SetSystolic)
DistolicResult3 = DistolicProcessDta(ArrayAmp, ArraymmHg, SetDistolic)

ArrayAmp = DtaAmp_29_AMP_Reg_200_150_80_S4
ArraymmHg = DtaMMHg_29_AMP_Reg_200_150_80_S4

SystolicResult4 = SystolicProcessDta(ArrayAmp, ArraymmHg, SetSystolic)
DistolicResult4 = DistolicProcessDta(ArrayAmp, ArraymmHg, SetDistolic)

ArrayAmp = DtaAmp_30_AMP_Reg_200_150_80_S5
ArraymmHg = DtaMMHg_30_AMP_Reg_200_150_80_S5

SystolicResult5 = SystolicProcessDta(ArrayAmp, ArraymmHg, SetSystolic)
DistolicResult5 = DistolicProcessDta(ArrayAmp, ArraymmHg, SetDistolic)


# Vertical Combine Result    
Systolic_200_150_80_CombineResultVertical = np.vstack((SystolicResult1, SystolicResult2, SystolicResult3, SystolicResult4, SystolicResult5))    # vertical stack
Distolic_200_150_80_CombineResultVertical = np.vstack((DistolicResult1, DistolicResult2, DistolicResult3, DistolicResult4, DistolicResult5))    # vertical stack
#print(Distolic_200_150_80_CombineResultVertical) 


"""================================================ 255 / 195 / 80  ==========================="""
SetSystolic = 255
SetDistolic = 195


ArrayAmp = DtaAmp_31_AMP_Reg_255_195_80_S1
ArraymmHg = DtaMMHg_31_AMP_Reg_255_195_80_S1


SystolicResult1 = SystolicProcessDta(ArrayAmp, ArraymmHg, SetSystolic)
DistolicResult1 = DistolicProcessDta(ArrayAmp, ArraymmHg, SetDistolic)


ArrayAmp = DtaAmp_32_AMP_Reg_255_195_80_S2
ArraymmHg = DtaMMHg_32_AMP_Reg_255_195_80_S2

SystolicResult2 = SystolicProcessDta(ArrayAmp, ArraymmHg, SetSystolic)
DistolicResult2 = DistolicProcessDta(ArrayAmp, ArraymmHg, SetDistolic)

ArrayAmp = DtaAmp_33_AMP_Reg_255_195_80_S3
ArraymmHg = DtaMMHg_33_AMP_Reg_255_195_80_S3

SystolicResult3 = SystolicProcessDta(ArrayAmp, ArraymmHg, SetSystolic)
DistolicResult3 = DistolicProcessDta(ArrayAmp, ArraymmHg, SetDistolic)

ArrayAmp = DtaAmp_34_AMP_Reg_255_195_80_S4
ArraymmHg = DtaMMHg_34_AMP_Reg_255_195_80_S4

SystolicResult4 = SystolicProcessDta(ArrayAmp, ArraymmHg, SetSystolic)
DistolicResult4 = DistolicProcessDta(ArrayAmp, ArraymmHg, SetDistolic)

ArrayAmp = DtaAmp_35_AMP_Reg_255_195_80_S5
ArraymmHg = DtaMMHg_35_AMP_Reg_255_195_80_S5

SystolicResult5 = SystolicProcessDta(ArrayAmp, ArraymmHg, SetSystolic)
DistolicResult5 = DistolicProcessDta(ArrayAmp, ArraymmHg, SetDistolic)


# Vertical Combine Result    
Systolic_255_195_80_CombineResultVertical = np.vstack((SystolicResult1, SystolicResult2, SystolicResult3, SystolicResult4, SystolicResult5))    # vertical stack
Distolic_255_195_80_CombineResultVertical = np.vstack((DistolicResult1, DistolicResult2, DistolicResult3, DistolicResult4, DistolicResult5))    # vertical stack
#print(Systolic_255_195_80_CombineResultVertical)

"""================================================ ALL  ==========================="""
SystolicResult = np.vstack((Systolic_60_30_80_CombineResultVertical, Systolic_80_50_80_CombineResultVertical, Systolic_100_65_80_CombineResultVertical, Systolic_120_80_80_CombineResultVertical, Systolic_150_100_80_CombineResultVertical, Systolic_200_150_80_CombineResultVertical, Systolic_255_195_80_CombineResultVertical))    # vertical stack
DistolicResult = np.vstack((Distolic_60_30_80_CombineResultVertical, Distolic_80_50_80_CombineResultVertical, Distolic_100_65_80_CombineResultVertical, Distolic_120_80_80_CombineResultVertical, Distolic_150_100_80_CombineResultVertical, Distolic_200_150_80_CombineResultVertical, Distolic_255_195_80_CombineResultVertical))    # vertical stack
print("\n DistolicResult\n", DistolicResult)

"""================================================ Systolic Statistics  ==========================="""



SystolicCoeff_M = SystolicResult[:,5]
SystolicCoeff_H = SystolicResult[:,9]
SystolicCoeff_L = SystolicResult[:,13]



SystolicCoeff_All = np.hstack((SystolicCoeff_M, SystolicCoeff_H, SystolicCoeff_L))
SystolicCoeff_All_Vertical = np.vstack((SystolicCoeff_M, SystolicCoeff_H, SystolicCoeff_L))
print("\n SystolicCoeff_All_Vertical \n", SystolicCoeff_All_Vertical)
#print("\n SystolicCoeff_All \n", SystolicCoeff_M)


SystolicCoeff_M_CntStatistic = pd.value_counts(SystolicCoeff_M) # 統計各元素出現次數
print("\n ----- SystolicCoeff_M_CntStatistic -----\n", SystolicCoeff_M_CntStatistic)

SystolicCoeff_H_CntStatistic = pd.value_counts(SystolicCoeff_H) # 統計各元素出現次數
print("\n ----- SystolicCoeff_H_CntStatistic -----\n", SystolicCoeff_H_CntStatistic)

SystolicCoeff_L_CntStatistic = pd.value_counts(SystolicCoeff_L) # 統計各元素出現次數
print("\n ----- SystolicCoeff_L_CntStatistic -----\n", SystolicCoeff_L_CntStatistic)

SystolicCoeff_All_CntStatistic = pd.value_counts(SystolicCoeff_All) # 統計各元素出現次數
print("\n ----- SystolicCoeff_All_CntStatistic -----\n", SystolicCoeff_All_CntStatistic)



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
print("\n SystolicCoeff_All \n", DistolicCoeff_All)


DistolicCoeff_M_CntStatistic = pd.value_counts(DistolicCoeff_M) # 統計各元素出現次數
print("\n ----- DistolicCoeff_M_CntStatistic -----\n", SystolicCoeff_M_CntStatistic)

DistolicCoeff_H_CntStatistic = pd.value_counts(DistolicCoeff_H) # 統計各元素出現次數
print("\n ----- DistolicCoeff_H_CntStatistic -----\n", DistolicCoeff_H_CntStatistic)

DistolicCoeff_L_CntStatistic = pd.value_counts(DistolicCoeff_L) # 統計各元素出現次數
print("\n ----- DistolicCoeff_L_CntStatistic -----\n", DistolicCoeff_L_CntStatistic)

DistolicCoeff_All_CntStatistic = pd.value_counts(DistolicCoeff_All) # 統計各元素出現次數
print("\n ----- DistolicCoeff_All_CntStatistic -----\n", DistolicCoeff_All_CntStatistic)


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


if SaveResult == True:
    np.savetxt('Systolic.csv', SystolicResult, delimiter = ',')
    np.savetxt('Distolic.csv', SystolicResult, delimiter = ',')

#a = np.asarray([ [1,2,3], [4,5,6], [7,8,9] ])
#np.savetxt('new.csv', a, delimiter = ',')
