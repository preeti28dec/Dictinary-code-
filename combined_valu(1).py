dic1={1:10, 2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
dic4 = {}
i=0
while i<len(dic1):
    dic1.update(dic2)
    dic2.update(dic3)
    dic3.update(dic1)
    dic4.update(dic1)
    i+=1
print(dic4)