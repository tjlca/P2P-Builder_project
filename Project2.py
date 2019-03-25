# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 14:44:57 2019
@author: Peter Guirguis
last edited Sun Feb 17 5:28 2019 
"""
import sys
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate
import numpy as np

import pandas as pd

"""Set up excel file an I-A matrix"""

df = pd.read_excel(r'./Step1.xlsx', sheet_name = 'A380')

A = df.values

""" Change length_A to change the size of the A matrix """

length_A = 380

index = {}

VC_All = []

name = []

df2 = pd.read_excel(r'./sector_code_new.xlsx', sheet_name = 'Sheet1')

df2_val = df2.values

for i in range (0,length_A-1):
    name.append(df2_val[i,2].lower()+" economic sector")
    index[name[i]] = int(df2_val[i,0])

"""Setting the matrix"""

I = np.eye(length_A-1)

IA = np.subtract(I,A)

bar_X_bar = IA

unc = np.zeros((length_A-1,length_A-1))



#x_positions = np.arange(1,380,54)
#x_labels = [1,55,109,163,217,271,325,379]
#plt.imshow(np.asarray(bar_X_bar))
##plt.colorbar()
#plt.xticks(x_positions,x_labels)
#plt.yticks(x_positions,x_labels)
#plt.show(block=False)

draw_n = ['Oilseed\nFarming 1','..........\n..........','Government\nsector 379']
draw_v = [['*','*','*'],['*','*','*'],['*','*','*']]

draw_x = pd.DataFrame(draw_v,draw_n,draw_n)
print(tabulate(draw_x, headers='keys', tablefmt='fancy_grid'))
print("This is current Life cycle model")

print("Economy scale direct requirement matrices have already been imported\n")
print("Press Enter to continue/n")
input()

"""Adding Value Chain"""

VC = 'default'

count = 0

search  = 'default'

while VC != '':
    
    VC = input("\nEnter the name of Number "+str(count+1)+" Value Chain process to be included in the system or leave blank : \n")
    
    if VC != '':
        
        VC_All.append(VC)
        
        count = 1+ count
        
        print ("\nFor %s : \n" % VC )
        
        print("\nEnter the output flow of %s to be included MOSTLY in the VC make matrix diagonal elemenent in kg: " % VC)
        
        equ_val = float(input ())
        
        new_col = np.zeros((length_A+count-1,1))
        
        new_col[length_A+count-2,0] = equ_val
        
        print ("\nEnter uncertainty for the the output flow of %s to be included MOSTLY in the VC make matrix diagonal elemenent : " % VC)
        
        unc_val = float(input())
        
        unc_new_col = np.zeros((length_A+count-1,1))
        
        unc_new_col[length_A+count-2,0] = unc_val
        
        search ='default'
        
        print("\nVC process %s created\n" % VC)
        
        while search != '':
            
            print ("\nEnter search terms for activities in the current life cycle model displayed earlier providing inputs into %s process or leave blank.\n Make sure that economy scale sectors are too disaggregated and you cannot search for specific flows. : " % VC)
            
            search =  input()
            
            if search != '':
                
            
                matching = [s for s in name if search in s]
                
                
            
                for i in matching:
                    print ("%d    %s" % (index[i], i))
                
                
                print("\nEnter identification number of process to include in the model or leave blank to enter a different search : ")
            
                ind_search = input()
                
                
                if ind_search != '':
                    
                    ind_search = int(ind_search)
                    
                    print ("For %s into %s:  " % (name[ind_search-1],VC))
                    
                    print ("\nEnter input flow (kg) from %s into %s:  " % (name[ind_search-1],VC))
                    
                    in_val = float(input())
                    
                    if ind_search < length_A:
                        
                        print ("\nEnter price ($) for flow from %s into %s:  " % (name[ind_search-1],VC))
                        
                        price = float(input())
                        
                        in_val = in_val*price
                        
                    new_col[ind_search-1, 0] = -in_val                   
                    
                    print ("\nEnter uncertainty of the flow: from %s into %s:  " % (name[ind_search-1],VC))
                    
                    unc_in_val = float(input())
                    
                    unc_new_col[ind_search-1,0] = -unc_in_val
                    
                    print("\nInput to %s VC process from %s created:\n" %  (VC,name[ind_search-1]))
                    print("Enter next input to  %s VC process" % VC)
                    
        
        
        new_row = np.zeros((1,length_A+count-2))
                    
        bar_X_bar = np.concatenate((bar_X_bar,new_row),axis=0)
        
        bar_X_bar = np.concatenate((bar_X_bar,new_col),axis=1)
        
        name.append(VC.lower()+" value chain scale sector")
        
        index[VC.lower()+" value chain scale sector"] = length_A + count-1
        
        unc = np.concatenate((unc, new_row),axis=0)
        
        unc = np.concatenate((unc,unc_new_col),axis=1)
        
        print("\nVC process %s completed"% VC)
        
        draw_n.append(VC+' '+str(length_A + count-1) +'\nVC')
        draw_v = [x + ['*'] for x in draw_v]
        draw_v.append(draw_v[0])
        draw_x = pd.DataFrame(draw_v,draw_n,draw_n)
        print(tabulate(draw_x, headers='keys', tablefmt='fancy_grid'))
        print("This is current Life cycle model")

        

L = count
        
        
equip = input("Enter the name of equipment scale process or leave blank : ")
 
if equip != '':
    
    count = count + 1
    
    print ("For %s : \n" % equip )
    
    print("Enter the output flow in Kg of %s to be included in the EQ make matrix diagonal elemenent : " % equip)
    
    equ_val = float(input ())
    
    new_col = np.zeros((length_A+count-1,1))
    
    new_col[length_A+count-2,0] = equ_val
    
    print ("Enter uncertainty for the the output flow of %s to be included in the EQ make matrix diagonal elemenent : " % equip)
    
    unc_val = float(input())
    
    unc_new_col = np.zeros((length_A+count-1,1))
    
    unc_new_col[length_A+count-2,0] = unc_val
    
    search ='default'
    
    print("\n Equipment process %s Created\n"% equip)
    
    while search != '':
        
        print ("\nEnter search words for inputs from activities in the into equipment scale process %s or leave blank : " % equip)
        
        search =  input()
        
        if search != '':
            
        
            matching = [s for s in name if search in s]
        
            for i in matching:
                print ("%d    %s" % (index[i], i))
            
            print("\nEnter identification number of process to include in the model or leave blank to enter a different search : ")
        
            ind_search = input()
            
            
            if ind_search != '':
                
                ind_search = int(ind_search)
                
                print ("\nFor %s into %s:  " % (name[ind_search-1],equip))
                
                print ("\nEnter input flow (kg) from %s to %s:" %  (name[ind_search-1],equip))
                
                in_val = float(input())
                
                if ind_search < length_A:
                    
                    print ("Enter price($) for the flow from %s into %s:  " % (name[ind_search-1],equip))
                    
                    price = float(input())
                    
                    in_val = in_val*price
                    
                new_col[ind_search-1, 0] = -in_val                   
                
                print ("\nEnter uncertainty for the flow from %s into %s:  " % (name[ind_search-1],equip))
                
                unc_in_val = float(input())
                
                unc_new_col[ind_search-1,0] = -unc_in_val
                
                print("\nInput to Equipment process %s created\n" % equip)
                print("Enter next input to  %s Equipment process\n" %equip)
                
                
    new_row = np.zeros((1,length_A+count-2))
                
    bar_X_bar = np.concatenate((bar_X_bar,new_row),axis=0)
    
    bar_X_bar = np.concatenate((bar_X_bar,new_col),axis=1)
    
    name.append(equip.lower() + " Eq scale sector")
    
    index[equip.lower() + " Eq scale sector"] = length_A + count-1
    
    unc = np.concatenate((unc, new_row),axis=0)
    
    unc = np.concatenate((unc,unc_new_col),axis=1)
    
    print("\nVC process %s completed"% equip)    
    print("Enter to continue\n")
    input()
    
    draw_n.append(equip+' '+str(length_A + count-1) +'\nEquip')
    draw_v = [x + ['*'] for x in draw_v]
    draw_v.append(draw_v[0])
    draw_x = pd.DataFrame(draw_v,draw_n,draw_n)
    print(tabulate(draw_x, headers='keys', tablefmt='fancy_grid'))
    



"""A is the Economy matrix
   B is the Value chain matrix
   C is the quipment matrix"""
    
AB = np.zeros((L,length_A))

AC = np.zeros((1,length_A))

BC = np.zeros((1,L))


"""Constract AB matrix"""

k = 0

search = name[0:length_A-1]

for j in VC_All:
    matching = [s for s in search if j.lower() in s]
            
    for i in matching:
        print ("%d    %s" % (index[i], i))
        
    print("Enter number of process %s that matches or leave blank: " % j)
            
    ind_search = input()
    
    if ind_search != '':
        AB[k,int(ind_search)-1] = 1
    k = k + 1

"""Constract AC matrix"""

search = name[0:length_A-1]

matching = [s for s in search if equip in s]
            
for i in matching:
    print ("%d    %s" % (index[i], i))
        
print("Enter number of process %s that matches or leave blank: " % equip)
            
ind_search = input()
    
if ind_search != '':
    AC[int(ind_search)-1] = 1
    
"""Constract BC matrix"""

search = name[length_A-1:length_A+L-1]

matching = [s for s in search if equip in s]
            
for i in matching:
    print ("%d    %s" % (index[i], i))
        
print("Enter number of process %s that matches or leave blank: " % equip)
            
ind_search = input()
    
if ind_search != '':
    BC[(0,int(ind_search)-length_A)+1] = 1
    
BA = np.transpose(AB)

CA = np.transpose(AC)

CB = np.transpose(BC)

