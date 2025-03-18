import numpy as np 
import matplotlib.pyplot as plt

data = np.loadtxt(open("mtcars.csv","rb"), usecols=(1,2,3,4,5,6),delimiter=",", skiprows=1)  

maxM = data.max(axis=0)[0]
minM = data.min(axis=0)[0]
avgM = data.mean(axis=0)[0]
print("Max mpg: ",maxM)
print("Min mpg: ",minM)
print("Srednja: ",avgM)
indices = []
index = 0
for row in data:
    if row[1]==6.0:
        indices.append(index)
    index+=1     
subdata = data.take(indices, axis=0)

print("Izračun sa 6 cilindra:")
print("Max mpg: ", subdata.max(axis=0)[0])
print("Min mpg: ", subdata.min(axis=0)[0])
print("Avg mpg: ", subdata.mean(axis=0)[0])

for i in range(len(data)):
    plt.scatter(data[i][0], data[i][3], marker="o", s= data[i][5]*20)

plt.xlabel('mpg')
plt.ylabel('hp')
plt.title('Primjer')
plt.show()
