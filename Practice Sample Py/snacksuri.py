x,y=map(int,input().split())
dict1={1:4.00,2:4.50,3:5.00,4:2.00,5:1.50}
if x in dict1:
    z=(dict1[x])*y
    print('Total: R$ %0.2f'%z)
else:
    pass