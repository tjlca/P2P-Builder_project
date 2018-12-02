
# coding: utf-8

# In[ ]:

import sys
import numpy as np

print ("Welcome to Eco-LCA")

rcond = None

"""Starting Counter for number of processes/network (can be changed with the length of any full list)"""

counter = 1

"""The count of levels in the chain being checked for input"""

level = 1

"""The list of processes still being checked for input"""

check = []

"""Starting a list of ( process, output name, output value)"""

out =[]

"""Starting a list of list of all (processes , output names, output values)"""

allPros =[]

"""Starting a list of lists of all (processes, input names, input values)"""

allIn = []

"""Environmental impact vector"""

F = []

allEnv = []

v_allEnv = []

res =[]

p = []


# In[2]:

print("Enter Model complexity/price limit")
epsilon = float(input())

print("Enter tolerance of iteration")
zeta = float(input())


pro = input ("Enter name of the final demand process/network:\n")

"""Adding the process into a list"""

out.append(pro)

print ("For %s, Enter:" % pro)

outName = input("Name of output:\n")

"""Adding the name of the put of the process to the list"""

out.append(outName)


"""Prompting the user to input the name of the final demand process/network then name of the output the value of the output"""

f_dem = float(input("Enter final demand:\n"))


dirt = {pro : counter}

print ("Flow of %s : " % outName)

outVal = float(input())

print ("Variance of flow: ")

v_outVal = float(input())

"""Adding the value of the output of the process"""

tec = np.zeros((1,1))

v_tec = np.zeros((1,1))

tec[(0,0)] = outVal

v_tec[(0,0)] = v_outVal

F.append(f_dem)

"""Adding the list made into a list of all lists"""

allPros.append(out)

"""Resetting the list for the next process"""

out = []

"""Asking for environmenal impact"""

print ("Environmental impact : ")
    
env = float(input())

allEnv.append(env)

tot_env = env

print ("Variance of environmental impact :")

v_env = float(input())

v_allEnv.append(v_env)

print ("Price of process :" )

price = float(input())

p.append(price)

Mc = np.sum(p)

check.append(pro)

"""@@@@@@@@@@@@@@@New edits@@@@@@@@@@@@@@@"""


S = np.linalg.solve(tec,F)

        
X_inv = np.linalg.inv(tec)
        
lamda = np.matmul(allEnv,X_inv)
    
alpha = np.matmul(X_inv,F)

unc1 = 0

unc2 = 0   
    
for i in range(0,counter):
    unc1 = (lamda[i]** 2) * v_allEnv[i] + unc1
        
for i in range(0,counter):
    for j in range(counter):
        unc2 = ((alpha[i] * lamda[j]))** 2 * v_tec[i,j] + unc2
        
res.append((unc1 + unc2)**(1/2))

print ("res = %f \n" % res[counter-1])


        
RSD = res[counter-1]/tot_env
        
curenv = env * S[-counter]
    
print ("The enveronmental impact of %s process is %f \n" % (pro,curenv))


RSD_old = RSD;

"""@@@@@@@@@@@@@@@End of new edits@@@@@@@@@@@@@@@"""

"""Looping through inputs of the processes"""

fail_counter = 0;
while level != 0 :
    
    
    old_X =tec
    old_M = allEnv
    old_F = F
    old_varX = v_tec
    old_varM = v_allEnv
    old_res = res
    old_p = p
    RSD_old = RSD
    old_Mc = Mc
    old_E = tot_env

    
    
    
    """Prompting user to enter the inputs for the process"""

    print ("Name of input to %s or leave blank to proceed : " % check[level - 1])
    
    inName = input()
    
    if inName != "":
        
        counter = counter + 1
        
        level = level + 1
               
    
        """Prompting the user for the value of the input"""
    
        print ("Flow of %s as input: " % inName)
    
        inVal = float(input())
    
        print ("Variance of flow of %s input: " % inName)
    
        v_inVal = float(input())
        
        
        print ("Price of process input is from:" )

        price = float(input())

        
        p.append(price)
        
        Mc = np.sum(p)
        
        if Mc > epsilon:
                tec = old_X 
                allEnv = old_M 
                F = old_F
                v_tec =  old_varX
                v_allEnv = old_varM
                res = old_res 
                p = old_p
                RSD = RSD_old
                Mc = old_Mc
                tot_env = old_E
                print("Model complexity has hit limit. Quitting algorithm")
                break;
        else:
            continue;
        
    
        """Asking for the name of the process the input is from"""
    
        print ("Enter name of the process outputing %s :" % inName)
    
        pro = input()
        
        dirt[pro] = (counter)
    
        """Asking for the output value of the current process """
        print ("For %s, enter: " % inName)
    
        print ("Flow of %s output:" % inName)
        
        outVal = float(input())
        
        print ("Variance of flow of %s output:" % inName)
        
        v_outVal = float(input())
        
        print ("Environmental impact :")
        
        env = float(input())
        
        allEnv.append(env)
        
        tot_env = env + tot_env
        
        print ("Variance of environmental impact :")
        
        v_env = float(input())
        
        v_allEnv.append(v_env)
        
        
        A = np.zeros((counter,counter))
        
        A[-tec.shape[0]:, -tec.shape[1]:] = tec
        
        tec = A
                
        tec[(0,0)] = outVal 
        
        tec[(0,-dirt[check[level-2]])] = (- inVal)
        
        v_A = np.zeros((counter,counter))

        
        v_A[-v_tec.shape[0]:, -v_tec.shape[1]:] = v_tec

        
        v_tec = v_A       

                
        v_tec[(0,0)] = v_outVal 
        

        
        v_tec[(0,-dirt[check[level-2]])] =  v_inVal
        

        
        F = np.append(0,F)
        
        """@@@@@@@@@@@@@@@@@@@@@@Enter New edits Here@@@@@@@@@@@@@@@@@@@@@@@@@@@"""
        S = np.linalg.solve(tec,F)
        
        X_inv = np.linalg.inv(tec)
        
        lamda = np.matmul(allEnv,X_inv)
    
        alpha = np.matmul(X_inv,F)

        unc1 = 0

        unc2 = 0   
    
        for i in range(0,counter):
            unc1 = (lamda[i]** 2) * v_allEnv[i] + unc1
        
        for i in range(0,counter):
            for j in range(0,counter):
                unc2 = ((alpha[i] * lamda[j]))** 2 * v_tec[i,j] + unc2
        
        res.append((unc1 + unc2)**(1/2))

        print ("res = %f \n" % res[counter-1])
        
        RSD = res[counter-1]/tot_env
        
        check.append(pro)
        
       
        if abs(RSD - RSD_old) > zeta:
             continue;
        else:
             print("Change in RSD is lower than tolerance\n")
             fail_counter = fail_counter+1;
             if fail_counter > 3:
                tec = old_X 
                allEnv = old_M 
                F = old_F
                v_tec =  old_varX
                v_allEnv = old_varM
                res = old_res 
                p = old_p
                RSD = RSD_old
                Mc = old_Mc
                tot_env = old_E
                break;
             else:
                 continue
        
        
        
        
        if RSD < RSD_old:
            print("RSD check as has passed")
            continue
            
        else:
            print("RSD check has failed\n")
            print("Do you want to keep currently entered data?\n")
            choice = input()
            if choice == "yes":
                continue;
            else:
                tec = old_X 
                allEnv = old_M 
                F = old_F
                v_tec =  old_varX
                v_allEnv = old_varM
                res = old_res 
                p = old_p
                RSD = RSD_old
                Mc = old_Mc
                tot_env = old_E
                print("Do you want to continue?")
                choice = input()
                fail_counter = fail_counter - 1;
                if choice == "yes":
                    check.pop()
                    level = level - 1
                    counter = counter - 1
                    continue;
                else:
                    break;
                   

            
    

        
    else:
        check.pop()
        level = level - 1
        

