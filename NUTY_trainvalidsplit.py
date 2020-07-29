#!/usr/bin/env python
# coding: utf-8

# # Script to move certain number of files into two folders train and valid
# 
# Script written as a part of NUTY dataset creation

# Library imports

# In[44]:


from pathlib import Path
import os 
import shutil


# Reading all the image files

# In[46]:


path_to_files = Path(input("Enter absolute file path to directory"))
path_to_split = Path(input("Enter absolute file path to directory containing split files, directory need not exist, make sure it is not the same directory as above"))
path_to_split.mkdir(exist_ok=True)
all_files = path_to_files.iterdir()
list(all_files)


# Creating train and valid directory

# In[47]:


path_to_train = path_to_split/"train"
path_to_train.mkdir(exist_ok=True)


# In[48]:


path_to_test = path_to_split/"test"
path_to_test.mkdir(exist_ok=True)


# In[49]:


counter=0
for image in path_to_files.iterdir():
    counter +=1 
    if counter % 9 == 0:
        shutil.move(str(image), str(path_to_test))
    else:
        shutil.move(str(image), str(path_to_train))
        


# In[ ]:




