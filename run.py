import hkexnew
import requests
import os
from lxml import etree


# 讀取 log 
if os.path.isfile('savelog.txt'):
  log = []
  with open('savelog.txt', 'r') as f:
    for line in f:
      log.append(line.strip())


url = 'https://www1.hkexnews.hk/search/titlesearch.xhtml?lang=en'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
payload = {
    'lang':'en',
    'category': '0',
    'market': 'SEHK',
    'searchType': '-1',
    'stockId': '1000016998',
    'from': '19990401',
    'to': '20201230'

}


# post 請求
r = requests.post(url, payload, headers=headers)
html = r.content
html = etree.HTML(html) # 生成一個 xpath 解釋對像

#   table headline
document = html.xpath('//div[@class="headline"]/text()')
headline = hkexnew.change_list(document, s= 0)
# print(headline)


# 發表時間
table_time = html.xpath('//td[@class="text-right release-time"]/text()')
table_time_new = hkexnew.change_list(table_time)
# print(table_time_new)


# document content 文件說明.
doc_content = html.xpath('//div[@class="doc-link"]/a/text()')
doc_content_new = hkexnew.change_list(doc_content,s=0)
# print(doc_content_new)

# a href a 超連接
doc_link = html.xpath('//div[@class="doc-link"]/a/@href')
doc_link_new = html.xpath('//div[@class="doc-link"]/a/@href')
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
    pdf_uri.extend(hkexnew.gethtmpdf(link))
    # 在這裡直接下載 htm 文件,有別於pdf集中下戴
    if link not in log:
      hkexnew.download(link)
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
    hkexnew.download(pdf_uri[i])
    with open('savelog.txt', 'a') as f:
      f.write('\n' + u)
    i = i+1
  else:
    print('己存在:  ', u)


# # 用於生成 html code
# str = """<tr><td>{date}</td><td><div class="headline">{document}</div><div class="doc-link"><a href={doc_link}>{doc_link_content}</a></div></td></tr>\n"""
# tablecode = ""
# i = 0
# for s in table_time_new:
#     # print(str.format(date=s))
#     tablecode = tablecode + str.format(date=s, document=headline[i], doc_link=doc_link_new[i], doc_link_content=doc_content_new[i])
#     i = i+1
# # print(tablecode)

# #hkexnew.changecontent('announcements.html','a2.html','Content',tablecode )

    