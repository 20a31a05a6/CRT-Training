class UserClass:
    full_name=""
    email=""
    __password=""
    mobile_no=""
    def __init__(self,name,email,password):
        self.full_name=name
        self.email=email
        self.__password=password
    def update_name(self,new_name):
        self.full_name=new_name
    def get_name(self):
        return self.full_name
    '''setter method for private password'''
    def update_password(self,new_password):
        self.__password=new_password
    def update_mobile_no(self,new_number):
        self.mobile_no=new_number
    '''getter method for private passord'''
    def get_user_password(self):
        return self.__password
    
        
