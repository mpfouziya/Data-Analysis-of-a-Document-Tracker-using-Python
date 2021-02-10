# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 12:04:46 2018

@author: mpfou
"""
import matplotlib.pyplot as plt

#Plotting a dictionary
def show_dict_histo(dictionary,title='',x='',y=''):
    plt.xticks(rotation=90)
    plt.xlabel(x)
    plt.ylabel(y)        
    plt.title(title)   
    plt.bar(dictionary.keys(),dictionary.values(),width=0.5)
    plt.show()

#Plotting a dataframe    
def show_pd_histo(df,orient='bar',title='',x='',y='',annot=True):
    ax=df.plot(kind=orient,figsize=(10,7),width=0.5)
    ax.set_alpha(0.3)
    ax.set_title(title)
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    if annot:
        if orient=='bar':
            for i in ax.patches:
                ax.text(i.get_x(),i.get_height()+0.1,str(i.get_height()),fontsize=10)
        elif orient=='barh':
            for i in ax.patches:
                ax.text(i.get_width()+0.3,i.get_y()+0.38,str(i.get_width()),fontsize=10)
        
    plt.show()   