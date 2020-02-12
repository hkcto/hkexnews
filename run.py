import hkexnew, wpxmlrpc, pyftp
import requests
import os
from lxml import etree

url = ['https://www1.hkexnews.hk/search/titlesearch.xhtml?lang=en',
      'https://www1.hkexnews.hk/search/titlesearch.xhtml?lang=zh']
# url= 'https://www1.hkexnews.hk/search/titlesearch.xhtml?lang=en'
# url_hk= 'https://www1.hkexnews.hk/search/titlesearch.xhtml?lang=zh'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
payload_eng = {
    'lang':'en',
    'category': '0',
    'market': 'SEHK',
    'searchType': '-1',
    'stockId': '1000016998',
    'from': '19990401',
    'to': '20201230'

}
payload_hk = {
    'lang':'zh',
    'category': '0',
    'market': 'SEHK',
    'searchType': '0',
    'stockId': '1000016998',
    'from': '19990401',
    'to': '20201230'

}

####################### 這裡是正式運行區 #################################

# 這裡是英文版
tablecode = hkexnew.spider(url[0], payload_eng)
wpxmlrpc.eidtpage(763, 'Announcements and Circulars', tablecode)

# 這裡是中文版
tablecode = hkexnew.spider(url[1], payload_hk)
wpxmlrpc.eidtpage(36, '公告及通函', tablecode)

# 這裡是上載區
pyftp.ftpupload()


########################## 這裡是測試區 ##################################
# # 這裡是英文版
# tablecode = hkexnew.spider(url[0], payload_eng)
# wpxmlrpc.eidtpage(1554, 'rpc_eng', tablecode)

# # 這裡是中文版
# tablecode = hkexnew.spider(url[1], payload_hk)
# wpxmlrpc.eidtpage(1559, 'rpc_hk', tablecode)



# 修改 wp page. id: 1559 是中文版的 1554 是英文版.
# id: 763 Announcements and Circulars
# id: 36 公告及通函
# wpxmlrpc.eidtpage(36, '公告及通函', tablecode)
# wpxmlrpc.eidtpage(763, 'Announcements and Circulars', tablecode)
#pyftp.ftpupload()

