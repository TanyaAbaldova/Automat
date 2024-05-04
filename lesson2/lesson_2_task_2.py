year = int(input ("Введите год: "))

def is_year_leap(year):
    if year % 4 == 0:
        print (year)
        return True
    else: 
        print (year)
        return False
year1 = is_year_leap(year)
print ("Год", year, ":", year1)