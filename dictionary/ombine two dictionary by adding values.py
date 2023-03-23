


#  Write a Python program to combine two dictionary by adding values for common keys.


d1 = {'a': 100, 'b': 200, 'c':300,"s":654,"f":34}
d2 = {'a': 300, 'b': 200, 'd':400,"s":764,"e":34,"w":5}
d3={}
for i,j in d1.items():
    if(i in d2.keys()):
        d3[i]=j+d2[i]
    else:
        d3[i]=j
        for i,j in d2.items():
            if(i not in d3.keys()):
                d3[i]=j
print(d3)
