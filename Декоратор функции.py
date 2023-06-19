
# декоратор

def my_decorator(func_to_decorate):

    def decorated_func():
        print('Я начал работать')
        func_to_decorate()
        print('Закончил')
    return decorated_func

@my_decorator
def my_func():
    print('Я работаю')

my_func()

# my_func = my_decorator(my_func)
# my_func()