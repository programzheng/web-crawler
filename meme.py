import requests
from bs4 import BeautifulSoup
import json

#first get memeList
htmlUrl = 'https://memes.tw/wtf'
htmlDocument = requests.get(htmlUrl)
memeList = BeautifulSoup(htmlDocument.text, 'html.parser')

#限制從第一頁往後找尋頁數(-1為不限制)
LIMIT = -1
#限制從第一頁往後找尋頁數計數
LIMIT_COUNT = 0
#所有頁數連結
htmlUrls = []
#所有圖片連結
imgUrls = []
while htmlUrl is not None:
    LIMIT_COUNT+=1
    #當前頁面圖片連結
    memeDivs = memeList.findAll('div', class_='mb-3 border-bottom pb-3')
    for memeDiv in memeDivs:
        memeImg = memeDiv.find('img')
        imgUrls.append(memeImg['data-src'])
    #找下一頁
    htmlUrl = memeList.find('a', rel="next")['href']
    htmlDocument = requests.get(htmlUrl)
    memeList = BeautifulSoup(htmlDocument.text, 'html.parser')
    htmlUrls.append(htmlUrl)
    if LIMIT_COUNT >= 0 and LIMIT_COUNT == LIMIT:
        break
#寫入json
with open('imgs.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(imgUrls, jsonfile, indent=4)

# memeDivs = memeList.findAll('div', class_='mb-3 border-bottom pb-3')
# for memeDiv in memeDivs:
#     memeImg = memeDiv.find('img')
#     imgUrls.append(memeImg['data-src'])
# print(imgUrls)
print(htmlUrls, imgUrls)