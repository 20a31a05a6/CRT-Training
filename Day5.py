#Inheritance Concept
#single Inheritance
class A:
    name="Chinni"
    age=36


class B(A):
    age=10


obj=B() #accessing methods also
obj.name="Mahesh"
print(obj.age)
print(obj.name)

#multilevel inheritance
class A:
    name="Chinni"
    age=36

class B(A):
    age=10

class C(B):
    pass

class D(C):
    pass

obj=D() #accessing methods also
#obj.name="Mahesh"
print(obj.age)
print(obj.name)

#Hierarchical inheritance
class Chairman:
    student="Prasad"
    roll_no="20A31A05A6"
    marks=0
    
class Principal(Chairman):
    marks=70  
obj=Principal()
print(obj.student)
print(obj.roll_no)
print(obj.marks)
class hod(Chairman):
    student="Durga prasad"
    marks=75
    branch="cse"
obj1=hod()
print(obj1.student)
print(obj1.roll_no)
print(obj1.marks)
print(obj1.branch)

#another example
class Mobile:
    camera=""
    processor=""
    weight=""
    battery=""

class Oppo(Mobile):
    frnt_cam=""
    display_size=""
    

class Redmi(Mobile):
    pass

class Vivo(Mobile):
    pass

#multiple inheritance
#diamond problem-if occurs in multiple inheritance, child class will be confused which merhod is taken and it can be resloved using python
class Mother:
    mother_name=""
    work=""
    def mother(self):
        print(self.mother_name)
class Father:
    father_name=""
    work=""
    def father(self):
        print(self.father_name)

class Child(Mother,Father):
    def parent(self):
        print("Father:",self.father_name)
        print("mother:",self.mother_name)

s1=Child()
s1.father_name="Ajay"
s1.mother_name="Ramya"
s1.parent()

#Hybrid Inheritance
class Govt:
    funds=""
    govt_order=""
    internships=""
    def government(self):
        print(self.funds)
        print(self.govt_order)
    
class Jntuv(Govt):
    faculty=""
    no_of_blocks=""
    branches=""
    def jntuv(self):
        self.faculty
        self.no_of_blocks
        self.branches
    
class Jntua(Govt):
    faculty=""
    no_of_blocks=""
    branches=""
    def jntua(self):
        self.faculty
        self.no_of_blocks
        self.branches
class Jntug(Govt):
    faculty=""
    no_of_blocks=""
    branches=""
    def jntua(self):
        self.faculty
        self.no_of_blocks
        self.branches
class Jntuk(Govt):
    schedule=""
    syllabus=""
    faculty=""
    no_of_blocks=""
    branches=""
    def functing(self):
        print(self.schedule)
        print(self.syllabus)
class Pragati(Jntuk):
    exams=""
    labs=""
    def money(self):
        
#python libraries
#rock,paper,scissor GAME
from random import random, randint

choice=['rock','paper','scissor']
p_score=0
c_score=0
limit=5
while p_score!=limit and c_score!=limit:
    print(f"choose among the following:",choice)
    my_ch=input("Player choice:").lower()
    if my_ch not in choice:
        print("---Invalid Choice---")
        continue
    sys_ch=choice[int(randint(0,2))]
    print(f"System choice : {sys_ch}")
    if my_ch=='rock' and sys_ch=='scissor':
        p_score+=1
    elif my_ch=='scissor' and sys_ch=='paper':
        p_score+=1
    elif my_ch=='paper' and sys_ch=='rock':
        p_score+=1
    elif my_ch== sys_ch:
        print("***** DRAW ******")
    else:
        c_score+=1
    print(f"your score:{p_score} system_score:{c_score}")

if p_score > c_score:
    print("You wins the Game")
else:
    print("System wins the Game")



#method overriding is also known as polymorphism
class A:
    def method_1(self,a,b):
        print("sumof 2 numbers:",a+b)
class B(A):
    def method_1(self,abc): #passing 
        print("value of ",abc)
    def method_1(self,a,b):
        print("mul of 2 numbers:",a*b)
ob=B()
ob.method_1(10,20)#passing one argument is overridding the 2nd method
def invert(string):
    res=""
    for i in string:
        if i=='0':
            res+='1'
        else:
            res+='0'
    return res
a=int(input())
b=int(input())
op='^'
new_a=bin(a)[2:]
new_b=bin(b)[2:]
new_a=invert(new_a)
new_b=invert(new_b)
#print(new_a, new_b)
x=int(new_a,2)
y=int(new_b,2)
print(x^y)

from translate import Translator

obj =Translator(fron_lang="english",to_lang="telugu")
new_name=obj.translate("ramya")
name1=obj.translate("ajay")
print(new_name)
print(name1)
