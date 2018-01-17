# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        self.lst=list(items)  # Получаем в список
        self.index = 0  # Счётчик чтобы бегать по списку и в конце завершить цикл
        self.case_ignore = kwargs.get('ignore_case')
        self.buf=[]  # Список для контроля уникальных значений

        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False

    def __next__(self):
        while self.index < len(self.lst):
            if self.case_ignore:  # Определяемся, будет ли разным регистр
                i = self.lst[self.index].lower()
            else:
                i = self.lst[self.index]  # В одну строку никак не работало
            if i not in self.buf:  # Проверка на уникальость...
                self.buf.append(i)  # ...и добавление в случае успеха
                return i  # ...и возврат в случае успеха
            self.index += 1
        raise StopIteration

    def __iter__(self):
        return self
