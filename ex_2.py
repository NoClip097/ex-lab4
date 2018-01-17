#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)
data3 = ['a','A','b','B']

# Реализация задания 2
buf=[];
reg_ignore=1
for i in data3:
    if reg_ignore:
        i = i.lower()
    buf.append(i) if i not in buf else print('!',i)
#print(list(data1))
print(buf)
print('А имеем')


print(list(Unique(data1)))
print(list(Unique(data2)))
print(list(Unique(data3, ignore_case=1)))
print(list(Unique(data3, ignore_case=0)))

