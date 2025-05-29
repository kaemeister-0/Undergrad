from math import sqrt
a,b,c=map(float,input().split())
div=(b*b)-(4*a*c)
if div>0 and a!=0 :
    x1 = (-b+sqrt(div))/(2*a)
    x2 = (-b-sqrt(div))/(2*a)
    print('R1 = %0.5f'%x1)
    print('R2 = %0.5f'%x2)
else:
    print('Impossivel calcular')