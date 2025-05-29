'''n=int(input('Input quantity: '))
counter=1
product=1
while counter<=n:
    qn=int(input('Input numbers: '))
    counter+=1
    product=product*qn
print(product)'''

''' 
task18
Take five numbers from the user and find the minimum 
and the average of only the even numbers 
entered by the user.
{If the user enters odd numbers ignore them}
count=0
counter=1
sum=0
while counter<=5:
    n=int(input('Five numbers: '))
    counter+=1
    if n%2==0 :
        count+=1
        sum+=n
        if n==sum:
            minimum=n
            maximum=n
        elif n>maximum :
            maximum=n
        elif n< minimum:
            minimum = n
print('Minimum',minimum,'Avarage',(sum/count))'''

'''
n=int(input('A number: '))
i=10
counter=1
while counter<=(n-1):
    i=i*10
    counter+=1
print(i)'''



numb=int(input('Enter a number: '))
digit=0
a=numb
while a!=0:
    digit+=1
    a=a//10
print(digit)
for i in range(digit):
    digit-=1
    div=int(numb/(10**digit))
    numb=numb-(div*(10**digit))
    if numb >0:
        print(div, end=", ")
    elif numb==0:
        print(div, end=" ")



'''
while counter<digit:
    div=int(10**(digit-1))
    for x in range(num,0):
        num=num%div
        r=num//div
        div=div//10
        print(r,end=',')'''