from adress import Address
from mail import Mailing

to_address = Address(355000, "Ставрополь", "Морозова", "95", "207")
from_address = Address(101000, "Москва", "Тверская", "100", "20")

mailing = Mailing(to_address, from_address, 10000, "RmEdW26")

print ("Отправление", mailing.track, "из" , from_address.index, from_address.city , from_address.street , from_address.house, "-" , from_address.apartment, "в",  to_address.index, to_address.city, to_address.street, to_address.house, "-", to_address.apartment, ".")
print("Стоимость ", mailing.cost," рублей.")