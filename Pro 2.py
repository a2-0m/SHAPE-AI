#!/usr/bin/env python
# coding: utf-8

# In[1]:


import hashlib

text = input("Enter your text : ")
hash_object1 = hashlib.md5(text.encode())
hash_object2 = hashlib.sha1(text.encode())
hash_object3 =hashlib.blake2b(text.encode())
print ("the hexadecimal equivalent of hash is :")
md5_hash = hash_object1.hexdigest()
sha1_hash = hash_object2.hexdigest()
blake2b_hash = hash_object3.hexdigest()

print(md5_hash)
print(sha1_hash)
print(blake2b_hash)


# In[ ]:




