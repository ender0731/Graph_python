import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
####################################################
def graph_y(data,columns):
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
        plt.savefig(f'Countplot_for_{x}.png')
    
    #barplot for categorical data with average value of numeric data
    for x1 in cat_columns:
        for y1 in num_columns:
            plt.figure()
            ax=sns.barplot(x=x1,y=y1,data=df)
            ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
            plt.title(f'Barplot_for_{x1}_and_{y1}')
            plt.tight_layout()
            plt.savefig(f'Barplot_for_{x1}_and_{y1}.png')
            plt.show()
            
        
#Dealing with numerical data
    for x in num_columns:
        # generating boxplots
        plt.figure()
        sns.boxplot(df[x])
        plt.title(f'Boxplot_for_{x}')
        plt.savefig(f'Boxplot_for_{x}.png')
        #generating distplots
        plt.figure()
        sns.distplot(df[x])
        plt.title(f'Boxplot_for_{x}')
        plt.savefig(f'Boxplot_for_{x}.png')
    #pairplot for numerical data
    plt.figure()
    sns.pairplot(df[num_columns])
    plt.title('Pairplot for the numerical variables')
    plt.savefig('Pairplot.png')
    plt.show()
    return None
####################################################
def graph_n(data,columns):
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
####################################################
print('Welcome to the graphing package.\nShut the current figure to display the next one.\nThe prompt will show a dialogue to press any key to close the window once all the graphs have been displayed.\n')
data=input('Please enter your file name.\n')
while True:
	dec_cols=input('Do you want to specify the columns required? Enter [y/n].\n')
	if dec_cols=='n':
		columns=0
		break
	elif dec_cols=='y':
		columns=list(input('Enter the column names as is in the dataset, separated by spaces. The column names have to be exactly the same.\n').split())
		break
	else:
		print('Please enter a valid input.\n')
#setting up the directory
while True:
    direc=input('Input the location of the file in the standard python syntax. Enter "n" if the file is in the current working directory.\n')
    if direc=='n':
        break
    else:
        try:
            os.chdir(direc)
            break
        except:
            print('Invalid directory.\n')
while True:
	save_or_no=input('Do you want to save the figures? Enter [y/n].\n')
	if save_or_no=='y':
		graph_y(data,columns)
		break
	elif save_or_no=='n':
		graph_n(data,columns)
		break
	else:
		print('Invalid input.\n')

		

