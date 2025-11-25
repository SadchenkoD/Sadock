import time

class Order:
    """Класс Заказ содержит информацию о заказе."""

    order_counter = 0

    def __init__(self):
        """Конструктор класса."""
        self.ordered_pizzas = []
        Order.order_counter += 1
        self.number = Order.order_counter

    def __str__(self):
        """Вернуть содержимое заказа и его сумму."""
        res = f"Заказ №{self.number}\n"
        for i, pizza in enumerate(self.ordered_pizzas, 1):
            res += f"{i}. {pizza}\n"
        res += f"Сумма заказа: {self.total():.2f} р.\n"
        return res

    def add(self, pizza):
        """Добавить пиццу в заказ."""
        self.ordered_pizzas.append(pizza)
        print(f"Пицца {pizza.name} добавлена!")

    def total(self):
        """Вернуть сумму заказа."""
        return sum(pizza.price for pizza in self.ordered_pizzas)

    def execute(self):
        """Выполнить заказ."""
        print("Заказ поступил на выполнение...")
        for i, pizza in enumerate(self.ordered_pizzas, 1):
            print(f"{i}. {pizza.name}")
            pizza.prepare()
            time.sleep(1)
            pizza.bake()
            time.sleep(1)
            pizza.cut()
            time.sleep(1)
            pizza.pack()
            time.sleep(1)
            print()
        print(f"Заказ №{self.number} готов! Приятного аппетита!")