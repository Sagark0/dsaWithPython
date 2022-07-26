a=5
def func(a):
    a+=1
    return a
for i in range(4):
    a=func(a)
print(a)