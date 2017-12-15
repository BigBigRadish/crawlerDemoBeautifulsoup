# -*- coding: utf-8 -*-  
#crawl big data with mongodb
import pymongo
client =pymongo.MongoClient("Localhost",27017)
agnostic=client["agnostic"]#把文章导入数据库，这里相当于创建一个数据库
sheet_lines=agnostic["sheet_lines"]#创建一个表单，mongodb跟excel很类似
path="c://Users/Agnostic/Desktop//agnostic.txt".encode(encoding='utf_8', errors='strict')
'''
with open(path,"r") as f:
    lines=f.readlines()
    for index,line in enumerate(lines):
        data={#构造一个数据字典
            "index":index,
            "line":line,
             "words":len((line).split())
        }
        print (data)
        sheet_lines.insert_one(data)#将数据插入到mongodb
        '''
#for item in sheet_lines.find({"words":0}):#从mongodb中找出所有words=0的对应的每一项
#   print (item)
for item in sheet_lines.find({"words":{"$gte":5}}):#筛选出word大于等于5的句子
    print (item["line"])
# $lt/$lte/$gt/$gte/$ne，依次等价于</<=/>/>=/!=。（l表示less g表示greater e表示equal n表示not  ）
    