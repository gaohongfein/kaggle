# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# <codecell>

data_train = pd.read_csv("/home/gao/Titanic/train.csv")
data_train

# <codecell>

data_train.info

# <codecell>

data_train.info()

# <codecell>

data_train.describe()

# <codecell>

import matplotlib.pyplot as plt

# <codecell>

fig = plt.figure()
fig.set(alpha=0.2)

plt.subplot2grid((2, 3),(0, 0))
data_train.Survived.value_counts().plot(kind='bar')
plt.title(u"获救人数情况1为获救")
plt.ylabel(u"人数")

plt.subplot2grid((2, 3), (0, 1))
data_train.Pclass.value_counts().plot(kind='bar')
plt.ylabel(u"人数")
plt.title(u"乘客等级")

plt.subplot2grid((2, 3), (0, 2))
plt.scatter(data_train.Survived, data_train.Age)
plt.ylabel("年龄")
plt.grid(b=None, which='major', axis='y')

plt.subplot2grid((2, 3), (1, 0), colspan=2)
data_train.Age[data_train.Pclass == 1].plot(kind='kde')
data_train.Age[data_train.Pclass == 2].plot(kind='kde')
data_train.Age[data_train.Pclass == 3].plot(kind='kde')
plt.xlabel("Age")
plt.ylabel("Dicht")
plt.title("Age in different Pclass")
plt.legend(('first Class', 'secend class', 'third Class'), loc='best')

plt.subplot2grid((2, 3), (1, 2))
data_train.Embarked.value_counts().plot(kind='bar')
plt.title("number")
plt.ylabel("number")




# <codecell>

fig = plt.figure(1)
fig.set(alpha=0.2)

Surived_0 = data_train.Pclass[data_train.Survived == 0].value_counts()
Surived_1 = data_train.Pclass[data_train.Survived == 1].value_counts()
df = pd.DataFrame({'Survied_1':Surived_1,'Survied_0':Surived_0})
df.plot(kind = 'bar', stacked = True)
plt.show()

# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


