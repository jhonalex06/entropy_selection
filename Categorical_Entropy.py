import pandas as pd
import numpy as np
import math
import tkinter as tk
from numpy import genfromtxt

#df = pd.read_csv('categorical_test.csv', sep=';')
#df = pd.read_csv('numerical_test.csv', sep=';')
df = pd.read_csv('breast-cancer.csv', sep=',')

y_name = 'EXPERIENCIA'
#Categorical = True and Numerical = False
model = True

def general_categorical_entropy(df):
    y, x = df.shape
    data = df.values
    weights = []

    print ('Calculado...')

    for i in range(y):
        for j in range(y):
            weights.append(sum(data[i] == data[j])/x)

    weights = np.array(weights)
    weights = weights[(weights > 0) & (weights < 1)]
    first = weights * np.log2(weights) + (1 - weights) * np.log2(1 - weights) 
    return sum(first)/2

def general_numerical_entropy(df):
    y, x = df.shape
    data = df.values
    weights = []
    weights2 = []
    maximun = []
    minimun = []

    for i in df.columns:
        maximun.append(float(df[i].max()))
        minimun.append(float(df[i].min()))

    for i in range(y):
        for j in range(y):
            weights.append((data[i] - data[j])/(np.array(maximun) - np.array(minimun)))

    weights = np.array(weights)
    weights = np.power(weights,2)
    for k in weights:
        weights2.append(math.sqrt(sum(k))/x)

    weights = np.array(weights2)
    weights = weights[(weights > 0) & (weights < 1)]
    first = weights * np.log2(weights) + (1 - weights) * np.log2(1 - weights) 
    #print (sum(first)/2)
    return sum(first)/2

def specific_entropies(df, total_entropy, model):
    specific = {}
    for count, i in enumerate(df.columns):
        df_delete = df.drop(columns=[i])
        if model:
            specific[i] = abs(general_categorical_entropy(df_delete) - total_entropy)
        else:
            specific[i] = abs(general_numerical_entropy(df_delete) - total_entropy) 
    
    print ('{} columns left'.format(count))
    return specific

def select_minimun_entropy(df, model):
    column0 = []
    column1 = []
    if model:
        total = general_categorical_entropy(df)
        specific_diferences = specific_entropies(df, total, model)
        for i in specific_diferences:
            column0.append(i)
            column1.append(specific_diferences[i])
    else:
        total = general_numerical_entropy(df)
        specific_diferences = specific_entropies(df, total, model)
        for i in specific_diferences:
            column0.append(i)
            column1.append(specific_diferences[i])

    df_decision = pd.DataFrame(zip(column0, column1), columns=['name', 'diference'])
    delete_name = df_decision[df_decision['diference'] == df_decision['diference'].min()]['name'].values[0]
    #print (df_decision)
    print ('The Column deleted was {}'.format(delete_name))
    df_drop = df.drop(columns=[delete_name])
    if len(df_drop.columns) == 1:
        print (('The Final Column is {}'.format(df_drop.columns[0]))) 
    return df_drop    

def excecute_selection(df, model, text, root):
    while len(df.columns) >= 2:
        print (type(text))
        text.insert(tk.END,'Jhonsi')
        root.update_idletasks()
        df = select_minimun_entropy(df, model)