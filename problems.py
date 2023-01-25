# rotation problem
n= int(input())
if n<=0:
    print("Invalid Input")
else:
    arr=list(map(int,input().split(' ')))
    k= int(input())
    if k<n:
        print("Invalid Input")
    else:
        first=arr[:n-k]
        last=arr[n-k:]
        res=first+last
        print(res)

# pairs problem
n=int(input())
arr=list(map(int,input().split()))
k=int(input())
res=[]
for i in range(0,n-1):
    for j in range(i+1,n):
        if arr[i]+arr[j]==k:
            res.append([arr[i],arr[j]])

print(len(set(res)))

#repeating elements
n=int(input())
arr=list(map(int,input().split()))
flag=False
ans=[]
for i in arr:
    if arr.count(i) > 1 and i not in ans:
        ans.append(i)
if len(ans)>0:
    print(*ans)
else:
    print("No elements found")

#array methods

a=[]
for i in range(int(input())):
    k=list(map(str,input().split()))
    if k[0]=="add":
        a.append(int(a[1]))
    elif k[0]=="insert":
        ele=int(a[1])
        ind=int(a[2])
        a.insert(ind,ele)
    elif k[0]=="remove":
        ele=int(a[1])
        if ele in a:
            a.remove(ele)
    elif k[0]=="pop":
        if len(a)>0:
            a.pop()
    elif k[0]=="print":
        if len(a)!=0:
            print(*a)
    
#password validation
for j in range(int(input())):
    password=input()
    pass_len=len(password)>=8 and len(password)<=16
    alp=password[0].isalpha()
    upper=False
    lower=False
    digit=False
    special=False
    for i in password:
        if i.isupper():
            upper=True
        elif i.islower():
            lower=True
        elif i.isdigit():
            digit=True
        else:
            special=True
    if pass_len and alp and upper and lower and digit and special:
        print(True)
    else:
        print(False)
        
               
               
