import pandas as pd
import matplotlib.pyplot as plt

print("Content-type: text/html\r\n\r\n")

df = pd.read_csv('Telangana.csv',skiprows=2)

df.plot(kind='line',x='Party',y='Won',color='blue')
plt.xticks(rotation=90)

#df.groupby(['Party','Won'])['Total'].size().unstack().plot(kind='bar',stacked=True)

plt.show()

df = pd.read_csv('Mizoram.csv',skiprows=2)

df.plot(kind='line',x='Party',y='Won',color='blue')
plt.xticks(rotation=90)

#df.groupby(['Party','Won'])['Total'].size().unstack().plot(kind='bar',stacked=True)

plt.show()



df = pd.read_csv('Madhyapradesh.csv',skiprows=2)

df.plot(kind='line',x='Party',y='Won',color='blue')
plt.xticks(rotation=90)

#df.groupby(['Party','Won'])['Total'].size().unstack().plot(kind='bar',stacked=True)

plt.show()

df = pd.read_csv('Rajasthan.csv',skiprows=2)

df.plot(kind='line',x='Party',y='Won',color='blue')
plt.xticks(rotation=90)

#df.groupby(['Party','Won'])['Total'].size().unstack().plot(kind='bar',stacked=True)

plt.show()

df = pd.read_csv('chattisgarh.csv',skiprows=2)

df.plot(kind='line',x='Party',y='Won',color='blue')
plt.xticks(rotation=90)

#df.groupby(['Party','Won'])['Total'].size().unstack().plot(kind='bar',stacked=True)

plt.show()

