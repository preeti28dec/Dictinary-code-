# Q1. Difference between dict.items() and dict.iteritems() in Python? 
Ans= dict.items(): returns a copy of the dictionary’s list in the form of (key, value) tuple pairs, which is a (Python v3.x) version, and exists in (Python v2.x) version.
    dict.iteritems(): returns an iterator of the dictionary’s list in the form of (key, value) tuple pairs. which is a (Python v2.x) version and got omitted in (Python v3.x) version.
# Q2. Python program to print the dictionary in a table format? 
Ans=## Python program to print the data
    d = {1: ["Python", 33.2, 'UP'],
    2: ["Java", 23.54, 'DOWN'],
    3: ["Ruby", 17.22, 'UP'],
    10: ["Lua", 10.55, 'DOWN'],
    5: ["Groovy", 9.22, 'DOWN'],
    6: ["C", 1.55, 'UP'] }
    print ("Pos,Lang,Percent,Change")
    for k, v in d.items():
    lang, perc, change = v
    print (k, lang, perc, change)
# Q3. How to find length of dictionary values? 
Ans=dict1 ={'Name':'Steve', 'Age':30, 'Designation':'Programmer'}
    print("len() method :", len(dict1))
# Q4. Find keys with duplicate values in the dictionary? 
ans=dic={
    'ball':'red',
    'bat':4,
    'wickets':8,
    'ball':'green',
    'bat':3
    }
temp = [] 
res = dict() 
for key, val in dic.items(): 
    if val not in temp: 
        temp.append(val) 
        res[key] = val 
print(res)
# Q5. Sum list of dictionaries with the same key? 
# Q6. Split dictionary keys and values into separate lists? 
ans= ini_dict = {'a' : 'akshat', 'b' : 'bhuvan', 'c': 'chandan'}
    print("intial_dictionary", str(ini_dict))
    keys = ini_dict.keys()
    values = ini_dict.values()
    print ("keys : ", str(keys))
    print ("values : ", str(values))
# Q7. Convert a set into a dictionary? 
ans= ini_set = {1, 2, 3, 4, 5}
    print ("initial string", ini_set)
    print (type(ini_set))
    res = dict.fromkeys(ini_set, 0)
    print ("final list", res)
    print (type(res))
# Q8. Get key with maximum value in Dictionary? 
ans=Tv = {'BreakingBad':100, 'GameOfThrones':1292, 'TMKUC' : 88}
    Keymax = max(Tv, key=Tv.get)
    print(Keymax)
# Q9. Sort the list alphabetically in a dictionary? 
ans=dict ={
    "L1":[87, 34, 56, 12],
    "L2":[23, 00, 30, 10],
    "L3":[1, 6, 2, 9],
    "L4":[40, 34, 21, 67]
}
print("\nBefore Sorting: ")
for x in dict.items():
    print(x)
print("\nAfter Sorting: ")
  for i, j in dict.items():
    sorted_dict ={i:sorted(j)}
    print(sorted_dict)
# Q10. Remove spaces from dictionary keys?
Product_list = {'P 01' : 'DBMS', 'P 02' : 'OS',
                'P 0 3 ': 'Soft Computing'};
Product_list = {x.replace(' ', ''): v 
     for x, v in Product_list.items()}
print (" New dictionary : ", Product_list)