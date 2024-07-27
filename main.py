import pandas as pd
import matplotlib
matplotlib.use('QtAgg')
from keys import FILE_PATH
from commands import *


import matplotlib.pyplot as plt

file = pd.read_csv(FILE_PATH)
fileDf = pd.DataFrame(file)

category = fileDf['category']
countedcategory = category.value_counts()
category_list = countedcategory.to_list()
percenteges = percentage_per_item(category_list)

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.pie(percenteges, labels = percenteges)
plt.title('pizza')

plt.subplot(1, 2, 2)
plt.plot(countedcategory)
plt.title('linhas')

print(type(countedcategory))

plt.show()
