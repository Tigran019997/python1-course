#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Homework  Harutyunyan  Tigran


# In[ ]:


#problem 1


# In[ ]:


s1="This  text  is  a  simple   text"
print(s1.replace("text","image"))


# In[ ]:


#problem 2


# In[6]:


import time
import calendar
import datetime


# In[ ]:


#problem 2.1


# In[19]:


bd = datetime.date(1984, 2, 1)


# In[ ]:


#problem 2.2


# In[21]:


print('Year: ', bd.year, type(bd.year))


# In[ ]:


#problem 2.3


# In[22]:


print('Month: ', bd.month)


# In[ ]:


#problem 2.4


# In[23]:


print('Day: ', bd.day)


# In[ ]:


#problem 2.5


# In[24]:


print('Day of the week (version 1): ', bd.isoweekday())


# In[ ]:


#problem 2.5


# In[27]:


bd = datetime.date(1984, 2, 1)
tday = datetime.date.today()
print(tday-bd)


# In[ ]:


#problem 2.6


# In[28]:


cal = calendar.month(2017, 5)
print ("Here is the calendar:")
print(cal)


# In[ ]:


#problem 2.7


# In[29]:


today = datetime.date.today()
one_day = datetime.timedelta(days = 1)
yesterday = today - one_day
tomorrow = today + one_day
print('Yesterday : ',yesterday)
print('Today : ',today)


# In[ ]:


#problem 2.8


# In[30]:


print('Yesterday : ',yesterday)
tdelta = datetime.timedelta(days = 2)
print(type(tdelta))
print('yesterday + 2 days: ',yesterday + tdelta, type(tday + tdelta))


# In[ ]:


#problem 2.9


# In[31]:


print('Yesterday : ',yesterday)
tdelta = datetime.timedelta(days = 2)
print(type(tdelta))
print('yesterday - 3 days: ',yesterday - tdelta, type(tday + tdelta))


# In[ ]:


#Problem 3.1


# In[235]:


a = [1, 4, 5, 7, 8, -2, 0, -1]


# In[158]:


#Problem 3.2


# In[206]:


a[2],a[4]


# In[ ]:


#Problem 3.3


# In[207]:


print('a= ',a, '\n')
a.sort(reverse = True)
print(a)


# In[210]:


a_sorted=sorted(a,reverse = True)
a_sorted


# In[ ]:


#problem 3.4


# In[218]:


print(a_sorted[0:3]) 
print(a_sorted[1:7])


# In[ ]:


#problem 3.5


# In[221]:


del a_sorted[2:4]


# In[ ]:


#problem 3.6


# In[222]:


a_sorted


# In[ ]:


#problem 3.7


# In[230]:


b = ["grapes", "Potatoes",  "tomatoes",  "Orange",  "Lemon",  "Broccoli",  "Carrot", "Sausages"] 


# In[231]:


b


# In[ ]:


#problem 3.8


# In[238]:


print('b= ',b, '\n')
b.sort()
print(b)


# In[ ]:


#problem 3.9


# In[240]:


c = a[0:3]+b[3:6]


# In[ ]:


#problem 3.10


# In[241]:


c


# In[ ]:


#problem 4


# In[273]:


market = {'dairy':['yogurt','cheese'],'fruits':['banana','apple','orange','lemon','apple','banana','banana']}


# In[274]:


market


# In[275]:


market['candies'] =['mars', 'kinder', 'twix']


# In[276]:


market


# In[277]:


market['fruits'].sort()


# In[278]:


market


# In[279]:


del market['fruits'][0]


# In[280]:


market


# In[281]:


del market['fruits'][1]


# In[282]:


market


# In[283]:


del market['fruits'][1]


# In[284]:


market


# In[ ]:




