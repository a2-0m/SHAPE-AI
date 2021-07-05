#!/usr/bin/env python
# coding: utf-8

# In[1]:


import hashlib

text =input("Enter text : ")
salt = "abc"
hash_object = hashlib.md5(text.encode())
md5_hash = hash_object.hexdigest()
hash = hashlib.md5((salt + text).encode()).hexdigest()
print ("the hexadecimal equivalent of hash is :")
print(hash)

print ("\nthe hexadecimal equivalent of hash with salt is :")
print(md5_hash)

hash_object1 = hashlib.md5(md5_hash.encode())
md5_hash1 = hash_object1.hexdigest()
print ("\nthe hexadecimal equivalent of iteretion 1 hash with salt is :")
print(md5_hash1)

hash_object2 = hashlib.md5(md5_hash1.encode())
md5_hash2 = hash_object2.hexdigest()
print ("\nthe hexadecimal equivalent of iteretion 2 hash with salt is :")
print(md5_hash2)


# In[ ]:




