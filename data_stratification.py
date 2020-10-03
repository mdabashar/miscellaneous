# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 05:45:02 2020

@author: User
"""

import pandas as pd

class DataStratification:
    def __init__(self):
        pass
    
    def undersampling(df):
        df_0 = df[df.label==0]
        df_1 = df[df.label==1]
        if len(df_0) < len(df_1):
            df_1 = df_1.sample(len(df_0), replace=False)
        elif len(df_0) > len(df_1):
            df_0 = df_0.sample(int(len(df_1)), replace=False)
        df = pd.concat([df_0, df_1])
        del df_0, df_1
        df = df.sample(frac=1).reset_index(drop=True)
        return df
    
    def oversample(df=None):
        df_0 = df[df.billPaid==0]
        df_1 = df[df.billPaid==1]
        if len(df_0) > len(df_1):
            df_1 = df_1.sample(len(df_0), replace=True)
        elif len(df_0) < len(df_1):
            df_0 = df_0.sample(len(df_1), replace=True)
        df = pd.concat([df_0, df_1])
        del df_0, df_1
        df = df.sample(frac=1).reset_index(drop=True)
        return df
    
    if __name__=='__main__':
        print('executing locally')