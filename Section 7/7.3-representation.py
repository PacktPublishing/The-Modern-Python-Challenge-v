import datetime as dt
import dateutil as util

class User(object):
    
    def __init__(self, name=None,
                 email=None, birthday=None):
        self.name = name
        self.email = email
        self.birthday = birthday
        
    def get_age(self):
        b_day = util.parser.parse(self.birthday)
        return int((dt.datetime.now() - b_day).days // 365)
    
    def __str__(self):
        age = str(self.get_age())
        return f"Your name is {self.name}. You are {age} years old"

    def __repr__(self):
        return f"{self.__class__.__name__}{self.__dict__}" 
    
    










    