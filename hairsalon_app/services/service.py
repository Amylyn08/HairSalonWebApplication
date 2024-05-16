class Service():
    def __init__(self,user_id, service_name,duration,price,material):
        self.user_id = user_id
        self.service_name = service_name
        self.duration = duration
        self.price = price
        self.material = material
    
    def __str__(self):
       return f"Service: {self.service_name}, Duration : {self.duration}, Price : {self.price}, Material : {self.material}"