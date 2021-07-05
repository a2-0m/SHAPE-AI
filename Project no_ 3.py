#!/usr/bin/env python
# coding: utf-8

# # Welcome to Jupyter!

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


# This repo contains an introduction to [Jupyter](https://jupyter.org) and [IPython](https://ipython.org).
# 
# Outline of some basics:
# 
# * [Notebook Basics](../examples/Notebook/Notebook%20Basics.ipynb)
# * [IPython - beyond plain python](../examples/IPython%20Kernel/Beyond%20Plain%20Python.ipynb)
# * [Markdown Cells](../examples/Notebook/Working%20With%20Markdown%20Cells.ipynb)
# * [Rich Display System](../examples/IPython%20Kernel/Rich%20Output.ipynb)
# * [Custom Display logic](../examples/IPython%20Kernel/Custom%20Display%20Logic.ipynb)
# * [Running a Secure Public Notebook Server](../examples/Notebook/Running%20the%20Notebook%20Server.ipynb#Securing-the-notebook-server)
# * [How Jupyter works](../examples/Notebook/Multiple%20Languages%2C%20Frontends.ipynb) to run code in different languages.

# You can also get this tutorial and run it on your laptop:
# 
#     git clone https://github.com/ipython/ipython-in-depth
# 
# Install IPython and Jupyter:
# 
# with [conda](https://www.anaconda.com/download):
# 
#     conda install ipython jupyter
# 
# with pip:
# 
#     # first, always upgrade pip!
#     pip install --upgrade pip
#     pip install --upgrade ipython jupyter
# 
# Start the notebook in the tutorial directory:
# 
#     cd ipython-in-depth
#     jupyter notebook
