#dictionaries topic

Dict = {1: 'College', 2: 'Branch', 3: 'Section'}
print(Dict[3])

Dict=dict({1: 'Rohith','Roll_no1':'20a31a05c1',
                2 : 'Ajay','Roll_no2': '20a31a05b6'})

print(Dict['Roll_no1'])

Dict = dict([(1, 'Pragti'), (2, 'B.tech')])
print(Dict[1])

Dict = {'Name': 'prasad', 1: [1, 2, 3, 4], 2:['Hello',2,3,'string']}
print(Dict[2])
print(Dict.get(2))

Dict = {'student1': {'id': '20a31a05a6'},
        'student2': {'id': '20a31a05b6'}}
print(Dict['student1']['id'])
'''
Dict1 = {'cou1': {'branch': 'cse'},
        'cou2': {'branch': 'cse-ds'}}



#program
dict1={'students_id' :['20a31a05a6','20a31a05b6','20a31a05a1','20a31a05c1'],
       'user_name' :['prasad','ajay','mahesh','rohith']}

dict2={'mail_id' :['20a31a05a6@pragati','20a31a05b6@pragati','20a31a05a1@pragati','20a31a05c1@pragati'],
       'password' :['prasad@123','ajay@123','mahesh@123','rohith@123']}

#if dict1['students_id']== True:

up,q,r,s,t =list(map(input("enter key values:")))
user1=input("enter key2:")
lst=[]
for i in range(5):
    d={ 'key1': input(),
        'key2' : input()
    }
    lst.append(d)
print(lst)

#program method 2
lst=[]
d={}
for i in range(5):
    d.update({ 'key1': input(),
               'key2' : input()
    })
    lst.append(d)
print(lst)'''

# passward and username

db=[{'saiprasad@gmail.com' : '12345'},
    {'rohith@gmail.com': '98786'},
    {'ajay@gmail.com': '874562'},
    {'vinayak@gmail.com':'65456'}
    ]
print(db)
username=input("Username or gmail:")
password=input("password:")
temp={username:password}
if temp in db:
    print("Logged In Successfully")
else:
    print("Invalid username")

'''for i in db:
    print(i.keys())
    print(i.values())
    print(i.items()) #return list of tuples'''
    

