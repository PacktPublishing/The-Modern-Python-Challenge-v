import datetime as dt
import dateutil as util
import pickle

class User(object):
    
    def __init__(self, name=None,
                 email=None, birthday=None, promo=False):
        self.name = name
        self.email = email
        self.birthday = birthday
        self.promo = promo
        self.save()
        
    def get_age(self):
        b_day = util.parser.parse(self.birthday)
        return int((dt.datetime.now() - b_day).days // 365)
    
    def __str__(self):
        age = str(self.get_age())
        return f"Your name is {self.name}. You are {age} years old"

    def __repr__(self):
        return f"{self.__class__.__name__}{self.__dict__}" 
    
    
    def promo_used(self):
        self.promo =True
        return self.promo
    
    def check_promo(self):
        if self.promo:
            return "You have already used the promo"
        else:
            return "You still have a promo to use"
        
    def save(self):
        f = open(self.name + ".obj" , "wb")
        pickle.dump(self, f)
        f.close()
        
def get_user(file):
    f = open(file, 'rb')
    user = pickle.load(f)
    return user








    