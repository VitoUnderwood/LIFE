x = [1,3,2,5,4]
for i in range(len(x)-1):
    for j in range(i+1,len(x)):
        if x[i] > x[j]:
            x[i],x[j] = x[j],x[i]
print(x)