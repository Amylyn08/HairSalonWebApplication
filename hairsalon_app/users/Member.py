class Member:
    def __init__(self,user_id, is_active, user_type, status, username, full_name, email, user_image,password, phone, address, age, speciality, payrate):
        self.user_id = user_id
        self.is_active = is_active,
        self.user_type = user_type
        self.status = status
        self.username = username
        self.full_name = full_name
        self.email=email
        self.user_image= user_image
        self.password = password
        self.phone_number = phone
        self.address =  address
        self.age = age
        self.speciality = speciality
        self.pay_rate= payrate 

    def __str__(self):
       return f"User: {self.username}, Full name : {self.full_name}"