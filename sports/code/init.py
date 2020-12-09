import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns

train = pd.read_csv('../input/train.csv')
train_add = pd.read_csv('../input/train_add.csv')
stasium = pd.read_csv('../input/stadium.csv')
add_2014 = pd.read_csv('../input/2014_add.csv')
test = pd.read_csv('../input/test.csv')

condition = pd.read_csv('../input/condition.csv')
condition_add = pd.read_csv('../input/condition_add.csv')

data = pd.concat([train, train_add], axis=0)

condition_new = pd.concat([condition, condition_add], axis=0)

tmp = pd.merge()
