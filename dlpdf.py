from urllib import parse
import urllib.request
import os
import requests

pdfurl = 'https://www1.hkexnews.hk/listedco/listconews/sehk/2020/0115/9129227/sehk19072200421.pdf'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}

# download pdf
#   set 1:  將rui 析分出需要保存的路徑path
#   set 2:  有了下載所需的 url和保存路徑,現在就需要進行保存的動作
def dlp(uri):
    url = parse.urlparse(uri)   # 分割 url:(scheme='https', netloc='www1.hkexnews.hk', path='/listedco/listconews/sehk/2020/0115/9129227/sehk19072200421.pdf', params='', query='', fragment='')
    folderpath , filename = os.path.split(url.path)   #   os.path.splith() 用於分割路徑和檔案名. 這裡再將 url.path 分割
    filepath = url.path.lstrip('/') # 刪移左邊的 "/"
    folderpath = folderpath.lstrip('/')
    print("folderpath: ", folderpath)
    print("filename: ",filename)
    print('filepath: ', filepath)
 
    if not os.path.isdir(folderpath):
        print('沒有文件夾:', folderpath)
        os.makedirs(folderpath)
    #set 2
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
    file = requests.get(uri, heardes=heardes)
    with open(filepath,'wb') as f:
        print('downloading: ', uri)
        print('save to: ', filepath)
        f.write(file.content)
    print(filepath, filename)

    

dlp(pdfurl)