import copy
import pickle
def myCompare(x, y):
    neq = (x != y)
    if x > y and neq:
        print str(x)+" > "+str(y)
    elif not(x > y) and neq:
        print str(x)+" < "+str(y)
    else:
        print str(x),"=",str(y)
    return x, y

var1 = input ("podaj wartosc 1: ")
var2 = input ("podaj wartosc 2: ")
x,y = myCompare(var1,var2)
list = ["Abecki","Bebecki","Cebecki","Debecki"]
print x,y
print list[1].upper()
print list[1]
for x in list: print x.upper() 
[x.upper() for x in list]
print "Pierwszy wyraz listy to: {}, a drugi, to: {}".format(list[0],list[1])

class Person:
    "klasa cz?eka"
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
    def getFullName(self):
        return self.firstName+" "+self.lastName

class Scientist(Person):
    def __init__(self, firstName, lastName, title):
        Person.__init__(self, firstName, lastName)
        self.title = title

    def getFullName(self):
        return self.title+" "+ Person.getFullName(self)

p = Person("Adam", "Abecki")
print p.getFullName()
s = Scientist("Bartosz", "Bebecki", "mgr")
print s.getFullName()


file = open("testPickle", "w")
pickle.dump(list,file)
file.close()

file = open("testPickle", "r")
otherList = pickle.load(file)
print otherList