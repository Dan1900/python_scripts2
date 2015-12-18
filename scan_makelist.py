import os
import os.path
#rootdir='/media/qd/306897646897279C/Data/neg/neg/'
rootdir='/home/qd/Desktop/adaboost_train/augpos'
#f=open('/media/qd/306897646897279C/Data/neg/neg.txt','w')
f=open('/home/qd/Desktop/adaboost_train/augpos/augpos.txt','w')
for parent,dirnames,filenames in os.walk(rootdir):
	#for dirname in dirnames:
	#	print "parent is:"+parent
	#	print "dirname is :"+dirname

	for filename in filenames:
		#print "parent is: "+parent
		#print "filename is: "+filename
		print "the full name of the file is: "+os.path.join(parent,filename)
		#line=parent+filename+'\n'	 
                line=filename+'\n'         
		f.write(line)
f.close()
