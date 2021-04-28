'''
ООП - объектно-ориентированное программирование
класс - форма, которая описывает сущность
поле класса (переменная) - свойство сущности
метод класса (функция) - умение сущности
'''

class Character:
    # конструктор класса вызывается при создании объекта
    # конструктор - магический метод
    # магический метод - встроенный в python метод (начинается и 
    # заканчивается на __)
    # self - указатель на текущий объект класса (пишется первым параметром
    #       в каждом методе)
    def __init__(self, name='', surname='', age=18):
        # прописываем поля (свойства класса)
        self.name = name
        self.surname = surname
        self.age = age
    
    # создаем пользовательский метот класса
    def say_hi(self, to):
        # print(self.name + ' говорит тебе "привет"')
        print(f'{self.name} говорит "{to} привет!!"')
    
    # метод чтобы выводить объект в print
    def __repr__(self):
        # должен вернуть строку, которую вставим в print
        return f'<Character name:{self.name}; surname:{self.surname}; age:{self.age}>'


class FloatNum:
    def __init__(self, integer, tail=False):
        if integer < 0:
            self.sign = '-'
            integer *= -1
        else:
            self.sign = '+'
        if tail != False:
            self.integer = integer
            self.tail = tail
        else:
            # 43.1
            # "43.1"
            # "['43', '1']"
            tmp_num = str(integer).split('.')
            self.integer = int(tmp_num[0])
            self.tail = int(tmp_num[1])


'''
# создание объекта класса:
char1 = Character()
# через точку доступны поля класса
char1.name = 'John'
print(char1.name)

char2 = Character()
print(char2.name)
'''
char1 = Character('John', 'Smith', 12)
print(char1.age)

char2 = Character('Bob', 'Smith')
print(char2.age)

char3 = Character(age=9)
print(char3.age)

char1.say_hi('Миша')
char2.say_hi('Олеся')

print(char1)
print(char2)

'''
задание 1:
создать класс для хранения дробного числа (32.54)
в классе будет 3 поля
1) знак
2) целая часть
3) дробная часть
целая часть должна быть от -9999 до 9999
дробная часть может быть в диапазоне от 0 до 99

сделать возможными способы создания объекта:
a = FloatNum(12, 54)
pritn(a) # 12.54
b = FloatNum(2.3)
print(b) # 2.3
c = b.sum(3.2)
print(c) # 5.5
d = FloatNum(-9.99)
print(d) # -9.99
e = FloatNumber(1234567.3) # "Ошибка. Слишком большое число"

'''
