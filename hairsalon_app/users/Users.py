class Users:
    def __init__(self,username):
        #self.owner_id = owner_id
        self.username =username
    def __str__(self):
       return f"Name: {self.username}" 