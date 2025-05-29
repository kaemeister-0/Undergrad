'''name = "Moses";
age = 23
print("My name is %s am CEO at MoTech Computers " %name)
print("Current am %d years old" %age)
print("So Am %s and am %d years old" %(name,age))'''

def string(sentence,position):
    sentence1= ''
    sentence2= ''
    for index in range(len(sentence)):
        if index%position==0 and index!=0 :
            sentence1+=sentence[index]
        else:
            sentence2+=sentence[index]
    return (sentence2+sentence1)
print(string(input(), int(input())))

