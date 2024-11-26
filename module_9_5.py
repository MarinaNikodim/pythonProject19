class StepValueError(ValueError):
    pass


class Iterator:
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError('Шаг не может быть равен 0')
        self.start = start # целое число, с которого начинается итерация.
        self.stop = stop # целое число, на котором заканчивается итерация.
        self.step = step # шаг, с которым совершается итерация.
        self.pointer = start # указывает на текущее число в итерации (изначально start)

    def __iter__(self): # метод, сбрасывающий значение pointer на start и возвращающий сам объект итератора.
        self.pointer = self.start
        return self

    def __next__(self): # метод, увеличивающий атрибут pointer на step.
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            raise StopIteration

        current_value = self.pointer
        self.pointer += self.step
        return current_value


try:
    iter1 = Iterator(200, 100, 0)
    for i in iter1:
        print(i, end='')
except ValueError as e:
    print(f'{e}')

    iter2 = Iterator(-5, 1)
    iter3 = Iterator(6, 15, 2)
    iter4 = Iterator(5, 1, -1)
    iter5 = Iterator(10, 1)

    for i in iter2:
        print(i, end=' ')
    print()
    iter3 = Iterator(6, 15, 2)
    for i in iter3:
        print(i, end=' ')
    print()
    for i in iter4:
        print(i, end=' ')
    print()
    for i in iter5:
        print(i, end=' ')
    print()
