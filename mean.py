import csv
with open('heightWeight.csv')as f:
    reader = csv.reader(f)
    fileData = list(reader)
fileData.pop(0)
newData = []
for i in range(len(fileData)):
    num = fileData[i][1]
    newData.append(float(num))
n = len(newData)
total = 0
for x in newData:
    total = total+x
mean = total/n
print(mean)
