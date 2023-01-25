#repeater operators
l="abc-"*5
print(l)

l1=[1,2,3]*5
print(l1)

#xor operation

a=5^10
print(a)
5  =0101
10 =1010
res=1111-15

# packages

def add_two_numbers(a,b):
    return a+b

def add_n_numbers(*arr):
    return sum(arr)

#from 'filename' import 'function_name'
#packages exist in day3 file

#Oop Concepts
class Student:
    name=""
    roll_number=""
    branch=""
    marks=0
    attendence=0.0
    is_transport=False
    def view_attendence(self):
        pass
    def view_marks(self):
        pass
    def view_name(self):
        pass
    def update_name(self,new_name):
        pass'''
    '''student_name="no name"
    def __init__(self,name):
        #print("object created")
        #print(name)
        #print(self.student_name)
        self.student_name=name
        def update_name(self,new_name):
            self.student_name=new_name

s1=Student("Mukesh")
s2=Student("Ramesh")
s3=Student("Suresh")
print(s2.student_name)
#print(s3.student_name)
s2.update_name("Ramesh Reddy")
print(s2.update_name)
class Bankaccount:
    acc_name=""
    acc_no=""
    __password="" #__ means private the pasword
    __account_IFSC=""
    #private variables has gitter and setter concepts
    #do not access private variables outside the class
    def __init__(self,acc_name,):
        pass





        
