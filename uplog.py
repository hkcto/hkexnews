import os

r = open('uploadlog.txt', 'a')
for root, dirs, files in os.walk('listedco'):
    for name in files:
        print(os.path.join(root,name))
        r.writelines('\n'+ os.path.join(root,name))
r.close()

