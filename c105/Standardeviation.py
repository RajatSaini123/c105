import csv
import math

with open('data.csv',newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)

data=file_data[0]
#finding mean

def mean(data):
    n=len(data)
    total=0
    for x in data:
        total+=int(x)
    mean=total/n
    return mean
#²and get the value
squared_list=[]
for number in data:
    a=int(number)-mean(data)
    a=a**2
    squared_list.append(a)
#getting the sum
sum=0
for i in squared_list:
    sum=sum+i
#/ the sum by the total value
result=sum/(len(data)-1)
#get the deviation by getting the √
sd=math.sqrt(result)
print(sd)