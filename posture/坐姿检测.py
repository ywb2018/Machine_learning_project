
# coding: utf-8

# In[98]:


import numpy as np
import pandas as pd
import os


# In[99]:


data_location = 'E:/Dataset/posture/'
texts = os.listdir(data_location)
texts[:3]


# ### 解析文件，构造矩阵

# In[100]:


#sensor1 -- sensor2 --s3 -- s4 --s5 -- s6 --s7 -- s8 --s9 -- s10 -- 名字 -- 坐姿

def text2matrix(filename):
    with open(data_location+filename) as f:
        str1 = f.readlines()
    length = len(str1)
    matrix = np.zeros((length,10))
    
    
#--------------------矩阵解析-----------------------------------------------   
    for i,line in enumerate(str1):
        if i<1:continue;#解决第一行是空行的情况
        num = np.reshape(str1[i].strip('\t\n').split('\t'),(1,-1)).shape[1] #得到行数
        if(num != 10):
            matrix[i,:num] = np.array(str1[i].strip('\t\n').split('\t'))
        else:
            matrix[i] = np.array(str1[i].strip('\t\n').split('\t'))
    handled_matrix = matrix[2:-3,:] # 去掉前2行和后3行后的矩阵
#--------------------矩阵解析-----------------------------------------------     


#--------------------label解析-----------------------------------------------  
    lab_dict = {'tuobei' :1,
                'youbian':2,
                'youpian':2,
                'zuobian':3,
                'zuopian':3,
                'zuozhi' :4}
    #根据文件名解析 特征：人 和 label
    if(filename.split('.')[0].isalpha()==False): #如果有数字
        if(filename.split('.')[0][:-1].isalpha() ==False): #进一步判断是2个数字？
            label = filename.split('.')[0][3:-2]         #如果是2个数字，就取最后两个数字之前的字母
        else:#只有一个数字
            label = filename.split('.')[0][3:-1]
    else:
        label = filename.split('.')[0][3:]
#-------------------label解析----------------------------------------------
        
#-------------------姓名解析----------------------------------------------  
    name_dict= {'cwb':1,
                'tsy':2,
                'wlj':3}
    lab_column = np.ones((handled_matrix.shape[0],1))*lab_dict[label]
    nam_column = np.ones((handled_matrix.shape[0],1))*name_dict[ filename[:3]]
    new_matrix = np.column_stack((handled_matrix,nam_column))
    matrix = np.column_stack((new_matrix,lab_column))
    
    rand_index = np.random.choice(matrix.shape[0],6,replace=False) # 抽取6个数据，四个用来训练，2个用来测试
    train_matrix = matrix[rand_index[:5]][:]
    test_matrix  = matrix[rand_index[5:]][:]
    
    return train_matrix,test_matrix


# ### 构造训练集和测试集

# In[101]:


train_matrix = np.zeros((len(texts),5,12))
test_matrix  = np.zeros((len(texts),1,12))
def construct_dataset():
    for i,file_name in enumerate(texts):
        train_matrix[i],test_matrix[i] = text2matrix(file_name) #获得每个文件里的矩阵
    
    return train_matrix.reshape(-1,12),test_matrix.reshape(-1,12) #比较trick的一步


# In[102]:


train,test = construct_dataset()
np.random.shuffle(train)
np.random.shuffle(test)
colum = ['sensor1','sensor2','sensor3','sensor4','sensor5','sensor6','sensor7','sensor8','sensor9','sensor10','Name','Posture']


# In[103]:


train_df = pd.DataFrame(train,columns=colum)
test_df  = pd.DataFrame(test, columns=colum)


# In[104]:


train_df.to_csv('C:/Users/ywb/Desktop/data/train_df.csv')
test_df.to_csv('C:/Users/ywb/Desktop/data/test_df.csv')

