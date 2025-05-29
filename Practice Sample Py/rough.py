'''
n=1
while (n<=100):
    divisor=1
    counter=0
    while(divisor<=n):
        if (n%divisor==0) :
            counter+=1
        divisor+=1   
    if (counter==2):
        print(n,'is Prime')
    else:
        print(n,'is not Prime')
    n+=1 '''

'''
N=int(input('Total number of inputs: '))
counter=1
while counter<= N:
    M=int(input('Enter Numbers: '))
    counter+=1
print(sum)'''
'''
n=int(input('Number: '))
sum = 0
for x in range(1, n):
    if n % x == 0:
        sum += x
if sum == n:
    print(n,'is perfect')
else:
    print(n,'is not perfect')'''


'''number=int(input('Number: ')
count=1
while (count<number):
    if(number%count==0):
        summa = summation+count
    count+=1
if(summation==number):
    print(number,"is perfect")
else:
    print(number,"is not perfect")'''



wrd = 'harry'
sec_wrd = 'hermione'


print(sorted(wrd.intersection(sec_wrd)))
