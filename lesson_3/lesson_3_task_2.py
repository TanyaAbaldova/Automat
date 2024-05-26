from smartphone import Smartphone
catalog = []

phone1 = Smartphone("Xiaomi ","Redmi 10 ", "+79001112233")
phone2 = Smartphone("Xiaomi ","M5S" , "+79004445566")
phone3 = Smartphone("Nokia ","5100 ", "+79007778899")
phone4 = Smartphone("Samsung ","Galaxy S24 ", "+79990012345")
phone5 = Smartphone("Apple ","iPhone 13 ", "+79990067890")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog: 
    phone.showPhone()
