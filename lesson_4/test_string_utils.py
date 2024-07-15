import pytest

from string_utils import StringUtils

    
def test_capitalize():
    task = StringUtils()
    #позитивные
    res = task.capitalize("воскресенье")
    assert res == "Воскресенье"
    res = task.capitalize("july")
    assert res == "July"
    res = task.capitalize("21 октября")
    assert res == ("21 Октября")
    res = task.capitalize ("17")
    assert res == "17"
    #негативные
    res = task.capitalize("")
    assert res == ""
    res = task.capitalize(" ")
    assert res == " "

@pytest.mark.xfail
#проверка на ввод числа
def test_capitalize_int():
    task = StringUtils()
    res = task.capitalize(26)
    assert res == "26"

def test_trim():
    task = StringUtils()
    #позитивные
    res = task.trim(" Идёт медведь по лесу")
    assert res == "Идёт медведь по лесу"
    res = task.trim("    VIVA LA REVOLUTION")
    assert res == "VIVA LA REVOLUTION"
    res = task.trim("    177RUS")
    assert res == "177RUS"
    #негативные
    res = task.trim("")
    assert res == ""
    res = task.trim(" ")
    assert res == ""

@pytest.mark.xfail
#проверка на ввод числа
def test_trim_int():
    task = StringUtils()
    res = task.trim(26)
    assert res == "26"

@pytest.mark.parametrize('str, delm, result', [
    #позитивные
    ("r,s,t", ",", ["r","s","t"]), 
    ("а-и-у", "-", ["а","и","у"]), 
    ("10,20,30", ",", ["10","20","30"]),
    #негативные
    ("", None, []),
    ("утро день вечер ночь", None, ["утро", "день", "вечер", "ночь"])
])
def test_to_list(str,delm,result):
    task = StringUtils()
    if delm == 0:
        res = task.to_list(str)
    else:
        res = task.to_list (str,delm)
    assert res == result

def test_contains():
    task = StringUtils()
    #позитивные
    res = task.contains("Норвежская лесная кошка","ж")
    assert res == True
    res = task.contains("Это не V","5")
    assert res == False
    res = ("05.03.1953", "9")
    assert res == True
    res = ("$200", "$")
    assert res == True
    #негативные
    res = task.contains(" "," ")
    assert res == True
    res = task.contains(" ","6")
    assert res == False

@pytest.mark.parametrize('str,symb,result', [
    #позитивные
    ("5 разных людей живут в 5 разных домах, пьют разные напитки и содержат разных питомцев. Кто выращивает рыбок?", "р", "5 азных людей живут в 5 азных домах, пьют азные напитки и содежат азных питомцев. Кто выащивает ыбок?"),
    ("Первая Госдума созвана в 1906", "0", "Первая Госдума созвана в 196"),
    ("2013", "3", "201"),
    #негативные
    (" ", " ", "")
])
def test_delete_symbol(str,symb,result):
    task = StringUtils()
    res = task.delete_symbol(str,symb)
    assert res == result

def test_starts_with():
    task = StringUtils()
    #позитивные
    res = task.starts_with("Британец","Б")
    assert res == True
    res = task.contains("Victory","F")
    assert res == False
    res = ("R3000", "R")
    assert res == True
    res = ("R3000", "3")
    assert res == False
    #негативные
    res = task.contains(" "," ")
    assert res == True
    res = task.contains(" ","6")
    assert res == False

def test_end_with():
    task = StringUtils()
    #позитивные
    res = task.end_with("Британец","ц")
    assert res == True
    res = task.contains("Victory","F")
    assert res == False
    res = ("R3000", "0")
    assert res == True
    res = ("R3000", "3")
    assert res == False
    #негативные
    res = task.contains(" "," ")
    assert res == True
    res = task.contains(" ","0")
    assert res == False

def test_is_empty():
    task = StringUtils()
    res = task.is_empty("")
    assert res == True
    res = task.is_empty("  ")
    assert res == True
    res = task.is_empty("Тут текст")
    assert res == False

@pytest.mark.xfail
def test_is_empty_number():
    #ввод в числовом формате
    task = StringUtils()
    res = task.is_empty(126)
    assert res == False

@pytest.mark.parametrize('list, join, result', [
    #позитивные
    (["r","s","t"], ",", "r,s,t"), 
    (["это","что","to-list", "наоборот?"], " ", "это что to-list наоборот?"),
    (["1","3","5 5"], "-", "1-3-5 5"),
    #негативные
    ([], None, ""),
])
def test_list_to_string(list,join,result):
    task = StringUtils()
    if join == 0:
        res = task.list_to_string(list)
    else:
        res = task.list_to_string(list,join)
    assert res == result