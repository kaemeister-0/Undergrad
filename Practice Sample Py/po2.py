'''n=int(input())
if n==1 :
    print()
for i in range(n):
    if n%i==0 :
        print(n,'is a prime number')
    elif n%i!=0 :
        print(n,'in not prime number')'''


 # d)18,-27, 36,-45,54,-63
# c)18, 27, 36, 45, 54, 63
# initialize loop counter
'''counter = 18

#loop structure
while counter <= 63:

    #inside loop body
    if counter ==18:
        print(counter, end=",")
    else:
        print(counter, end="," )
    counter+=9'''
'''
counter=9
for i in range(9,63):
    counter=counter+9
    if counter >= 9 and counter <=63:
         print(counter, end=",")  '''
#taking input
'''num=int(input('Enter a number:'))
#declaring variables
m=0
#loop structure
while (num>0):
    #modulus & floor division function
    m=num%10
    num=num//10
    print (m,end=',')'''
'''
#taking input
num=int(input("Enter any number: "))
#variable
sum1=0
#loop structure
for i in range(1,num):
    if(num%i==0):
        sum1+=i #loop
#conditions       
if (sum1==num):
    print ('%d is perfect number'%num)   
else:
    print ('%d is not perfect number'%num)'''

'''
#taking integer
num = int(input("Enter a number: "))  
#condition
if num > 1:  
    #loop structure
   for i in range(2,num): #prime number>1
       if (num % i) == 0:  
           print(num,"is not a prime number")   
           break  
   else:  
       print(num,"is a prime number")  
         
else:  
   print(num,"is not a prime number")'''
  
import numpy as np
import cv2
import pyscreenshot as pys

forcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', forcc, 8, (1920,1080))


while True:
    img= pys.grab()
    img_np=np.array(img)

    #frame= cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Screen', img_np)
    out.write(img_np)


    if cv2.waitKey(20) & 0xFF==ord('q'):
        break

out.release()
cv2.destroyAllWindows()