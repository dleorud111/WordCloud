#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt


# In[7]:


# txt파일 불러오기
result = ""
for number in range(1, 14):
    index = '{:02}'.format(number)
    filename = "Sequence_" + index + ".txt"
    text = open('./'+filename, 'r', encoding='utf-8-sig')
    result += text.read().replace("\n", " ")

result


# In[8]:


# 정규식으로 특수문자 제거
import re

pattern = '[^\w\s]'
text = re.sub(pattern, repl='', string=result)
text


# In[9]:


import matplotlib.font_manager as fm

for f in fm.fontManager.ttflist:
    if 'Gothic' in f.name:
        print(f.fname)
        


# In[13]:


font_path = 'C:\WINDOWS\Fonts\malgunsl.ttf'
wc = WordCloud(font_path=font_path, background_color="white")
wc.generate(text)
plt.figure(figsize=(50,50))
plt.axis("off")
plt.imshow(wc)
plt.show()


# In[16]:


# Generate a word cloud image
mask = np.array(Image.open('./sparta.png'))
wc = WordCloud(font_path=font_path, background_color="white", mask=mask)
wc.generate(text)

f = plt.figure(figsize=(50,50))
f.add_subplot(1,2, 1)
plt.imshow(mask, cmap=plt.cm.gray)
plt.title('Original Stencil', size=40)
plt.axis("off")

f.add_subplot(1,2, 2)
plt.imshow(wc, interpolation='bilinear')
plt.title('Word Cloud', size=40)
plt.axis("off")
plt.show()


# In[18]:


mask = np.array(Image.open('./sparta.png'))
wc = WordCloud(font_path=font_path, background_color="white", mask=mask)
wc.generate(text)

f = plt.figure(figsize=(50,50))
plt.imshow(wc, interpolation='bilinear')
plt.title('나만의 워드 클라우드', size=40)
plt.axis("off")
plt.show()
f.savefig('./myWordCloud.png')


# In[ ]:




