import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('fivethirtyeight')


df = pd.read_csv('Suicides_in_India.csv',usecols=['Year','Gender','Total','State'])
df2 = pd.read_csv('crime.csv',usecols=['STATE/UT','Year','Murder'])
df2 = df2.rename(columns={'STATE/UT': 'State'})

jks = df[df.State.str.startswith('JAMMU')]
a = jks.copy()
jkm = df2[df2.State.str.startswith('JAMMU')]

jkm = jkm.groupby(['Year']).apply(sum)
jks = jks.groupby(['Year']).apply(sum)
bar1 = np.array(jkm.Murder)
bar2 = np.array(jks.Total)
years = [2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012]

fig , ax = plt.subplots()
murders = ax.bar(x=years ,height=bar1,width=0.80,color='#F04747',label='Murders')
suicides = ax.bar(x=years, height=bar2, width=0.80, color='#A1CDEC',bottom=bar1,label='Suicides')
ax.set_yscale('log')
ax.set_xticks(years)
#ax.set_xticklabels(years,rotation=45)
plt.legend()
plt.title('J&K Murders vs Suicides')
