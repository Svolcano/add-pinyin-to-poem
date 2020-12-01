# -!- coding: utf-8 -!-
import re
import requests
import time
import os

def craw(chinese):
    url='http://hanyu.baidu.com/s?wd=%s'%chinese
    print(chinese)
    header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
    }
    serverError=True
    while serverError:
        try:
            imagename='./dest/'+chinese+'.gif'
            if os.path.exists(imagename):
                return 
            response = requests.get(url, headers=header)
            html = response.text
            imgs = re.compile('data-gif="(.+?\.gif)"').findall(html)
            for img in imgs:
                imageurl=img
                try:
                    response = requests.get(imageurl)
                    img = response.content
                    with open(imagename,'wb' ) as f:
                        f.write(img)
                except:
                    print(chinese+' failure')
            serverError=False
        except:
            print(chinese+'server error')
            time.sleep(40)
    

with open('hanzi.txt', 'r', encoding='utf-8') as rh:
    strs = rh.read().strip()
strs = list(strs)
print(len(strs))
for st in strs:
    craw(st)