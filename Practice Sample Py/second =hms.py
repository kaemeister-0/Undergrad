#use of type int and input function
time =int(input("enter second: "))
#apply of floor division
hour =int(time//3600)
#apply of greater then equal if
if hour<=1:
    print("%d hour"%hour)
if hour>1:
        print("%d hours"%hour)
#apply of modulus
time2 =time%3600
#apply of floor Division
minute =time2//60
#apply of greater then equal if 
if minute<=1:
    print("%d minute" % minute)
if minute > 1:
        print("%d minutes" % minute)
##apply of modulus
second =time2%60
#apply of greater then equal if 
if second<=1:
    print("%d second" % second)
if second > 1:
        print("%d seconds" % second)