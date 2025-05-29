'''t=int(input())
h = t // 3600
hs = t % 3600
m = hs // 60
s = hs % 60
print('{}:{}:{}'.format(h,m,s))'''

'''days=int(input())
ano = days // 365
hs =days % 365
mes = hs // 30
dia = hs % 30
print('{} Years'.format(ano),end=',')
print('{} Months '.format(mes),end='and ')
print('{} Days'.format(dia),end='')'''

'''
def function_name(days):
    year = days // 365
    hs =days % 365
    months = hs // 30
    day = hs % 30
    print('{} Years'.format(year),end=', ')
    print('{} Months '.format(months),end='and ')
    print('{} Days'.format(day),end='')
function_name(int(input()))'''

'''def splitting_money(amount):
    D=amount // 500
    C=(amount%500)//100
    L=((amount%500)%100)//50
    XX=(((amount%500)%100)%50)//20
    X=((((amount%500)%100)%50)%20)//10
    II=(((((amount%500)%100)%50)%20)%10)//2
    if D>0:
        print('500 taka: {} note(s)'.format(D))
    if C>0:
        print('100 taka: {} note(s)'.format(C))
    if L>0:
        print('500 taka: {} note(s)'.format(D))
    if XX>0:
        print('500 taka: {} note(s)'.format(D))
    if X>0:
        print('500 taka: {} note(s)'.format(D))
    if II>0:
        print('500 taka: {} note(s)'.format(D))
splitting_money(int(input()))'''

x,y=map(int,input().split())
if x==1 :
    x1=4.00*y
    print('Total: R$ %0.2f'%x1)
elif x==2 :
    x2=4.00*y
    print('Total: R$ %0.2f'%x2)
elif x==3 :
    x3=4.00*y
    print('Total: R$ %0.2f'%x3)
elif x==4 :
    x4=4.00*y
    print('Total: R$ %0.2f'%x4)
elif x==5 :
    x5=4.00*y
    print('Total: R$ %0.2f'%x5)