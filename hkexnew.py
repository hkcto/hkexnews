import requests
import urllib.request
from urllib import parse
from lxml import etree
import os

log = []
if os.path.isfile('savelog.txt'):
  with open('savelog.txt', 'r') as f:
    for line in f:
      log.append(line.strip())




def spider(url, payload, title):
    # post 請求
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
    r = requests.post(url, payload, headers=header)
    html = r.text
    html = etree.HTML(html) # 生成一個 xpath 解釋對像

    # 發表時間
    release_time = html.xpath('//td[@class="text-right release-time"]/text()')
    release_time= change_list(release_time) # 這行係為了刪除空白或無用的字符的list元素
    # print("release time: \n", release_time)

    #   table headline 文件標題
    doc_headline = html.xpath('//div[@class="headline"]/text()')
    doc_headline = change_list(doc_headline, s= 0)
    # print('doc_headline', doc_headline)

    # document content 文件說明.
    doc_content = html.xpath('//div[@class="doc-link"]/a/text()')
    doc_content = change_list(doc_content,s=0)
    # print("doc_content\n",doc_content)

    # a href a 文件超連結
    doc_link = html.xpath('//div[@class="doc-link"]/a/@href')
    doc_link_new = html.xpath('//div[@class="doc-link"]/a/@href')
    # print("doc_link\n",doc_link)
    hkexnews_link = 'https://www1.hkexnews.hk'

    # 判斷 a href 是什麽類型 pdf or htm. pdf 就要下載, htm　就需進一步爬取和分析
    # pdf_uri 用來保存所有需要下載的 pdf 檔案
    # htm_uri 用來保存需要再次分析的 url
    pdf_uri = []
    htm_uri = []
    i = 0
    for u in doc_link:
        filetype = os.path.splitext(u)[1]  # os.path.splitext() 可以分離出檔案的名和後綴
    if filetype == '.pdf':
        link = hkexnews_link + u
        pdf_uri.append(link)
        #print("pdf_uri 添加了: ", link)
    elif filetype == '.htm':
        link = hkexnews_link + u
        htm_uri.append(link)
        #print("htm_uri 添加了:", link)
        pdf_uri.extend(gethtmpdf(link))
        # 在這裡直接下載 htm 文件,有別於pdf集中下戴
        if link not in log:
            download(link)
            with open('savelog.txt', 'a') as f:
                f.write('\n' + link)
        else:
            print('己存在:  ', link)
    else:
        pass
    i = i+1


    #   將 a href 和 hkexnews link 合併,得到完整的 pdf URI,有了完整的URL才能下載其PDF檔
    # i = 0
    # for s in doc_link:
    #   doc_link[i] = hkexnews_link + s
    #   i = i+1


    # 執行下載文件
    i = 0
    for u in pdf_uri:
        if u not in log:
            download(pdf_uri[i])
            with open('savelog.txt', 'a') as f:
                f.write('\n' + u)
                i = i+1
        else:
            print('己存在:  ', u)


    # 用於生成 html code
    str = """<tr><td class="td-date">{date}</td><td><div class="headline">{document}</div><div class="doc-link"><a href={doc_link} style="text-decoration:none;">{doc_link_content}</a></div></td></tr>\n"""
    tablecode = ""
    i = 0
    for s in release_time:
        # print(str.format(date=s))
        tablecode = tablecode + str.format(date=s, document=doc_headline[i], doc_link=doc_link_new[i], doc_link_content=doc_content[i])
        i = i+1



    tablecode = '<div style="width:15%;display:inline-block;"></div><div id="table-div" style="display:inline-block"><table><thead><th style="border:0;">Date</th><th style="border:0;">Document</th></thead>' + tablecode + '</table></div>'
    headercode = """<section id="banner"></div><div style="width:10%;display:inline-block"></div><h2 style="display:inline-block">{title}</h2></section>\n""".format(title=title)
    tablecode = headercode + tablecode

    return tablecode




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