import urllib  
import urllib2  
import os
import re
  
f=open("E:\\data\\faceScrub\\facescrub_actresses.txt")
i=f.read()
save_path="E:\\data\\faceScrub\\"  
list1=i.split()
pat = re.compile('http://(.)+')
idx=1
for s in list1:
    m = re.search('http', s, re.IGNORECASE)
    if bool(m):
        print s
        fileName=save_path+str(idx)+".jpg"
        try:
            urllib.urlretrieve(s,fileName)
            idx=idx+1
        except Exception,e:
            print e


