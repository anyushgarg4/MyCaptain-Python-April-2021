#!/usr/bin/env python
# coding: utf-8

# In[3]:


print("Hello Sir")


# In[4]:


radius = input("Enter the radius of the circle for area : ")


# In[5]:


radius = float(radius)


# In[10]:


print(" The area of the circle is : ", 3.14*radius*radius)


# In[1]:


numbers = int(input("How Many Terms? "))


# In[2]:


n1, n2 = 0, 1
count = 0


# In[3]:


if numbers <=0:
    print("This works only when positive integer is entered.")
elif numbers==1:
    print("Fibonacci Sequence till " ,numbers,":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < numbers:
        print(n1)
        n = n1 + n2
        n1 = n2
        n2 = n
        count += 1
    
    


# In[ ]:




