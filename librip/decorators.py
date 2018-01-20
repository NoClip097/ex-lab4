# Здесь необходимо реализовать декоратор, print_result который принимает на вход функцию,
# вызывает её, печатает в консоль имя функции, печатает результат и возвращает значение
# Если функция вернула список (list), то значения должны выводиться в столбик
# Если функция вернула словарь (dict), то ключи и значения должны выводить в столбик через знак равно


def print_result(func_to_decorate):  # Всё как на лекции
    def decorated_func(*args):
        res = func_to_decorate(*args)
        print(func_to_decorate.__name__)
        if type(res) is str or type(res) is int:
            print(res)
        elif type(res) is list:
            print("\n".join([str(x) for x in res]))  # В одну строку
            #list(map(lambda x: print(x), res))
        elif type(res) is dict:
            print("\n".join([str(x) + " = " + str(res[x]) for x in res]))  # В одну строку
            #for k, v in res.items():
               # print('{} = {}'.format(k, v))
        return res
    return decorated_func
