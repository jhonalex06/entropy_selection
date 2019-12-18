import pandas as pd
import numpy as np
from numpy import genfromtxt

df = pd.read_csv('categorical_test.csv', sep=';')
y_name = 'EXPERIENCIA'

def general_entropy(df):
    y, x = df.shape
    data = df.values
    weights = []

    for i in range(y):
        for j in range(y):
            weights.append(sum(data[i] == data[j])/x)

    weights = np.array(weights)
    weights = weights[(weights > 0) & (weights < 1)]
    first = weights * np.log2(weights) + (1 - weights) * np.log2(1 - weights) 
    return sum(first)/2

def specific_entropies(df, total_entropy):
    specific = {}
    for i in df.columns:
        df_delete = df.drop(columns=[i])
        specific[i] = abs(general_entropy(df_delete) - total_entropy)
    
    return specific

def select_minimun_entropy(df,name):
    column0 = []
    column1 = []
    total = general_entropy(df)
    specific_diferences = specific_entropies(df, total)
    for i in specific_diferences:
        if i != name:
            column0.append(i)
            column1.append(specific_diferences[i])

    df_decision = pd.DataFrame(zip(column0, column1), columns=['name', 'diference'])
    delete_name = df_decision[df_decision['diference'] == df_decision['diference'].min()]['name'].values[0]
    print (df_decision)
    print ('The Column deleted is {}'.format(delete_name))
    df_drop = df.drop(columns=[delete_name])
    return df_drop    

#select_minimun_entropy(df, y_name)
#print (len(df.columns))

while len(df.columns) >= 2:
    df = select_minimun_entropy(df, y_name)