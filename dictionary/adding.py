

lis = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
#lis=[20, 20, 30, 40, 30,50,60]
b=[]


for i in range(len(lis)):
    for j in range(i+1,len(lis)):
        if(lis[i]==lis[j]):
            b.append(lis[j])
print(list(set(b)))
