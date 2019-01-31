# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 14:44:57 2019

@author: Peter Guirguis
"""
 

import numpy as np

import pandas as pd

"""Set up excel file an I-A matrix"""

df = pd.read_excel(r'C:/Users/Peter/Documents/Eco-LCA/Step1.xlsx', sheet_name = 'A380')

A = df.values

""" Change length_A to change the size of the A matrix """

length_A = 379

index = {}

equip_All = []

name = []

df2 = pd.read_excel(r'C:/Users/Peter/Documents/Eco-LCA/sector_code_new.xlsx', sheet_name = 'Sheet1')

df2_val = df2.values

for i in range (0,length_A):
    name.append(df2_val[i,2])
    index[name[i]] = i

"""Setting the matrix"""

I = np.eye(length_A+1)

IA = np.subtract(I,A)

bar_X_bar = IA

unc = np.zeros(length_A+1,length_A+1)

"""Adding equipment"""

equip = 'default'

count = 0

search  = 'default'

while equip != '':
    
    equip = input("Enter the name of *** or leave blank : \n")
    
    if equip != '':
        
        equip_All.append(equip)
        
        count = 1+ count
        
        print ("For %s : \n" % equip )
        
        print("Enter flow: \n")
        
        equ_val = float(input ())
        
        new_col = np.zeros((length_A+count+1,1))
        
        new_col[length_A+count,0] = equ_val
        
        print ("Enter uncertainty: \n")
        
        unc_val = float(input())
        
        unc_new_col = np.zeros((length_A+count+1,1))
        
        unc_new_col[length_A+count,0] = unc_val
        
        search ='default'
        
        while search != '':
            
            print ("Enter search words for inputs into %s or leave blank : " % equip)
            
            search =  input()
            
            if search != '':
                
            
                matching = [s for s in name if search in s]
            
                for i in matching:
                    print ("%d    %s" % (index[i], i))
                
                print("Enter number of process or leave blank to enter a differnet search : ")
            
                ind_search = input()
                
                
                if ind_search != '':
                    
                    ind_search = int(ind_search)
                    
                    print ("For %s into %s:  " % (name[ind_search],equip))
                    
                    print ("Enter flow: \n")
                    
                    in_val = float(input())
                    
                    new_col[ind_search, 0] = -in_val
                    
                    print ("Enter uncertainty: \n")
                    
                    unc_in_val = float(input())
                    
                    unc_new_col[ind_search,0] = -unc_in_val
                    
        new_row = np.zeros((1,length_A+count))
                    
        bar_X_bar = np.concatenate((bar_X_bar,new_row),axis=0)
        
        bar_X_bar = np.concatenate((bar_X_bar,new_col),axis=1)
        
        name.append(equip)
        
        index[equip] = length_A + count-1
        
        unc = np.concatenate((unc, new_row),axis=0)
        
        unc = np.concatenate((unc,unc_new_col),axis=1)
        
        
equip = input("Enter the name of equipment or leave blank : \n")
    
if equip != '':
        
    equip_All.append(equip)
        
    count = 1+ count
        
    print ("For of %s : \n" % equip )
    
    print ("Enter flow: \n")
        
    equ_val = float(input ())
        
    new_col = np.zeros((length_A+count+1,1))
    
    new_col[length_A+count,0] = equ_val
    
    print ("Enter uncertainty: \n")
    
    unc_val = float(input())
        
    unc_new_col = np.zeros((length_A+count+1,1))
        
    unc_new_col[length_A+count,0] = unc_val
        
    search ='default'
        
            
    while search != '':
            
        print ("Enter search words for inputs into %s or leave blank : " % equip)
            
        search =  input()
            
        if search != '':
                
            
            matching = [s for s in name if search in s]
            
            for i in matching:
                print ("%d    %s" % (index[i], i))
                
            print("Enter number of process or leave blank to enter a differnet search : ")
            
            ind_search = input()
                
                
            if ind_search != '':
                    
                ind_search = int(ind_search)
                    
                print ("For %s into %s:  " % (name[ind_search],equip))
                    
                print ("Enter flow: \n")
                    
                in_val = float(input())
                    
                new_col[ind_search, 0] = -in_val
                    
                print ("Enter uncertainty: \n")
                    
                unc_in_val = float(input())
                    
                unc_new_col[ind_search,0] = -unc_in_val
                    
    new_row = np.zeros((1,length_A+count))
                    
    bar_X_bar = np.concatenate((bar_X_bar,new_row),axis=0)
        
    bar_X_bar = np.concatenate((bar_X_bar,new_col),axis=1)
        
    name.append(equip)
        
    index[equip] = length_A + count-1
        
    unc = np.concatenate((unc,new_row),axis=0)
        
    unc = np.concatenate((unc,unc_new_col),axis=1)
        