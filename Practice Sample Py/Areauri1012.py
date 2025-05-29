A, B, C =input().split(" ")
base1, base2, height = A, B, C 

tringul=(1/2) * float(base1) * float(height)
circle=(3.14159 * float(height) * float(height))
trapezeum=((float(base1) + float(base2)) / 2) * float(height)
square=(float(base2) * float(base2))
rectangle=(float(base1) * float(base2))
print('TRIANGULO: %0.3f'%tringul)
print('CIRCULO: %0.3f'%circle)
print('TRAPEZIO: %0.3f'%trapezeum)
print('QUADRADO: %0.3f'%square)
print('RETANGULO: %0.3f'%rectangle)