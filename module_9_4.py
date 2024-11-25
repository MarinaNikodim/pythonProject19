import random

first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x: x[0] == x[1], zip(first, second)))
print(result) # Результатом должен быть список совпадения букв в той же позиции. Где True - совпало, False - не совпало


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as f:
            for line in data_set:
                f.write(str(line))
    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка\n', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall:

    def __init__(self, *words): # атрибут words, хранящий коллекцию строк
        self.words = words

    def __call__(self): # метод __call__ который будет случайным образом выбирать слово из words и возвращать его
        return random.choice(self.words) # Для случайного выбора с одинаковой вероятностью для каждого данного в коллекции


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
