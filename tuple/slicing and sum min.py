
# 1. VIEW---(Same as a list)


n = (12,23,43,33,55,76,21,98,9,54,65,49,89,53,89,23,32)

print(n[1:])
print(n[2:16])
print(n[7:-9])
print(n[4::-1])
print(n[12::2])
print(n[1:-3:2])
print(n[4:-4:2])
print(n[-3:4:2])
print(n[1:9:-2])
print(n[-2:-9:-2])
print(n[-9::-2])
print(n[-1:-12:1])


print(sum(n))
print(max(n))
print(min(n))
print(n.count(89))
print(n.index(65))

'''
# 2.INSERT--- (not possible)
# 3.UPDATE--- (not possible)
# 4.DELETE--- (only del is possible)
'''
