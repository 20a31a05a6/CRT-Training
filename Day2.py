#Day2 training session
a=[10,20,30,40,50]
b=[15,10,20,25,30]
a.append(60)
print(a)
c={"10",'100','20','30'}
print(c)
#tuple
t=(1,2,3,4,5,3,4,2)
res=t.count(3)
print(res)
resu=t.index(3)
print(resu)

#sets venn diagrams operations
s1={1,2,3,4,5,4,5,3,2,6,7,8,2} #allow duplication
s2={2,8,4,9,10,5,15,20}
print(s1-s2)
print(s2-s1)
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
#s=set(1,2,3,4)
#l=set(5,6,7,8)
#print(s.union(l))

#Conditional Statements
p=True
if p==True:
    
    print("Correct Condition")
else:
    print("Wrong Condition")


#Odd or Even program
p=int(input("Enter a Number:"))
if p%2==0:
    
    print("Even Number!")
else:
    print("Odd Number")

#Prime or not
n=int(input("Enter Number:"))
n=n//10
if n%2==0:
    print("It is a Prime")
else:
    print("It is not a Prime")
#sample code for elif
n = int(input("Enter Number:"))
if n>0 and n<=20:
    if n%2==0:
        print("weired Number")
    else:
        print("normal number")
elif n>=20 and n<30:
    print("Normal Number:")
else:
    if n%2==0:
        print("Normal number")
    else:
        print("weired Number")
        
 #ranges (for lopps)
print(list(range(1,10)))
for i in range(11):
    print(i,end=" ")
lst=[20,30,40,70,80,90]
for i in lst:
    print(i, end=" ")
lst=[1,2,3,4,5,6,7,8,9,10]
for i in lst:
    print(i*i,end=" ")

#print the index values of list or range
l= [20,45,76,36,29, 'chinni' 'sai']
for i in range(len(l)):
    print(i,end = " ")

#program
n=int(input())
l1=[10,15,20,40,50,30]
flag=False
temp=0
for i in range(len(l1)):
    if n==l1[i]:
        print(i)
        temp= True
        break
if temp== False:
    print("Not present in that list")

#list compresions
l=[i for i in range(10)]
print(l)
l1=[i*i*i for i in range(10)]
print(l1)
l2=[num for num in range(1,101) if num%2==0]
print(l2)
l3=[num for num in range(1,101) if num%2!=0]
print(l3)

#program
lst=[num for num in range(1,1001) if num%7==0 and num%11==0]
print(lst)
print(len(lst))
#program
l=[1,2,3,5]
for i in range(len(l),0,-1):
    print(i,end=" ")

sepList=list(map(int,input().split(' ')))
p,n=0,0

for i in sepList:
    if i<0:
        n+=i
    else:
        p+=i
print(p+n)

#2 dictionaries of con be in list 



    


        
