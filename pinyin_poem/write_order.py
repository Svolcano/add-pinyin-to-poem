# -!- coding: utf-8 -!-
import re
import requests
import time
import os
from tqdm import tqdm

def craw(chinese):
    url='http://hanyu.baidu.com/s?wd=%s&ptype=zici'%chinese
    header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
    }
    imagename='E:/6000汉字笔顺/'+chinese+'.gif'
    if os.path.exists(imagename):
        return 
    response = requests.get(url, headers=header)
    html = response.text
    imgs = re.compile(r'data-gif="(.+?\.gif)"').findall(html)
    for img in imgs:
        imageurl=img
        try:
            response = requests.get(imageurl)
            img = response.content
            with open(imagename,'wb' ) as f:
                f.write(img)
        except:
            print(chinese+' failure')

    

with open('hanzi.txt', 'r', encoding='utf-8') as rh:
    strs = rh.read().strip()
strs = list(strs)
print(len(strs))
for st in tqdm(strs):
    craw(st)