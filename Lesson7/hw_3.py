"""
3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе
инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы методы
перегрузки арифметических операторов: сложение (add()), вычитание (sub()), умножение (mul()), деление (truediv()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и
обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух.
Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух.
Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида **\n\n***..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: **\n\n.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: **\n\n***.
"""


class Kletka:
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return self.num

    def __add__(self, other):
        return f'Сумма клеток: {self.num + other.num}'

    def __sub__(self, other):
        if self.num - other.num > 0:
            return f'Вычитание клеток: {self.num - other.num}'
        else:
            return 'вычитание невозможно'

    def __mul__(self, other):
        return f'Умножение клеток: {self.num * other.num}'

    def __truediv__(self, other):
        return f'Деление клеток: {round(self.num / other.num)}'

    def make_order(self, count):
        return '\n'.join(['*' * count for i in range(self.num // count)]) + '\n' + '*' * (self.num % count)


kletka_1 = Kletka(20)
kletka_2 = Kletka(10)
print(kletka_1 + kletka_2)
print(kletka_1 - kletka_2)
print(kletka_1 * kletka_2)
print(kletka_1 / kletka_2)
print(kletka_2.make_order(8))
