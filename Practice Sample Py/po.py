#B=['Adam','Bella','Charlie','David']
'''B=[1,2,3,4,5]
for count in B:
    print (count)'''

'''a=[22,44,66,44,323,54]
sum=0
for i in a:
    sum += i
print(sum)    '''

'''a=[22,44,66,44,323,54]
largest = -999
for i in a:
    if i > largest:
        largest = i
print(largest) '''    

'''for counter in range(5):
    print (counter,'index')'''


'''flowers =['Lily','Rose','Orchid']
for x in flowers:
    if x == 'rose':
        continue
    print(x)'''


#3 range function
''' syntax range (start, stop, step)'''

'''for x in range(-10,5):
    print(x)'''



'''color=['White','Green','Red','Black']
cars=['BMW','Lamborghini','Mercedez','Bugatti']
for x in color:
    for y in cars:
        print(x,y)'''


#pass statement
'''a=20
if a< 80:
     pass
print('GGGGG')   '''

'''for num in range(2,4):
    print('Hi')'''

'''
#taking input
random=[input('Enter the name of your favorite car :') , input('Enter a Number :')]
#loop structure
for i in range(int(random[1])):
    print(random[0]))'''

'''num=int(input('Enter Number:'))
list=[],num
for i in range'''



''''i = int (input ("Enter Number:"))
sum = 0 
for i in range (1,i):
    if i %7 ==0 :
        sum+= i
print (sum)'''
'''
sum =0
sum2=0
counter=0
for a in range(0,10):
    n= int(input("enter ten numbers: "))
    if n%2!=0:
        sum =sum+n
        counter=counter+1
sum2=float(sum/counter)
print("Total is %d and Average is %f"%(sum,sum2))'''

'''
sum=0
#loop structure
for i in range (0,600):
    if (i%7==0 and i%9==0):
        pass
    elif (i%7==0 ):
        sum+=i
    elif i%9==0 :
        sum+=i   
print(sum)'''

'''for on in range(10,50):
    if (on%2 != 0):
        print(on)'''




''' #apply of input function
n =int(input("enter a number: "))
#variables
m=n+1
sum=0
sum2=0
for o in range(0,m):
    if o%2!=0:
        sum=sum+o**2
    elif o%2==0:
        sum2=sum2+o**2
l =sum-sum2
print("y=%d"%l)'''

'''
x=int(input('Enter a number: '))
i=x+1
s=0
s1=0
for n in range(0,i):
    if n%2!=0 :
        s=s+n**2
    elif n%2==0:
        s1=s1+n**2
a=s-s1
print ('y= %d'%a)      '''   

'''
sum =0
sum2=0
counter=0
for a in range(0,10):
    n= int(input("enter ten numbers: "))
    if n%2!=0:
        sum =sum+n
        counter=counter+1
sum2=float(sum/counter)
print("Total is %d and Average is %0.2f"%(sum,sum2))'''
'''
s=0
for i in range(0,10):
    n=int(input())
    s=s+n
    print(s) '''
'''
n=int(input('A number: '))
i=10
for x in range(n-1):
    i=i*10
print(i)'''

"""
n=int(input('Input quantity: '))
sum=0
for x in range(0,n):
    n1=int(input('Input Numbers: '))
    sum+=n1
    sum1=sum/2
    if x==0:
        maximum=n1
    elif n1 > maximum: 
        maximum=n1
    if  x==0:
        minimum =n1 
    elif n1< minimum:
        minimum = n1    
print ('"Maximum',maximum,'"','"Minimum','"',minimum,'"Average is',sum1,'"')"""


#taking input
'''n=int(input("A number= "))

for x in range(1,n+1):
    if(n%x==0):
        print(x,end=",")
print("Total %s divisors"%count)'''

'''
N=int(input('Enter a number'))
s=N+1
sum=0
for i in range(1,s):
    if i%7==0:
        sum+=i
print(sum)'''



'''numb=int(input("Please, enter input quantity: "))
sum=0
count=0
for index in range(numb):
    inp=int(input("Please, enter a number: "))
    if index==0:
        maximum=inp
    elif inp>maximum:
        maximum=inp
    if index==0:
        minimum=inp
    elif inp<minimum:
        minimum=inp
    sum+=inp
    count+=1
av=sum/count
print("Maximum",maximum,"Minimum",minimum,"Average is",av)'''

'''
n=int(input("Enter a number:"))
count=0
while(n>0):
    count+=1
    n=n//10
print("The number of digits=",count)'''