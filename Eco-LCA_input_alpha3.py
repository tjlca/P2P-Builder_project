
# coding: utf-8

# In[ ]:


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


# In[2]:


"""Prompting the user to input the name of the final demand process/network then name of the output the value of the output"""

f_dem = input("Enter final demand:\n")

pro = input ("Enter name of the final demand process/network:\n")

"""Adding the process into a list"""

out.append(pro)

print ("For %s, Enter:" % pro)

outName = input("Name of output:\n")

"""Adding the name of the put of the process to the list"""

out.append(outName)

dirt = {pro : counter}

print ("Flow of %s : " % outName)

outVal = float(input())

print ("Variance of flow: ")

v_outVal = float(input())

"""Adding the value of the output of the process"""

tec = np.zeros((1,1))

v_tec = np.zeros((1,1))

tec[(0,0)] = outVal

v_tec[(0,0)] = v_tec

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

check.append(pro)

"""@@@@@@@@@@@@@@@New edits@@@@@@@@@@@@@@@"""

S = np.linalg.solve(tec,F)
        
X_inv = np.linalg.inv(tec)
        
lamda = np.matmul(allEnv,X_inv)
    
alpha = np.matmul(X_inv,F)

unc1 = 0

unc2 = 0   
    
for i in range(0,counter)
    unc1 = (lamda[i]** 2) * v_allEnv[i] + unc1
        
for i in range(0,conuter)
    for j in range(c0,ounter)
        unc2 = ((alpha[i] * lamda[j])** 2 * v_tec[i,j] + unc2
        
res.append((unc1 + unc2)**(1/2))

print ("res = %f \n" % res[counter-1])
        
RSD = res[counter-1]/tot_env
        
curenv = env * S[-counter]
    
print ("The enveronmental impact of %s process is %f \n" % (pro,curenv))

"""@@@@@@@@@@@@@@@End of new edits@@@@@@@@@@@@@@@"""

"""Looping through inputs of the processes"""

while level != 0 :
    
    
    """Prompting user to enter the inputs for the process"""

    print ("Name of input to %s or leave blank to proceed : " % check[level - 1])
    
    inName = input()
    
    if inName != "":
        
        counter = counter + 1
        
        level = level + 1
               
    
        """Prompting the user for the value of the input"""
    
        print ("Flow of %s : " % inName)
    
        inVal = float(input())
    
        print ("Variance of flow of %s : " % inName)
    
        v_inVal = float(input())
    
        """Asking for the name of the process the input is from"""
    
        print ("Enter name of the process outputing %s :" % inName)
    
        pro = input()
        
        dirt[pro] = (counter)
    
        """Asking for the output value of the current process """
        print ("For %s, enter:")
    
        print ("Flow of %s :" % inName)
        
        outVal = float(input())
        
        print ("Variance of flow of %s :" % inName)
        
        v_outVal = float(input())
        
        print ("Enveronmental impact :")
        
        env = float(input())
        
        allEnv.append(env)
        
        tot_env = env + tot_env
        
        print ("Variance of enveronmental impact :")
        
        v_env = float(input())
        
        v_allEnv.append(v_env)
        
        A = np.zeros((counter,counter))
        
        A[-tec.shape[0]:, -tec.shape[1]:] = tec
        
        tec = A
                
        tec[(0,0)] = outVal 
        
        tec[(0,-dirt[check[level-2]])] = (- inVal)
        
        v_A = np.zeros((counter,counter))
        
        v_A[-tec.shape[0]:, -tec.shape[1]:] = v_tec
        
        v_tec = v_A
                
        v_tec[(0,0)] = v_outVal 
        
        v_tec[(0,-dirt[check[level-2]])] = (- v_inVal)
        
        F = np.append(0,F)
        
"""@@@@@@@@@@@@@@@@@@@@@@Enter New edits Here@@@@@@@@@@@@@@@@@@@@@@@@@@@"""
        S = np.linalg.solve(tec,F)
        
        X_inv = np.linalg.inv(tec)
        
        lamda = np.matmul(allEnv,X_inv)
    
        alpha = np.matmul(X_inv,F)

        unc1 = 0

        unc2 = 0   
    
        for i in range(0,counter)
            unc1 = (lamda[i]** 2) * v_allEnv[i] + unc1
        
        for i in range(0,conuter)
            for j in range(0,counter)
                unc2 = ((alpha[i] * lamda[j])** 2 * v_tec[i,j] + unc2
        
        res.append((unc1 + unc2)**(1/2))

        print ("res = %f \n" % res[counter-1])
        
        RSD = res[counter-1]/tot_env
        
        curenv = env * S[-counter]
    
        print ("The enveronmental impact of %s process is %f \n" % (pro,curenv))
    
        check.append(pro)
        
    else:
        check.pop()
        level = level - 1
        

