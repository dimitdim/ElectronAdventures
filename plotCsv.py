import matplotlib.pyplot as plt
path=raw_input('Filename: ')
f=open(path,'r')
x=[]
y=[]
f.readline()
for line in f:
    raw=line.split(',')
    x.append(float(raw[0]))
    y.append(float(raw[1]))
p=plt.polyfit(x,y,1)
plt.scatter(x,y)
plt.scatter(x,p*x,'-')
plt.show()
