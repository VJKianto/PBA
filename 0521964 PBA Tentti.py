
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import bs4
import seaborn as sns
from matplotlib import pyplot as plt
import matplotlib.font_manager


colnames=['Id','Title','Body','Tags','CreationDate','Y']
df1=pd.read_csv(r'C:\Users\Vona\data1.csv',names=colnames)
df2=pd.read_csv(r'C:\Users\Vona\data2.csv',names=colnames,encoding='latin-1') #2
df3=pd.merge(df1,df2,how='outer',on=colnames) #3
#df3=pd.concat([df1,df2],axis=1) #3 alternative

df3.rename(columns={'Y': 'Post category'}, inplace=True) #4
df3['Post category']=df3['Post category'].replace(['HQ'],'High-quality post')
df3['Post category']=df3['Post category'].replace(['LQ_EDIT','LQ_CLOSE'],'Low-quality post') #5


df3['Python in tags']=np.where(df3['Tags']=='<python>',True,False) #6
#df3.loc[df3['Tags']=='<python>','Python in tags']='True'
#df3.loc[df3['Tags']!='<python>','Python in tags']='False'  #6 alternative


df3.dropna(subset=['Body'],inplace=True)
df3['Body'] = df3['Body'].apply(lambda x: bs4.BeautifulSoup(x, 'lxml').get_text())# 7 


df3['Body']=df3['Body'].str.strip() #8

#df3['word_count'] = df3['Body'].str.split().str.len()  #9 alternative 
df3['word_count'] = df3['Body'].str.count(' ') + 1 #9, total or per row?


sns.catplot(x='Post category',y='word_count',kind='box',data=df3, sym='',notch=True) #10
#RuntimeWarning: Glyph missing from current font?? Unable to resolve
#sym='' removes outliers, notch=True shows confidence intervals for the median values. = 4 points?
plt.show()
