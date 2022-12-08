a={}
b={}

x=input("Number of elements in A:")
for i in range(x):
    k=input("Key:")
    v=input("Value:")
    a[k]=v
print(a)

y=input("Number of elements in B:")
for i in range(y):
    k=input("Key:")
    v=input("Value:")
    b[k]=v
print(b)

a.update(b)
print(a)