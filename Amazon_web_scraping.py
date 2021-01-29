#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
# url = 'https://www.amazon.in/s?rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1389401031%2Cn%3A1389432031&page=2'
# req = Request(url , headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'})

# webpage = urlopen(req).read()
# page_soup = soup(webpage, "html.parser")
# print(page_soup.prettify())


# In[ ]:


mobilelinks=[]
for i in range(2,100):
  req = Request(f'https://www.amazon.in/s?rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1389401031%2Cn%3A1389432031&page={i}',headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'})
  webpage=urlopen(req).read()
  page_soup = soup(webpage, "html.parser")
  mobilelists=page_soup.find_all('div' ,class_='a-row a-size-base a-color-base')
  for item in mobilelists:
    for link in item.find_all('a',class_="a-size-base a-link-normal s-no-hover a-text-normal",href=True):
      mobilelinks.append(link['href'])


# In[ ]:


df=[]
for i in range(0,len(mobilelinks)):
  df.append("https://www.amazon.in/" + mobilelinks[i])
print(df)


# In[ ]:


# for i in range(0,len(df)):
links=[]
for i in range(0,len(df)):
  a=df[i].split('/')[5]
  links.append(df[i].replace(a,'product-reviews'))
links


# In[ ]:


Device_name=[]
review=[]

for l in range(0,400):
  main_url=links[l]
  p=0
  while (p<3):
    url2=main_url
    req1 = Request(url2,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'})
    webpage1=urlopen(req1).read()
    page_soup1 = soup(webpage1, "html.parser")
    reviews=(page_soup1.find_all('span' ,class_='a-size-base review-text review-text-content'))
    names=page_soup1.find('span' ,class_="a-list-item")
    for k in range(0,len(reviews)):
      review.append(reviews[k].get_text())
    h=0
    while h<len(reviews):
      Device_name.append(names.get_text())
      h=h+1
    url_new=(page_soup1.find_all('li',class_='a-last'))
    for item in url_new:
      for link in item.find_all('a',href=True):
          main_url=('https://www.amazon.in/' + link['href'])
    p=p+1


# In[ ]:


import csv
import pandas as pd


# In[ ]:


dict={"mobile name" : Device_name , "reviews" : review }


# In[ ]:


dict


# In[ ]:


from google.colab import files
df=pd.DataFrame(dict)
df.to_csv('df.csv')
files.download('df.csv')


# In[ ]:


for i in range(0,len(df)):
  df['mobile name'][i]=df['mobile name'][i].lstrip('\n')
  df['reviews'][i]=df['reviews'][i].strip('\n\n')
df
df.to_csv('df.csv')
files.download('df.csv')


# In[ ]:




