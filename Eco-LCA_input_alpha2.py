
# coding: utf-8

# In[1]:


import numpy as np

print ("Welcome to Eco-LCA")

"""Starting Counter for number of processes/network (can be changed with the length of any full list)"""

counter = 1

"""Starting a list of ( process, output name, output value)"""

out =[]

"""Starting a list of list of all (processes , output names, output values)"""

allPros =[]


"""Starting a list of (process, input name, input value)"""

used =[] 

"""Starting a list of lists of all (processes, input names, input values)"""

allIn = []


# In[2]:


"""Prompting the user to input the name of the first process/network then name of the output the value of the output"""

pro = input ("Enter name of the first process/network:\n")

"""Adding the process into a list"""

out.append(pro)

print ("Enter name of output of %s : " % pro)

outName = input()

"""Adding the name of the put of the process to the list"""

out.append(outName)

print ("Enter value of %s outputed from %s : " % (outName, pro))

outVal = float(input())

"""Adding the value of the output of the process"""

out.append(outVal)

"""Adding the list made into a list of all lists"""

allPros.append(out)

"""Resetting the list for the next process"""

out = []

"""Prompting user to enter the inputs for the process"""

print ("Enter name of input of %s or leave blank to proceed : " % pro)

usedName = input()

"""Looping through inputs of the processes"""

while usedName != "":
    
    used = []
    
    """Assigning the list for input the name process"""
    
    used.append(pro)
    
    """Adding the name of input"""
    
    used.append(usedName)
    
    """Prompting the user for the value of the input"""
    
    print ("Enter value of %s inputed into %s : " % (usedName, pro))
    
    usedVal = float(input())
    
    """Adding the value to the list"""
    
    used.append(usedVal)
    
    """Adding the list to a list of all lists of inputs"""
    
    allIn.append(used)
    
    print ("Enter name of input of %s or leave blank to proceed : " % pro)
    
    usedName = input()

pro = input("Enter name of next process or leave blank if all processes/networks are inputed:\n")


# In[3]:


"""Run loop until user leaves the process name blank"""

while (pro !=""):
    counter += 1

    print ("Enter name of output of %s : " % pro)

    outName = input()

    print ("Enter value of %s outputed from %s : " % (outName, pro))

    outVal = float(input())
    
    out.append(pro)
    out.append(outName)
    out.append(outVal)
    
    allPros.append(out)
    
    out = []
    
    print ("Enter name of input of %s or leave blank to proceed : " % pro)

    usedName = input()

    while usedName != "":
        used = []
    
        used.append(pro)
    
        used.append(usedName)
    
        print ("Enter value of %s inputed into %s : " % (usedName, pro))
    
        usedVal = float(input())
    
        used.append(usedVal)
    
        allIn.append(used)
    
        print ("Enter name of input of %s or leave blank to proceed : " % pro)
        
        usedName = input()
    
    pro = input("Enter name of next process or leave blank if all processes/networks are inputed:\n")
    


# In[4]:


"""Creating a square zeros matrix with dimantions counter for the outputs """

make = np.zeros((counter,counter))

"""Making the outputs the diagonal of the square matrix """
for i in range(counter):
    make[i,i] = allPros[i][2]
    


# In[5]:


"""Creating a square zeros matrix with dimantions counter for the intputs """
use = np.zeros((counter,counter))

"""Running through the list of inputs"""
for j in range(len(allIn)):
    
    """Checking the process name to find the column number"""
    for k in range(counter):
        
        if allIn[j][0] == allPros[k][0]:
            
            """Checking the input to find the row"""
            for l in range(counter):
                
                if allIn[j][1] == allPros[l][1]:
                    """Assigning the input in it's place in the matrix"""
                    use[l,k] = allIn[j][2]


# In[6]:


"""Making the tecnology matrix"""
tec_mat = make - use

print (tec_mat)


# In[7]:


"""Making the flow rate matrix"""
f = np.zeros((counter,1))

"""Asking for the main flow"""

mainFlow = input("Enter the name the main process : \n")

"""Asking for the main flow rate for that process"""

print ("Enter flow rate of %s required : " % mainFlow)

mainVal = input()

"""Finding the postion of the main flow"""
for i in range(counter):
    
    if mainFlow == allPros[i][0]:
        
        """Assigning the flow rate to the matrix"""
        f[i] = mainVal


# In[8]:


"""Making an environmental row """
env = np.zeros(counter)

"""Prompting the user to enter the environmental impact of each process"""

for i in range(counter):
    print ("Enter the environmental impact of %s : " % allPros[i][0])
    
    env[i] = input()
    


print("Final Environmental Impact\n")
print(np.matmul(env,np.matmul(np.linalg.inv(tec_mat),f)))
