#!/usr/bin/env python
# coding: utf-8

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
    
    


# In[5]:





# In[6]:


for num in range(5):
    print(i)


# In[7]:


print(num)


# In[8]:


for num in range(5):
    print(num)


# In[9]:


for num in range(1, 14)


# In[10]:


for num in range(1 ,14):
    print(num)


# In[11]:


for num in range(-12, 14):
    print(num)


# In[14]:


start = int(input("Enter the start of range : "))
end = int(input("Enter the end of range : "))


# In[15]:


for num in range(start, end + 1):
    if num>=0:
        print(num, end = " ")


# In[18]:


for i in range(-12, 20):
    if i>=0:
        print(i)


# In[19]:


print(i)


# In[20]:


for i in range(-12, 20):
    print(i)


# In[22]:


def most_frequent(string):
    d = {}
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
            return d


# In[23]:


print most_frequent("Mississippi")


# In[24]:


def most_frequent(string):
    d = {}
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
            return d


# In[25]:


def most_frequent(string):
    d = {}
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
            return d
        
print(most_frequent("Mississippi")        


# In[27]:


def most_frequent(string):
    dict = {}
    for n in string:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict

print(most_frequent('Mississippi'))
        


# In[ ]:




