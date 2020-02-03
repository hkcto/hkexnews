from ftplib import FTP
import os

def ftpupload():
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
            ftp.storbinary('STOR '+ name, open(file, 'rb'))
            
    ftp.quit()

ftpupload()