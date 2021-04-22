dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
ctr = sum(map(len, dict.values()))
print(ctr)
# count=0
# for key,value in dict.items():
#     if isinstance(value,list):
#         count+=len(value)
# print(count)