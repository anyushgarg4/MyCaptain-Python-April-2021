


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




