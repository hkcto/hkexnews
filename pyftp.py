from ftplib import FTP
import os

def ftpupload():
    uplog = []
    with open('uploadlog.txt','r') as f:
        for line in f:
            uplog.append(line.strip('\n'))
    ftp = FTP('192.168.0.254','root', '1001.admin')
    for root, dirs, files in os.walk('listedco'):
        for name in files:
            # print(root)
            folder = root.split('\\')
            file = os.path.join(root, name)
            ftp.cwd('~')
            for mk in folder:
                try:
                    ftp.mkd(mk)
                    print(mk)
                    ftp.cwd(mk)
                except:
                    ftp.cwd(mk)
            if file not in uplog: 
                ftp.storbinary('STOR '+ name, open(file, 'rb'))
                print('uploaded: ', file)
                with open('uploadlog.txt','a') as f:
                    f.write('\n'+ file)
            
    ftp.quit()




