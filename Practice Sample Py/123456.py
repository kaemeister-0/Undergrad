'''n=int(input('Quantity of keys: '))
count=0
dict1={}
s=0
for i in range(n):
    keys=input('Key: ')
    count+=1
    for index in range(n):
        values=int(input('Values: '))
        dict1.update({keys:values})
        s+=values
        break
print(dict1)
print('Avarage is: ',s/count)'''

l = [("a", 1), ("b", 2), ("a", 3), ("b", 1), ("a", 2), ("c", 1),("c",9)]
d = {}
for a, b in l:
    d.setdefault(a, []).append(b)
    print(a)
    print(b)
print (d)