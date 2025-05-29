'''s=input('')
n=len(s)
for i in range(n): 
        temp='' 
        for j in range(n):
            temp=temp+s[j]
            print(temp)
        if n==n:
            break '''



'''captain=['messi','ronaldo',['ramos','casillas']]
captain.append('buffon',1)
print(captain)'''
'''
word=input('')
x=len(word)
if x<4:
    print(word)
elif x>3:
    print(word+'er')
    if er in word[-1] :
        word.slice(er,est)
        print(word)'''
'''lst=[]
for i in range(0,5):
    num=int(input('Enter number: '))
    lst.append(num)
max_num= lst[0]
for x in range(0,len(lst)):
    if lst[x]>max_num:
        max_num=lst[x]
print('Largest number',max_num,'was found at location',lst.index(max_num))'''

'''lst=[]
for i in range(0,5):
    num=int(input('Enter number: '))
    lst.append(num)
max_num= lst[0]
min_num=lst[0]
for x in range(0,len(lst)):
    if lst[x]>max_num:
        max_num=lst[x]
    if lst[x]<min_num:
        min_num=lst[x]
print('Smallest number',min_num,'was found at location',lst.index(min_num))
print('Largest number',max_num,'was found at location',lst.index(max_num))'''


'''s1=input('First string: ')
s2=input('Second string: ')
if len(s1)>len(s2):
    for i in range(len(s2)):
        print(s1[i],end='')
        print(s2[i],end='')
        d=len(s1)-len(s2)
    print(s1[d:])
else:
    for i in range(len(s1)):
        print(s1[i],end='')
        print(s2[i],end='')
        d=len(s2)-len(s1)
    print(s2[d:])'''

'''w=input('Enter a word: ')
w2=w[:-2]
if len(w)<4:
    w=w
    print(w)
elif len(w)>3:
    if 'er' in w[-2:]:
        w2+='est'
        print(w2)
    else:
        w=w+'er'
        print(w)'''
'''l=[]
a=int(input())
for n in range(1,(a+1)):
    l.append(int(input()))
for n in l:
    if (n%2!=0)and (n<0):
        print("ODD NEGATIVE")
    if(n==0):
        print("NULL")
    if(n%2!=0)and(n>0):
        print("ODD POSITIVE")
    if(n%2==0)and(n<0):
        print("EVEN NEGATIVE")
    if(n%2==0)and(n>0):
        print("EVEN POSITIVE")'''

dict1={'first_name':'frodo','last_name':'baggins'}
x=dict1.pop('_name')
print(x)