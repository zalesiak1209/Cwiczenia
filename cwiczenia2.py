from file_manager import *
# 1
lista1 = [1, 2, 3, 4, 5, 6, 7]
lista2 = [8, 9, 10, 11, 12, 13, 14]


def fun1(a_list, b_list):
    c_list = []
    i = 0;
    while i < len(a_list or b_list) - 1:
        i += 1;
        if a_list[i] % 2 == 0:
            c_list.append(a_list[i])
        if b_list[i] % 2 == 1:
            c_list.append(b_list[i])

    print(c_list)


fun1(lista1, lista2)


# 2

def fun2(dic):
    dicc = {
        'Length': str(len(dic)),
        'letters': str([i for i in dic]),
        'big_letters': str(dic.upper()),
        'small_letters': str(dic.lower())}

    print(dicc)


fun2('sialalla')

# 3
dic = {'a': '', 't': '', 'k': ''}


def fun3(text, letter):
    mystring = text.maketrans(letter)
    text_trans = text.translate(mystring)
    print('Text:', text)
    print('Po usunieciu wartosci:', text_trans)


fun3('Patryk', dic)


# 4
def fun4(temp_Celc):
    temperature_temp = float
    temp_Fahr = ((temp_Celc * 9) / 5) + 32
    temp_Rank = temp_Fahr + 459.67
    temp_Kelw = temp_Celc + 273.15
    print("Stopnie Celsjusza:", temperature_temp(temp_Celc))
    print("Stopnie Fahrenheit'a:", temperature_temp(temp_Fahr))
    print("Stopnie Rankine:", temperature_temp(temp_Rank))
    print("Stopnie Kelvin'a:", temperature_temp(temp_Kelw))


fun4(20)


# 5
class Calculator():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self, a, b):
        return a + b

    def difference(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b


# 6
class ScienceCalculator(Calculator):

    def Exponentation(self, a, b):
        return self.a ** self.b


# 7
def fun7(text):
    return text[::-1]


print('Odwrócone słowo:',fun7('koteł'))

#9
any='aaa'
file_manager.read_file(any)
file_manager.update_file(any, any)
