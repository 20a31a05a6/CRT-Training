from User import UserClass

class Login:
    __db = []
    def __init__(self):
        self.print_menu()
    def print_menu(self):
        print("Welcome User")
        print("1.Register")
        print("2.Login")
        print("3.Exit")
    def create_user(self,name,email,password):
        new_user=UserClass(name,email,password)
        self.__db.append(new_user)
        print(self.__db)
        return True
    '''def login_user(self,email,password):
        current_user=''' 
    def validate_user(self,email,password):
        temp=self.__db.copy()
        for user_obj in temp:
            if email==user_obj.email:
                if password==user_obj.get_user_password():
                    return True #login successfully
                else:
                    return False #login failed
        #returns false because user data not found
        return False #email not found

obj=Login()
while True:
    option=input("Enter your choice: ")
    if option=="1":
        name=input("Enter your full Name:")
        email=input("Enter Your email:")
        password=input("Enter your password:")
        res=obj.create_user(name,email,password)
        if res==True:
            print("User Created Successfully")
    elif option=="2":
        email=input("Enter your email:")
        password=input("Enter Your password:")
        result=obj.validate_user(email,password)
        if result==True:
            print("Login Succefuully")
        else:
            print("Please check Your email and Password")
    elif option=="3":
        break
    else:
        print("Invalid Input")
        
    
