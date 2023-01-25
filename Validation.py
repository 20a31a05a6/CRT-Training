e=input()
str ="@gmail.com"
if e[0] in "qwertyuiopasdfghjklzxcvbnmQWERRTYUIOPASDFGHJKLZXCVBNM":
    if e[-10:]==str:
        print("validation Successfully")
    else:
        print("Missing @ character in Email")
else:
    print("Reenter email")
    
    
    
