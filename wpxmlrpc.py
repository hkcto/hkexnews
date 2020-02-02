from wordpress_xmlrpc import Client, WordPressPage
from wordpress_xmlrpc import WordPressPage
from wordpress_xmlrpc.methods import posts

id = 'ctr'
pwd = '#01UbRoTFru!luB#v('
url = 'http://ctr.finasia-group.com/xmlrpc.php'

def eidtpage(pageid, title, content):
    wp = Client(url, id, pwd)
    page = WordPressPage()
    page.title = title
    page.content = content
    wp.call(posts.EditPost(pageid, page))

eidtpage(1559, 'rpc_hk' ,'this is not change title')