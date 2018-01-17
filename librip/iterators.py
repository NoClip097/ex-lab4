# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        self.lst=list(items)
        self.index = 0
        self.case_ignore = kwargs.get('ignore_case')
        self.buf=[]



        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False

    def __next__(self):
        while self.index <= len(self.lst):
            if self.index == len(self.lst):
                raise StopIteration
            if self.case_ignore:
                i = self.lst[self.index].lower()
            else:
                i = self.lst[self.index]
            if i not in self.buf:
                self.buf.append(i)
                return i
            self.index += 1
        raise StopIteration

            #if i not in self.buf:
            #    self.buf.append(i)
            #    return i


        #return buf
        # Нужно реализовать __next__

    def __iter__(self):
        return self
