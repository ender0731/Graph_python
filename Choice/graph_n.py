import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
###python program to display graphs
def graph_n(data,columns,directory):
    cat_columns=[]
    num_columns=[]
    if columns==0:
        columns=pd.read_csv(data).columns
    data=pd.read_csv(data)
    df=data[columns]
    df.dropna(inplace=True)
    for x in columns:
        if df[x].dtype=='object':
            cat_columns.append(x)
        elif len(set(df[x]))<10:
            cat_columns.append(x)
        else:
            num_columns.append(x)
    
#converting numeric data in categorical columns to string type for ease in making barplots   
    for x in cat_columns:
        df[x]=df[x].apply(str)
            
#Dealing with categorical data
    #generating countplots for categorical columns
    for x in cat_columns:
        plt.figure()
        sns.countplot(df[x])
        plt.title(f'Countplot_for_{x}')
       
    
    #barplot for categorical data with average value of numeric data
    for x1 in cat_columns:
        for y1 in num_columns:
            plt.figure()
            ax=sns.barplot(x=x1,y=y1,data=df)
            ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
            plt.title(f'Barplot_for_{x1}_and_{y1}')
            plt.tight_layout()
            plt.show()
            
        
#Dealing with numerical data
    for x in num_columns:
        # generating boxplots
        plt.figure()
        sns.boxplot(df[x])
        plt.title(f'Boxplot_for_{x}')
        #generating distplots
        plt.figure()
        sns.distplot(df[x])
        plt.title(f'Boxplot_for_{x}')
    #pairplot for numerical data
    plt.figure()
    sns.pairplot(df[num_columns])
    plt.title('Pairplot for the numerical variables')
    plt.show()
    return None