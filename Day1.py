#define data types
#int datatypes(uninary operators)
var1=26
var2=53
print(var1)
print(type(var1))

#binary operators
sum = var1+var2
dif =var1-var2
mul=var1*var2
fdiv=var1/var2
idiv=var1//var2
print(sum)
print(dif)
print(mul)
print(fdiv)
print(idiv)

#float datatypes
var3= 15.5
var4= 4.0
print(type(var4))

#boolean
a=True
b=False
print(type(a))
print(type(b))



    
#logical operators
print(a and b)
#print(a or b)

#string datatypes
str1='This is a single Quote'
str1="This is a double quotes"
str2=""" This is a multiple
         lines of programming"""
print(type(str2))
print(type(str1))

#list datatypes
lst=[10,20,30,20,40,50]
print(type(lst))
print(lst)
lst[2]=60
print(lst)
print(lst[1:5])
print(lst[-1:-6:2])

#tuple datatypes
a= (10,20,30,'xyz','string',20)
print(type(a))
print(a)
n1=10%2
n2=10/2
print(n1)
print(n2)
print(0 or 1)
print(1 & 64)
print(1 or 64)


l=[1,2,3]
print(2 in l)
a=10

print(a is None)
lst=[1,2]
lst.append(10)
print(lst)
print(lst.pop(0))
print(lst)
print(lst.remove(2))
print(lst)

lst=[1,3,4,5]
print(lst.insert(1,2))
print(lst)

v=[1,1,1,2,3,4]
b=v.count(1)
print(b)
#b=a.

A=[1,2,3]
B=A.reverse()
print(A)

a=[3,1,2]
b=a.sort()
print(b)
print("g",a)
a=[1,2,3]
b=[1,2,3,4]

#c=str(list(map(str,b)))

username=input()
for i in range (8):
    password=input()
print(username,password)
user=list(map(int,input("enter").split()))
print("f",user[0]*user[0])
