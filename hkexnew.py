import requests
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
def download(uri, filepath):

    f_name = filepath.split('/')[-1] # f_name 得到的值是 202001140085.pdf, 也就是檔案名
    filepath = filepath.lstrip('/')
    
    # strip() 去除字符串的頭尾字符(默認為空格和換行符),只能去除頭尾,不能去除中間部分的字符
    #   lstrip() 去除字符串開頭的字符(默認為空和,換行,制表符)
    folderpath = filepath.strip(f_name) # 移除檔案名,得到文件夾 path
    folderpath = folderpath.lstrip('/')      #  去除開頭的 '/' 字符,使其成為相對路徑.



    if not os.path.isdir(folderpath):
        os.makedirs(folderpath)

    file = requests.get(uri)
    with open(filepath,'wb') as f:
        print('downloading: ', uri)
        print('save to: ', filepath)
        f.write(file.content)

#   修改字串,主要用於修改 html
def changecontent(old_file, new_file, old_str, new_str):
    content = open(old_file)
    with open(new_file, 'w') as f:
        for line in content:
            f.write(line.replace(old_str,new_str))

    content.close