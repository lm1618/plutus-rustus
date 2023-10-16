#将TSV转换为pickle，TSV下载地址http://addresses.loyce.club/
#此版本为Linux版本，windows修改路径地址即可

# coding=UTF-8
import csv
import pickle
import os
filename="blockchair_bitcoin.tsv"
#创建空List
s=[]
count=0

num=0
with open(os.getcwd()+"/"+filename) as f:
     data=csv.reader(f,delimiter='\t')
     for line in data:
        # print(line[0])
        count=count+1
        s.append(line[0])
        if count%500000==0:
            print(s)
            with open(os.getcwd()+"/"+str(num).zfill(3)+".pickle","wb") as pkl:
                pickle.dump(s,pkl)
                s.clear()
            num=num+1
     num=num+1
     with open(os.getcwd()+"/"+str(num).zfill(3)+".pickle","wb") as pkl:
        pickle.dump(s,pkl)
        s.clear()
            
