class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


    def sayName(self):
    
        print ("Мое имя", self.first_name)

    def sayLName(self):
        print ("Моя фамилия", self.last_name)

    def sayName_lastName(self):
        print ("Меня зовут", self.first_name, self.last_name)

user1 = User("Иосиф", "Сталин")
user1.sayName()
user1.sayLName()
user1.sayName_lastName()