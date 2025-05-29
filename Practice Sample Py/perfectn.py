'''n=int(input('Enter a number: '))
count=1
summ=0
while (count<n):
    if (n%count==0):
        summ+=count
    count+=1
if (summ==n):
    print(n,'is perfect number')
else :
    print (n,'is not perfect')    '''

a,b,c = map(int, input().split())
maxab=((a+b+abs(a-b))/2)
max =  ((maxab + c + abs(maxab - c)) / 2)
print("%d eh o maior\n" %max)