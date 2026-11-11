import pandas as pd
import numpy as np 
 
data = pd.read_excel("datas.xlsx")
# print(data.head())
data.drop(columns=["Date"], inplace=True)
# print(data.head())

l = np.log(data / data.shift(1))
l.dropna(axis=0, inplace=True)

l2 = l.mean()
print(l2.head())

