
# coding: utf-8

# In[3]:


def exception_example():
    try:
        ans = 5/0
    except ZeroDivisionError:
        print("You cannot divide by 0")
        
exception_example()        
    

