# Функции в Python являются объектами: их можно присваивать переменным
def hello():
    print("hello")


def wrap(another_func):
    print("Я получаю функцию и возвращаю, как есть")
    return another_func


new_hello = wrap(hello)
new_hello()


# Мы положили в список и вызвали функцию из списка

def function_1():
    print("hello")


def function_2():
    print("bye")


funcs = [function_1, function_2]
funcs[0]()
funcs[1]()

# Напишем функцию, которая будет укладывать другие в словарь

registered = {}


def hello():
    """ Изначальная функция """
    print("hello")


def register_func(another_func, name):
    """ Функция регистрации в словаре"""
    registered[name] = another_func


register_func(hello, "Поздороваться")
print(registered)


# Создадим пару функций и положим в словарь. Затем попросим пользователя
# ввести что-то с клавиатуры, получим из словаря и вызовем нужную функцию.

registered = {}

def func_1():
    print("Давай начнем")

def func_2():
    print("Давай закончим")

def register_func(another_func, name):
    registered[name] = another_func

register_func(func_1, "start")
register_func(func_2, "end")

user_input = input("Введите команду")
function_to_call = registered.get(user_input)
function_to_call()

# Программа: Введите команду
# Пользователь: start
# Программа: Давай начнем

# Программа: Введите команду
# Пользователь: end
# Программа: Давай закончим