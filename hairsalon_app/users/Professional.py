class Profesionnal:
    def __init__(self,username, full_name, email, user_image,password, phone, address, age, speciality, payrate):
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