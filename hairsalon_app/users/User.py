from flask_login import UserMixin

#hey iana, ignore this class and folder. This is for registration, nothing to do with Members and Professionals class!
#I will implement all this later on..

class User(UserMixin):
    def __init__(self, username, user_id, user_type):
        self.username = username
        self.user_type = user_type #professional, client, admin_super/user/appoint
        self.user_id = user_id #like in db 
        self._is_active = True  # Using a private variable to store is_active
    
    def get_id(self):
        return str(self.username)
    
    @property
    def is_active(self):
        return self._is_active
    
    @is_active.setter
    def is_active(self, value):
        self._is_active = value
