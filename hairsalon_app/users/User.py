from flask_login import UserMixin

#hey iana, ignore this class. This is for registration, nothing to do with Members and Professionals class!
#I will implement all this later..
class User(UserMixin):
    def __init__(self, username):
        self.username = username
    
    def get_id(self):
        return self.username