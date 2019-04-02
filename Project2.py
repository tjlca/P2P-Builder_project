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

#df = pd.read_excel(r'./Step1.xlsx', sheet_name = 'A380')

#A = df.values


df1 = pd.read_excel(r'./U.xlsx', sheet_name = 'Sheet1')
df2 = pd.read_excel(r'./V.xlsx', sheet_name = 'Sheet1')


U = df1.values
V = df2.values

A = np.matmul(U,np.linalg.inv((np.transpose(V))))

""" Change length_A to change the size of the A matrix """

length_A = 380





index = {}

VC_All = []

equip_All =[]

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
                
            
                matching = [s for s in name if search.lower() in s]
                
                
            
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
                    
                    unc_new_col[ind_search-1,0] = unc_in_val
                    
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
equip = 'default'
        
while equip != '':
  
    equip = input("Enter the name of equipment scale process Number "+str(count-L+1)+" or leave blank : ")
     
    if equip != '':
        
        equip_All.append(equip)
        
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
                
            
                matching = [s for s in name if search.lower() in s]
            
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
                    
                    unc_new_col[ind_search-1,0] = unc_in_val
                    
                    print("\nInput to Equipment process %s created\n" % equip)
                    print("Enter next input to  %s Equipment process\n" %equip)
                    
                    
        new_row = np.zeros((1,length_A+count-2))
                    
        bar_X_bar = np.concatenate((bar_X_bar,new_row),axis=0)
        
        bar_X_bar = np.concatenate((bar_X_bar,new_col),axis=1)
        
        name.append(equip.lower() + " Eq scale sector")
        
        index[equip.lower() + " Eq scale sector"] = length_A + count-1
        
        unc = np.concatenate((unc, new_row),axis=0)
        
        unc = np.concatenate((unc,unc_new_col),axis=1)
        
        print("\nEquipment scale process %s completed"% equip)    
        print("Enter to continue\n")
        input()
        
        draw_n.append(equip+' '+str(length_A + count-1) +'\nEquip')
        draw_v = [x + ['*'] for x in draw_v]
        draw_v.append(draw_v[0])
        draw_x = pd.DataFrame(draw_v,draw_n,draw_n)
        print(tabulate(draw_x, headers='keys', tablefmt='fancy_grid'))
        print("This is the current life cycle model\n")
        

print("\n\n\nPermutation matrix Creation Starts\n")

"""A is the Economy matrix
   B is the Value chain matrix
   C is the quipment matrix"""
    
permut_vc_econ = np.zeros((L,length_A-1))

"""If equip_All != none or VC_all != none"""

permut_equip_vc = np.zeros((count-L,L)) 


"""Constract permut_vc_econ matrix"""

k = 0

search = name[0:length_A-1]


for j in VC_All:
        
        
        matching = [s for s in search if j.lower() in s]
                
        for i in matching:
            print ("%d    %s" % (index[i], i))
        print("Starting creation of the Permutation matrices\n")    
        print("Enter number ID of the the Economy Scale sector that matches with VC process %s or leave blank:\n\n " % j)
                
        ind_search = input()
        
        if ind_search != '':
            permut_vc_econ[k,int(ind_search)-1] = 1
        k = k + 1
        print("\n \n")

"""Constract permut_equip_econ matrix"""

if equip_All != " " or equip_All != None  or equip_All != "":
    permut_equip_econ = np.zeros((count -L,length_A-1))


    k = 0
    for j in equip_All:
        matching = [s for s in search if j.lower() in s]
        
        for i in matching:
            print ("%d    %s" % (index[i], i))
            
        print("\n\nEnter number ID of the the Economy Scale sector that matches with Equipment process %s or leave blank \n\n" % j)
                
        ind_search = input()
        
        if ind_search != '':
            permut_equip_econ[k,int(ind_search)-1] = 1
        k= k + 1
        print("\n")
        print("\n")


    """Constract permut_equip_vc matrix"""
    k = 0
    search = name[length_A-1:length_A+L-1]
    for j in equip_All:
        matching = [s for s in search if j.lower() in s]
                    
        for i in matching:
            print ("%d    %s" % (index[i], i))
                
        print("\n\nEnter number ID of the the VC Scale sector that matches with Equipment scale process %s or leave blank): \n\n" % j)
                    
        ind_search = input()
            
        if ind_search != '':
            permut_equip_vc[(k,int(ind_search)-length_A)+1] = 1
            
        k =k + 1
    permut_econ_equip = np.transpose(permut_equip_econ)

    permut_vc_equip = np.transpose(permut_equip_vc)
    
permut_econ_vc = np.transpose(permut_vc_econ)



X_vc = bar_X_bar[(length_A-1):(length_A-1 + L),(length_A-1):(length_A-1 + L)]
X_eq = bar_X_bar[len(bar_X_bar)-(count - L):,len(bar_X_bar)-(count - L):]


V_vc = X_vc * np.eye(len(X_vc))
U_vc = (X_vc  - V_vc)*(-1)


V_eq = X_eq * np.eye(len(X_eq))
U_eq = (X_eq  - V_eq)*(-1)


price_vector_vc = []

if np.any(permut_econ_vc) == True:
    for j in VC_All:
        print("Enter price for %s product flow\n" % j)
        price = float(input())
        price_vector_vc.append(price)
        
else:
    price_vector_vc = 0

price_vector_eq = []

if np.any(permut_econ_equip) == True:
    for j in equip_All:
        print("Enter price for %s product flow\n" % j)
        price = float(input())
        price_vector_eq.append(price)    

else:
  price_vector_eq = 0

vc_eq_cutoff =  bar_X_bar[length_A-1:length_A-1+L,length_A-1+L:len(bar_X_bar)]
econ_eq_cutoff = bar_X_bar[0:length_A-1,length_A-1+L:len(bar_X_bar)]

econ_vc_cutoff = bar_X_bar[0:length_A-1,length_A-1:length_A-1+L]



new_V = V - np.matmul(np.matmul(permut_econ_vc,np.multiply(V_vc,price_vector_vc)),permut_vc_econ) - np.matmul(np.matmul(permut_econ_equip,np.multiply(X_eq,price_vector_eq)),permut_equip_econ)

new_V_vc = V_vc - np.matmul(np.matmul(permut_vc_equip,X_eq),permut_equip_vc)


new_U = U - np.matmul(np.matmul(permut_econ_vc,np.multiply(U_vc,price_vector_vc)),permut_vc_econ) - np.matmul(econ_vc_cutoff,permut_vc_econ) - np.matmul(econ_eq_cutoff,permut_equip_econ)  - np.matmul(np.matmul(permut_econ_equip,np.multiply(U_eq,price_vector_eq)),permut_equip_econ)  

new_U_vc = U_vc - np.matmul(np.matmul(permut_vc_equip,X_eq),permut_equip_vc) - np.matmul(vc_eq_cutoff,permut_equip_vc)

