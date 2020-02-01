import requests
from lxml import etree
import os

url1 = 'https://www1.hkexnews.hk/listedco/listconews/sehk/2020/0115/2019072200362.htm'
url2 = 'https://www1.hkexnews.hk/listedco/listconews/sehk/2020/0114/2020011400044.htm'

# get htm pdf rui
def gethtmpdf(url):

    html = requests.get(url).text
    html = etree.HTML(html)

    #   os.path.split() 可以分開檔案的路徑和名稱
    p, n= os.path.split(url)
    pdf_link = html.xpath('//font[@type="uploadFile"]/a/@href')
    i = 0
    pdf_url = []
    for link in pdf_link:
        pdf_url.append(p + '/' + link)
        i= i+1

    return(pdf_url)

pdf_list = gethtmpdf(url2)
print(pdf_list)

