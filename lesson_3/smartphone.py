class Smartphone:

    def __init__(self, brand, model, number):
        self.brand = brand
        self.model = model
        self.number = number

    def showPhone(self):
        print (self.brand, self.model, self.number)

phone1 = Smartphone("Xiaomi ","Redmi 10 ", "+79001112233")
phone2 = Smartphone("Xiaomi ","M5S" , "+79004445566")
phone3 = Smartphone("Nokia ","5100 ", "+79007778899")
phone4 = Smartphone("Samsung ","Galaxy S24 ", "+79990012345")
phone5 = Smartphone("Apple ","iPhone 13 ", "+79990067890")