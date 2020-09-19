# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pandas as pd
import tkinter.filedialog 
# Get file path 
path = tkinter.filedialog.askopenfilename()


# path = "/Users/cassandriagoh/Desktop/Python/Kaggle and applications/PLAYING.csv"

data = pd.read_csv(path)
# data = data.set_index('respid')

product_codes = []
users = []
for col in data:
    for i in range(len(data)):
        row = data.loc[i, col]
        value = data.iloc[i, 0]
        if row == 1:
            product_codes.append(value)
            users.append(col)
            # print (col, data.iloc[i, 0])
user_purchases = pd.DataFrame({"product_code": product_codes, "users": users})

export = tkinter.filedialog.asksaveasfilename(defaultextension = '.csv')
user_purchases.to_csv(export, index = False, header = True)
