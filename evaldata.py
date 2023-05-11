# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 09:10:46 2020

@author: User
"""
import pandas as pd
import numpy as np

class EvalData():
    
    def __init__(self):
        print('Eval Data Object Created')
        
    def get_data(self, BASE='', measure=''):

        df_gan = pd.read_csv(BASE + 'MadGan.txt', sep='\t')
        df_auto = pd.read_csv(BASE + 'AutoEnco.txt', sep='\t')
        df_lstm = pd.read_csv(BASE + 'Lstm.txt', sep='\t')
        df_iso = pd.read_csv(BASE + 'IsoForest.txt', sep='\t')
        df_gaus = pd.read_csv(BASE + 'GausianMixtureModel.txt', sep='\t')
        df_onecls = pd.read_csv(BASE + 'OneClassSvm.txt', sep='\t')
        df_gblstm = pd.read_csv(BASE + 'MadGanBiLSTM.txt', sep='\t')
        df_gcnn = pd.read_csv(BASE + 'MadGanCNN.txt', sep='\t')
        df_tanosagan = pd.read_csv(BASE + 'TAnoSAGan.txt', sep='\t')

        rows = []
        rows.append(df_gan[df_gan['Measurement']==measure].values[0][1:])
        rows.append(df_auto[df_auto['Measurement']==measure].values[0][1:])
        rows.append(df_lstm[df_lstm['Measurement']==measure].values[0][1:])
        rows.append(df_iso[df_iso['Measurement']==measure].values[0][1:])
        rows.append(df_gaus[df_gaus['Measurement']==measure].values[0][1:])
        rows.append(df_onecls[df_onecls['Measurement']==measure].values[0][1:])
        rows.append(df_gblstm[df_gblstm['Measurement']==measure].values[0][1:])
        rows.append(df_gcnn[df_gcnn['Measurement']==measure].values[0][1:])
        rows.append(df_tanosagan[df_tanosagan['Measurement']==measure].values[0][1:])
        
        
        return np.array(rows)