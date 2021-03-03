
import pandas as pd
import numpy as np


def readExcel():
    path ='/Users/hanxiaodi/PycharmProjects/CCSassistant/excelTempleFile/批量开户测试.xlsx'
    df = pd.read_excel(path)
    return df


def get_data():
    df=readExcel()
    rowNums=df.shape[0]
    # colNums= df.shape[1]
    customerList = []
    i =0
    while i < rowNums:
        dict1 =dict(df.loc[i])
        customerList.append(dict1)
        i+=1
    print(customerList)
    return customerList

def append_data_to_excel():
    pass


def writeExcel(data,filePath):
    frame = pd.DataFrame(data)
    print(frame)
    frame.to_excel(filePath)

if __name__ == '__main__':
    get_data()

