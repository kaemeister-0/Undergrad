num = int(input())
l1 = []
for j in range(num):
    strg = input()
    l1.append(strg)
for i in l1:
    length= len(i) 
    if length <=10 :
        print(i)
    else:
        l2 = i[1:-1]
        print(str(i[0])+str(len(l2))+str(i[-1]))

'''
class book:
    def __init__(self, name):
        self.name = name
        self.genre='biography'
    def review(self):
        print('This book is just out of the world,mind-blowing!')

class fiction(book):
    def __init__(self, name, genre="biography"):
        super().__init__(name)
        self.genre=genre
    def review(self):
        print(self.name,'which is a',self.genre, "is just out of the world,mind-blowing!")

class nonfiction(book):
    def __init__(self, name, genre="biography"):
        super().__init__(name)
        self.genre=genre
    def review(self):
        print(self.name,'which is a',self.genre, "is just out of the world,mind-blowing!")

b1 = fiction('The Shining','Psychological horror')
b2 = nonfiction('A Beautiful Mind')
b1.review()
print('=========================')
b2.review()
print('=========================')'''