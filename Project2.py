# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 14:44:57 2019

@author: Peter Guirguis

last edited Sun Feb 17 5:28 2019 
"""
 

import numpy as np

import pandas as pd

"""Set up excel file an I-A matrix"""

df = pd.read_excel(r'C:/Users/Peter/Documents/Eco-LCA/Step1.xlsx', sheet_name = 'A380')

A = df.values

""" Change length_A to change the size of the A matrix """

length_A = 380

index = {}

VC_All = []

name = []

df2 = pd.read_excel(r'C:/Users/Peter/Documents/Eco-LCA/sector_code_new.xlsx', sheet_name = 'Sheet1')

df2_val = df2.values

for i in range (0,length_A-1):
    name.append(df2_val[i,2].lower())
    index[name[i]] = int(df2_val[i,0])

"""Setting the matrix"""

I = np.eye(length_A-1)

IA = np.subtract(I,A)

bar_X_bar = IA

unc = np.zeros((length_A-1,length_A-1))

"""Adding Value Chain"""

VC = 'default'

count = 0

search  = 'default'

while VC != '':
    
    VC = input("Enter the name of Value Chain or leave blank : \n")
    
    if VC != '':
        
        VC_All.append(VC)
        
        count = 1+ count
        
        print ("For %s : \n" % VC )
        
        print("Enter flow: ")
        
        equ_val = float(input ())
        
        new_col = np.zeros((length_A+count-1,1))
        
        new_col[length_A+count-2,0] = equ_val
        
        print ("Enter uncertainty: ")
        
        unc_val = float(input())
        
        unc_new_col = np.zeros((length_A+count-1,1))
        
        unc_new_col[length_A+count-2,0] = unc_val
        
        search ='default'
        
        while search != '':
            
            print ("Enter search words for inputs into %s or leave blank : " % VC)
            
            search =  input()
            
            if search != '':
                
            
                matching = [s for s in name if search in s]
            
                for i in matching:
                    print ("%d    %s" % (index[i], i))
                
                print("Enter number of process or leave blank to enter a differnet search : ")
            
                ind_search = input()
                
                
                if ind_search != '':
                    
                    ind_search = int(ind_search)
                    
                    print ("For %s into %s:  " % (name[ind_search-1],VC))
                    
                    print ("Enter flow: ")
                    
                    in_val = float(input())
                    
                    if ind_search < length_A:
                        
                        print ("Enter price: ")
                        
                        price = float(input())
                        
                        in_val = in_val*price
                        
                    new_col[ind_search-1, 0] = -in_val                   
                    
                    print ("Enter uncertainty: ")
                    
                    unc_in_val = float(input())
                    
                    unc_new_col[ind_search-1,0] = -unc_in_val
                    
        new_row = np.zeros((1,length_A+count-2))
                    
        bar_X_bar = np.concatenate((bar_X_bar,new_row),axis=0)
        
        bar_X_bar = np.concatenate((bar_X_bar,new_col),axis=1)
        
        name.append(VC.lower())
        
        index[VC.lower()] = length_A + count-2
        
        unc = np.concatenate((unc, new_row),axis=0)
        
        unc = np.concatenate((unc,unc_new_col),axis=1)

L = count
        
        
equip = input("Enter the name of equipment or leave blank : ")
 
if equip != '':
    
    count = count + 1
    
    print ("For %s : \n" % equip )
    
    print("Enter flow: ")
    
    equ_val = float(input ())
    
    new_col = np.zeros((length_A+count-1,1))
    
    new_col[length_A+count-2,0] = equ_val
    
    print ("Enter uncertainty: ")
    
    unc_val = float(input())
    
    unc_new_col = np.zeros((length_A+count-1,1))
    
    unc_new_col[length_A+count-2,0] = unc_val
    
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
                
                print ("For %s into %s:  " % (name[ind_search-1],equip))
                
                print ("Enter flow: ")
                
                in_val = float(input())
                
                if ind_search < length_A:
                    
                    print ("Enter price: ")
                    
                    price = float(input())
                    
                    in_val = in_val*price
                    
                new_col[ind_search-1, 0] = -in_val                   
                
                print ("Enter uncertainty: ")
                
                unc_in_val = float(input())
                
                unc_new_col[ind_search-1,0] = -unc_in_val
                
    new_row = np.zeros((1,length_A+count-2))
                
    bar_X_bar = np.concatenate((bar_X_bar,new_row),axis=0)
    
    bar_X_bar = np.concatenate((bar_X_bar,new_col),axis=1)
    
    name.append(equip.lower())
    
    index[equip.lower()] = length_A + count-2
    
    unc = np.concatenate((unc, new_row),axis=0)
    
    unc = np.concatenate((unc,unc_new_col),axis=1)
    
"""A is the A matrix
   B is the Value chain matrix
   C is the quipment matrix"""
    
AB = np.zeros((L,length_A))

AC = np.zeros((1,length_A))

BC = np.zeros((1,L))


"""Constract AB matrix"""

k = 0

search = name[0:length_A-1]

for j in VC_All:
    matching = [s for s in search if j in s]
            
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
    