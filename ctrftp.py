from ftplib import FTP


host ='chianteck.com'
user = 'chiantec'
password = r'bLfwipr4CoE0EFpR a X'
ftp = FTP(host, user, password)
# ftp.login()

ftp.cwd('www')
ftp.retrlines('LIST')