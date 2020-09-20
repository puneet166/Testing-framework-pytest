import pandas as pd

def cal_sd(inputt,data):
    colum=[i for i in data.columns if data[i].dtype !='O']
    if inputt in colum:
        g = float("{:.2f}".format(data[inputt].std()))
        return g
    else:
        return -1
def preprocessing(file_name,inputt):    
    import os
    #file_name=input("enter path with filename" )
    #file_name=input("enter path of the file")
    if os.path.isfile(file_name+'.csv'):    
    
        data=pd.read_csv(file_name+".csv")
        #print(data.columns)
       # inputt=input("Enter column name for Calculate S.D")
        #age="Age"
        ret=cal_sd(inputt,data)
        if ret==-1:
            return("S.D not calculated of this column name or column doesnt exist")
        else:
            return('S.D of this is {}'.format(ret))
    else:
        return("File doest exist")
#preprocessing("rr","kk")