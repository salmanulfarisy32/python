x = ['apple','banana','cherry']
print(x)
x.append('orange')
print(x)
x.extend('a')
print(x)
x.remove('a')
print(x)
x.pop(1)
print(x)
x.pop()
print(x)
y = ['apple','banana','cherry']
print(y)
del x[1]
print(x)
del x
y = ['apple','banana','cherry']
for i in y:
    print(i)
i=0
while i < len(y):
    print(y[i])
    i = i + 1
z=['a','b','c','d','e','f','z','y','x']
z.sort()
print(z)
a=['1','2','3','4','5','9','8','7','6']
a.sort()
print(a)
z.sort(reverse = True)
print(z)
a.sort(reverse = True)
print(a)
y.reverse()
print(y)
b = a.copy()
print(b)




