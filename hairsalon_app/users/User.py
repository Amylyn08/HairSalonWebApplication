from flask_login import UserMixin

#hey iana, ignore this class and folder. This is for registration, nothing to do with Members and Professionals class!
#I will implement all this later on..
class User(UserMixin):
    def __init__(self, username):
        self.username = username
    
    def get_id(self):
        return self.username
    
    def set_active_status(self, is_active):
        self.is_active = is_active