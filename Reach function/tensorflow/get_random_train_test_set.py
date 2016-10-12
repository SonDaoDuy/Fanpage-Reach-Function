import codecs
import random

my_list = []
lines = random.sample(range(1,1114),891)
#print lines
data = codecs.open("getdata.txt",'r')
#data = g.read()
#print data
train = codecs.open("train",'w')
test = codecs.open("test",'w')
for line in range(1114):
    item = data.readline()
    my_list.append(item)

for i in range(1114):
    if(i in lines):
        train.write(my_list[i])
    else:
        test.write(my_list[i])

data.close()
train.close()
test.close()
#print my_list