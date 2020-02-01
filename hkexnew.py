import requests
import urllib.request
from urllib import parse
from lxml import etree
import os

# change_list def
def change_list(xpath_list, s = 1):
    xpath_list = [str(x) for x in xpath_list] # 在這裡將所有 list 中的元素轉為 str 型態
    xpath_list = [x.strip() for x in xpath_list if x.strip()!=''] # 刪除特殊字符,如 \n \t
  
    if s == 1:
      i = 0
      for x in xpath_list:
          xpath_list[i] = x[0:10]
          i = i +1
    return xpath_list


# Download def
#   只接受的係字串參數
#   uri是要下載的URL, filepath 是保存文件的路徑
def download(uri):
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
    # headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
    file = requests.get(uri)
    with open(filepath,'wb') as f:
        print('downloading: ', uri)
        print('save to: ', filepath)
        f.write(file.content)
    print(filepath, filename)

#   修改字串,主要用於修改 html
def changecontent(old_file, new_file, old_str, new_str):
    content = open(old_file)
    with open(new_file, 'w') as f:
        for line in content:
            f.write(line.replace(old_str,new_str))

    content.close


# get htm pdf link, retun list type
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