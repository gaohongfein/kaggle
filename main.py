import numpy as np
import pandas as pd
from pandas import Series, DataFrame

data_train = pd.read_csv("/home/gao/下载/Titanic/train.csv")
# print(data_train)

print(data_train.info())