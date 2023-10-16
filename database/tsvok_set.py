# coding=UTF-8
import csv
import pickle
import os
filename="blockchair_bitcoin.tsv"
s=set()
count=0

num=0
with open(os.getcwd()+"/"+filename) as f:
     data=csv.reader(f,delimiter='\t')
     for line in data:
        # print(line[0])
        count=count+1
        s.add(line[0])
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
            

#data=csv.reader("C:\\Users\\HY\\Desktop\\380.tsv",delimiter='\t')
## with open("D:\\data.pkl", "wb") as f:
#     # pickle.dump(data,f)
#dset= set(data["address"])
#df=pd.DataFrame(dset)
#df.to_pickle("D:\\pk.pkl")
#print(df)
#print(os.getcwd())