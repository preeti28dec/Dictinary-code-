import operator
d={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
print('Original dictionary : ',d)
sorted_d = sorted(d.items(), key=operator.itemgetter(1))
print('ascending order: ',sorted_d)
sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
print('descending order: ',sorted_d)
