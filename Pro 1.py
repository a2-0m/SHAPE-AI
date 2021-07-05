#!/usr/bin/env python
# coding: utf-8

# In[1]:


import hashlib

text = input("Enter your text : ")
hash_object = hashlib.md5(text.encode())
print ("the hexadecimal equivalent of hash is :")
md5_hash = hash_object.hexdigest()
print(md5_hash)


# In[ ]:




