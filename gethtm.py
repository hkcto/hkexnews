import requests
from lxml import etree

url = 'https://www1.hkexnews.hk/listedco/listconews/sehk/2020/0115/2019072200362.htm'

html = requests.get(url).text
html = etree.HTML(html)

pdf_link = html.xpath('//font[@type="uploadFile"]/a/@href')
print(pdf_link)

