import math

'''Start your Code from the Line Below'''
r=float(input('Radius of a circle= '))
#Area of a circle is: A = πr²
#Circumference of a Circle = 2πr 
#circumference
c=2*math.pi*(r)
print('Circumference of circle is: %0.4f'%c)
#area
a=math.pi*(r)**2
print('Area of circle is: %0.4f'%a)