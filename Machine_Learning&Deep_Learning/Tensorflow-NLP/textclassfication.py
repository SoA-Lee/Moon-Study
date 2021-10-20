import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline # 그래프를 주피터 노트북에서 바로 그리게 함

train_data = pd.read_csv("word2vec-nlp-tutorial/labeledTrainData.tsv",header=0,delimiter="\t",quoting=3)
train_data.head()