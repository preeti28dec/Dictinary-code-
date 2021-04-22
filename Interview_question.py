# A_Z=['a'==1,'b'==2,'c'==3,'d'==4,'e'==5,'f'==6,'g'==7,'h'==8,'i'==9,'j'==10,'k'==11,'l'==12,'m'==13,'n'==14,'o'==15,'p'==16,'q'==17,'r'==18,'s'==19,'t'==20,'u'==21,'v'==22,'w'==23,'x'==24,'y'==25,'z'==26]
# def strScore(str, s, n): 
#     score = 0
#     index = 0
#     for i in range(n): 
#         if (str[i] == s):
#             for j in range(len(s)):
#                 score += (ord(s[j]) -
#                           ord('a') + 1)
#             index = i + 1
#             break
#     score = score * index
#     return score
# str = ["sahil", "shashanak", "sanjit","abhinav", "mohit" ] 
# s = "abhinav"
# n = len(str)
# score = strScore(str, s, n); 
# print(score)
# santence=int(input("enter the santence "))
# score = 0
# index = 0
# while index<len(santence):
#     score=santence[index]+score
#     score.out.println("ENTER A SENTENCE")
#     d=br.readLine();
#     d=d.toUpperCase();
#     if(d.charAt(d.length()-1)=='!',d.charAt(d.length()-1)=='.',d.charAt(d.length()-1)=='?'):
x=input("ente the santence")
x=x[:-1]
x=x.split(" ")
sum=0
i=0
while i<len(x):
    j=0
    while j <len(list(i)):
       sum=sum+ord(j)
       j+=1
    print(i," = ",sum)
    i+=1
    sum=0
x=sorted(x)
while i<len(x):
   print(i,end=" ")
   i+=1