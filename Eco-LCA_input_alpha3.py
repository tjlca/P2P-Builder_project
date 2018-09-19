
# coding: utf-8

# In[30]:


import numpy as np

print ("Welcome to Eco-LCA")

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

"""Starting the Tecnology matrix"""

tec = []

"""Environmental impact vector"""

env =[]


# In[31]:


"""Prompting the user to input the name of the final demand process/network then name of the output the value of the output"""

pro = input ("Enter name of the final demand process/network:\n")

"""Adding the process into a list"""

out.append(pro)

print ("Enter name of output of %s : " % pro)

outName = input()

"""Adding the name of the put of the process to the list"""

out.append(outName)

print ("Enter value of %s outputed from %s : " % (outName, pro))

outVal = float(input())

"""Adding the value of the output of the process"""

tec.append(outVal)

"""Adding the list made into a list of all lists"""

allPros.append(out)

"""Resetting the list for the next process"""

out = []

"""Asking for environmenal impact"""

print ("Enter the environmental impact of %s : " % pro)
    
env.append(input())

check.append(pro)

"""Looping through inputs of the processes"""

while level != 0 :
    
    
    """Prompting user to enter the inputs for the process"""

    print ("Enter name of input of %s or leave blank to proceed : " % check[level - 1])
    
    inName = input()
    
    if inName != "":
        
        level = level + 1
               
    
        """Prompting the user for the value of the input"""
    
        print ("Enter value of %s inputed into %s : " % (inName, check[level-2]))
    
        useVal = float(input())
    
        """Asking for the name of the process the input is from"""
    
        print ("Enter name of the process outputing %s :" % inName)
    
        pro = input()
    
        """Asking for the output value of the current process """
    
        print ("Enter value of %s outputed by %s :" % (inName, pro))
        
        outVal = input()
        
        a = np.zeros(counter,1)
        
        tec = [a] + tec
        
        check.append(pro)
        
        counter = counter + 1
        
    else:
        check.pop()
        level = level - 1
        


# In[33]:


counter


# In[35]:


a = 0

tec = [a] + tec

tec

