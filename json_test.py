#!/usr/bin/python
import json
import codecs
#Function:Analyze json script
#Json is a script can descript data structure as xml, 
#for detail, please refer to "http://json.org/json-zh.html".

#Note:
#1.Also, if you write json script from python,
#you should use dump instead of load. pleaser refer to "help(json)".

#json file:
#The file content of temp.json is:
#{
# "name":"00_sample_case1",
# "description":"an example."
#}
####f = file("F:/pic/test.json");
####s = json.load(f)
####print s
####print s["etag"]
####f.close

#json string:
##s = json.loads('{"name":"test", "type":{"name":"seq", "parameter":["1", "2"]}}')
##print s
##print s.keys()
##print s["name"]
##print s["type"]["name"]
##print s["type"]["parameter"][1]



##s =json.loads('{ "_id" : ObjectId("522c47995ae6e1342ccf213e"), "cTime" : ISODate("2015-06-17T05:08:42.334Z"), "etag" : "3f8d9b01bbba75a83170bbd04c294afe", "info" : { "face_data" : { "face_count" : NumberLong(1), "face_info" : [       {       "face_id" : NumberLong(0),      "face_rect" : [         {       "x" : NumberLong(547),     "y" : NumberLong(619) },        {       "x" : NumberLong(1113),         "y" : NumberLong(559) },        {       "x" : NumberLong(607),  "y" : NumberLong(1183) },  {       "x" : NumberLong(1173),         "y" : NumberLong(1123) } ],     "landmarks" : [         {       "y" : NumberLong(751),  "x" : NumberLong(664) },   {       "y" : NumberLong(748),  "x" : NumberLong(787) },        {       "y" : NumberLong(734),  "x" : NumberLong(722) },        {       "y" : NumberLong(765),     "x" : NumberLong(727) },        {       "y" : NumberLong(744),  "x" : NumberLong(734) },        {       "y" : NumberLong(688),  "x" : NumberLong(1060) },  {       "y" : NumberLong(720),  "x" : NumberLong(964) },        {       "y" : NumberLong(684),  "x" : NumberLong(1008) },       { "y" : NumberLong(720),   "x" : NumberLong(1015) },       {       "y" : NumberLong(696),  "x" : NumberLong(1000) },       {       "y" : NumberLong(688),  "x" : NumberLong(602) },   {       "y" : NumberLong(652),  "x" : NumberLong(825) },        {       "y" : NumberLong(662),  "x" : NumberLong(717) },        { "y" : NumberLong(604),   "x" : NumberLong(1111) },       {       "y" : NumberLong(628),  "x" : NumberLong(948) },        {       "y" : NumberLong(614),  "x" : NumberLong(1024) },  {       "y" : NumberLong(909),  "x" : NumberLong(811) },        {       "y" : NumberLong(900),  "x" : NumberLong(984) },        { "y" : NumberLong(727),   "x" : NumberLong(883) },        {       "y" : NumberLong(931),  "x" : NumberLong(916) },        {       "y" : NumberLong(883),  "x" : NumberLong(916) },   {       "y" : NumberLong(1039),         "x" : NumberLong(789) },        {       "y" : NumberLong(1005),         "x" : NumberLong(981) },   {       "y" : NumberLong(1005),         "x" : NumberLong(902) },        {       "y" : NumberLong(1029),         "x" : NumberLong(907) },        { "y" : NumberLong(1022),  "x" : NumberLong(907) },        {       "y" : NumberLong(1060),         "x" : NumberLong(914) },        {       "y" : NumberLong(1200),    "x" : NumberLong(885) } ] } ] } }, "status" : NumberLong(3), "uTime" : ISODate("2015-06-27T15:51:56.075Z"), "userId" : ObjectId("0007ad522c477534510795f9") }')
##print s

##s=json.loads('{ "people": [{ "firstName": "Brett", "lastName":"McLaughlin", "email": "aaaa" },{"firstName": "Jason", "lastName":"Hunter", "email": "bbbb"},{ "firstName": "Elliotte", "lastName":"Harold", "email": "cccc" }]}')
##print s
##print s['people'][0]["firstname"]
##print s['people'][0]["lastname"]

##s = json.loads('{"name":"test", "type":{"name":"seq", "parameter":["1", "2"]}}')
##print s
##print s.keys()
##print s["name"]
##print s["type"]["name"]
##print s["type"]["parameter"][1]

f=codecs.open('F:/luhaofang/DataForChenDan.data')
for line in f.readlines():
    j=json.loads(line)
    filename=j['image_id']
    filename='D:/Data/sample/pic_baby/'+filename
    pname=filename[0:filename.index('.jpg')]+'_f.pts'
    print pname
    nf=open(pname,'w')
    nf.writelines(['version 3:\n','n_points:78\n','{\n'])
    v0=j['face_points']  
    v=j['face_points'][0]['result'][0]['landmark']
    pts=[]
    for landmark in v:
        pts.append(str(v[landmark]['x']))
        pts.append(str(v[landmark]['y']))
##        print v[landmark]['x']
##        print v[landmark]['y']
##        break
    #print pts[0]
    for wi in range(0,len(pts)/2):
        line=pts[2*wi]+' '+pts[2*wi+1]+'\n'
        nf.write(line)
    nf.write('}')
    nf.close()
    print len(v)
    #print str(j)
    #print j['face_points']
    #break

