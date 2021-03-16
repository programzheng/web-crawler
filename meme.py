import requests
from bs4 import BeautifulSoup

htmlUrl = 'https://memes.tw/wtf'
htmlDocument = requests.get(htmlUrl)
memeList = BeautifulSoup(htmlDocument.text, 'html.parser')

memeDivs = memeList.findAll('div', class_='mb-3 border-bottom pb-3')
imgUrls = []
for memeDiv in memeDivs:
    memeImg = memeDiv.find('img')
    imgUrls.append(memeImg['data-src'])