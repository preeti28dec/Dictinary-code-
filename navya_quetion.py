name=input("enter the any santence =\n")
user=name.split(" ")
i=0
x=[]
y=[]
while i<len(user):
    j=0
    sum=0
    while j <len(user[i]):
        sum+=ord(user[i][j])
        j+=1
    x.append(sum)
    y.append(user[i])
    k=0
    while k<len(x):
        if x[i]<x[k]: 
            tem=x[i]
            x[i]=x[k]
            x[k]=tem
            y[i],y[k]=y[k],y[i]
        k=k+1
    i+=1
print(x)
print(y)