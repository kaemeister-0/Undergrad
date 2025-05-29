x=input('entr:')
count=0
for index in x:
    #a=int(index)
    if index=='0' or index=='1':
        count+=1
    else:
        count=count
if count==len(x):
    print('binary')
else:
    print('not')