# -*- coding: utf-8 -*-
"""ICA7P1_KatiJohnson.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lBJSJsUYa4QzQo8NPXbDkWpakfhSNwWv
"""

from google.colab import drive
drive.mount('/content/drive')

"""1. Use pandas in Python to read the file to a data frame called boxoffice, show the first lines by using head()"""

import pandas as pd

boxoffice = pd.read_csv('/content/drive/MyDrive/CSC302/DATA/boxoffice.csv')
boxoffice.head()

"""Output the amount for Star Wars by using iloc or loc"""

boxoffice.loc[0,'amount']

"""Please run the following codes in different cells and observe what they are producin

boxoffice['amount'].plot.bar()
import matplotlib.pyplot as plt
plt.figure(figsize=(15, 3))
plt.bar(boxoffice['title'],boxoffice['amount'])
"""

boxoffice['amount'].plot.bar()

import matplotlib.pyplot as plt

plt.figure(figsize=(15, 3))
plt.bar(boxoffice['title'],boxoffice['amount'])