# -*- coding: utf-8 -*-
"""Calculated.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KU13nsPiymZNIsjrbmSvVdxR2RVXEIkx
"""

def cal_sd(inputt,data):
    colum=[i for i in data.columns if data[i].dtype !='O']
    if inputt in colum and data[inputt].isnull().sum()==0:
        g = float("{:.2f}".format(data[inputt].std()))
        return g
    
    else:
        return -1
def preprocessing(data,inputt):
    
    #print(data.columns)
    #inputt=input("Enter column name for Calculate S.D")
    ret=cal_sd(inputt,data)
    if ret==-1:
        return("S.D not calculated of this column name or column doesnt exist or column held Null values or its not numberical column")
    else:
        return('S.D of this is {}'.format(ret))

def testing(file,inputt):
    import pandas as pd
    import numpy as np
    import os
    #file=input("enter path of the file with extension")
    fin=file.find(".")
    if (fin!=-1):
        if (file.split(".")[1] == "csv"):
            if os.path.isfile(file):    

                data=pd.read_csv(file)
                return(preprocessing(data,inputt))
            else:
                return("file does not exist")
        elif (file.split(".")[1] == "xlsx"):
            if os.path.isfile(file):    

                data=pd.read_excel(file)
                return(preprocessing(data,inputt))
            else:
                return("file does not exist")

        elif (file.split(".")[1]=="json"):
            if os.path.isfile(file):    
                    import json  
                    from pandas.io.json import json_normalize  

                    data= pd.read_json(open(file))

                    d=data.columns[0]


                    jsonn = json_normalize(data[d]) 
                    return(preprocessing(jsonn,inputt))
            else:
                return("file does not exist")
        else:
            return("Please enter correct extension")
    else:
        return("Please enter correct file and path and extension")

