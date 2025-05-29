#python program to find area of a triangle

a,b,c = map(float , input().split())
#formula
s= (a+b+c)/2.0
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("The area of the triangle is %0.2f" %area)