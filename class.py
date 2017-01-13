
# coding: utf-8

# In[1]:

print(type(1))


# In[2]:

print(type([]))


# In[3]:

print(type(()))


# In[4]:

print(type({}))


# In[16]:

class Dog():
    species='human'
    
    def __init__(self, breed,name,age):
        self.breed = breed
        self.name = name
        self.age =age

sam = Dog('Lab','sam','10')
frank = Dog('huskie','frank','500')
john = Dog('chuahva','john','25')


# In[13]:

sam.age


# In[8]:

sam.breed


# In[10]:

john.breed


# In[14]:

john.age


# In[17]:

john.species


# In[18]:

list =(1,2,'a')


# In[20]:

print(list)


# In[21]:

len(list)


# In[ ]:




# In[ ]:



