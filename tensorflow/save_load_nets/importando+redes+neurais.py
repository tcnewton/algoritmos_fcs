
# coding: utf-8

# In[36]:


import os
import tensorflow as tf


# In[37]:


tf.reset_default_graph()


# ### Importando Redes Neurais

# In[52]:


path1 = os.getcwd()
os.chdir ('save')
path2 = os.getcwd()
with tf.Session() as sess:
    saver = tf.train.import_meta_graph(os.path.join(path2, 'teste_save.meta'))
    saver.restore(sess, tf.train.latest_checkpoint('./'))
    graph = tf.get_default_graph()
os.chdir (path1)


# #### Garantindo que retornou ao diretorio original

# In[51]:


print (os.getcwd())


# In[50]:


os.chdir ('..')

