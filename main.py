import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
from Choice import graph_y as gy
from Choice import graph_n as gn
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
		gy.graph_y(data,columns)
		break
	elif save_or_no=='n':
		gn.graph_n(data,columns)
		break
	else:
		print('Invalid input.\n')

		


		

