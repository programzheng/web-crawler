import requests
from bs4 import BeautifulSoup
import json
import pathlib

#first get memeList
htmlUrl = 'https://memes.tw/wtf'
htmlDocument = requests.get(htmlUrl)
memeList = BeautifulSoup(htmlDocument.text, 'html.parser')

#JSON檔案名稱
JSON_FILE_NAME='meme-imgs.json'
#jsonFile
jsonFilePath = pathlib.Path(JSON_FILE_NAME)
#限制從第一頁往後找尋頁數(-1為不限制)
PAGE_LIMIT = -1
#頁數計數
PAGE_COUNT = 0
#分塊寫入json需小於PAGE_LIMIT(-1為不分塊)
PAGE_CHUNK_SIZE = 50
#所有頁數連結
htmlUrls = []
#所有圖片連結
imgUrls = []
while htmlUrl is not None:
    #當前頁面圖片連結
    memeDivs = memeList.findAll('div', class_='mb-3 border-bottom pb-3')
    for memeDiv in memeDivs:
        memeImg = memeDiv.find('img')
        imgUrls.append(memeImg['data-src'])
    #找下一頁
    htmlUrl = memeList.find('a', rel="next")['href']
    if htmlUrl is None:
        break
    htmlDocument = requests.get(htmlUrl)
    memeList = BeautifulSoup(htmlDocument.text, 'html.parser')
    htmlUrls.append(htmlUrl)
    if PAGE_CHUNK_SIZE >= 0 and PAGE_COUNT % PAGE_CHUNK_SIZE == 0:
        #檢查json檔案存在
        if jsonFilePath.exists():
            with jsonFilePath.open() as jsonFile:
                imgUrls = imgUrls + json.load(jsonFile)
                #寫入json
                with jsonFilePath.open('w', encoding='utf-8') as jsonFile:
                    json.dump(imgUrls, jsonFile, indent=4)
                    #清除已寫入的imgUrl
                    imgUrls.clear()
        else:
            #寫入新檔案json
            with jsonFilePath.open('w', encoding='utf-8') as jsonFile:
                json.dump(imgUrls, jsonFile, indent=4)
                #清除已寫入的imgUrl
                imgUrls.clear()
                
    if PAGE_COUNT >= 0 and PAGE_COUNT == PAGE_LIMIT:
        break
    PAGE_COUNT+=1

if PAGE_CHUNK_SIZE == -1:
    #寫入json
    with jsonFilePath.open('w', encoding='utf-8') as jsonFile:
        json.dump(imgUrls, jsonFile, indent=4)
        #清除已寫入的imgUrl
        imgUrls.clear()