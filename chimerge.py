import pandas as pd
from collections import Counter
import numpy as np
import tkinter as tk

def chimerge(data, attr, label, max_intervals):
    labels = sorted(set(data[label]))
    empty_count = {l: 0 for l in labels}
    intervals = [[sorted(set(data[attr]))[i], sorted(set(data[attr]))[i]] for i in range(len(sorted(set(data[attr]))))]
    while len(intervals) > max_intervals: # While loop
        chi = []
        for i in range(len(intervals)-1):
            # Calculate the Chi2 value
            obs0 = data[data[attr].between(intervals[i][0], intervals[i][1])]
            obs1 = data[data[attr].between(intervals[i+1][0], intervals[i+1][1])]
            total = len(obs0) + len(obs1)
            count_0 = np.array([v for i, v in {**empty_count, **Counter(obs0[label])}.items()])
            count_1 = np.array([v for i, v in {**empty_count, **Counter(obs1[label])}.items()])
            count_total = count_0 + count_1
            expected_0 = count_total*sum(count_0)/total
            expected_1 = count_total*sum(count_1)/total
            chi_ = (count_0 - expected_0)**2/expected_0 + (count_1 - expected_1)**2/expected_1
            chi_ = np.nan_to_num(chi_) 
            chi.append(sum(chi_))
        min_chi = min(chi) 
        for i, v in enumerate(chi):
            if v == min_chi:
                min_chi_index = i
                break
        new_intervals = []
        skip = False
        done = False
        for i in range(len(intervals)):
            if skip:
                skip = False
                continue
            if i == min_chi_index and not done:
                t = intervals[i] + intervals[i+1]
                new_intervals.append([min(t), max(t)])
                skip = True
                done = True
            else:
                new_intervals.append(intervals[i])
        intervals = new_intervals

    return intervals


def excecute_chimerge(df, label, intervals, text, root):
    text.delete('1.0', tk.END)
    #iris = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)
    #iris = pd.read_csv('iris_example.csv')
    #iris.columns = ['sepal_l', 'sepal_w', 'petal_l', 'petal_w', 'type']
    #iris.to_csv('iris_example.csv')
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    newdf = df.select_dtypes(include=numerics)

    for attr in newdf.columns:
        title = 'Interval for', attr
        message = chimerge(data=df, attr=attr, label=label, max_intervals=int(intervals))
        msj = '{} \n {}'.format(title, message)
        text.insert(tk.END,'{} \n'.format(msj))
        root.update_idletasks()

#excecute_chimerge()
