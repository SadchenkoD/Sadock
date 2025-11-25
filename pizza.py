class Pizza:
    """Класс Пицца содержит общие атрибуты для пиццы."""

    def __init__(self):
        """Конструктор класса."""
        self.name = "Заготовка"
        self.dough = "тонкое"
        self.sauce = "кетчуп"
        self.toppings = []
        self.price = 0

    def __str__(self):
        """Вернуть информацию о пицце."""
        res = f"Пицца: {self.name} | Цена: {self.price:.2f} р.\n"
        res += f"Тесто: {self.dough} Соус: {self.sauce}\n"
        res += f"Начинка: {', '.join(self.toppings)}"
        return res

    def prepare(self):
        """Сообщить о процессе подготовки."""
        print(f"Начинаю готовить пиццу {self.name}")
        print(f"   - замешиваю {self.dough} тесто...")
        print(f"   - добавляю соус: {self.sauce}...")
        print(f"   - и, конечно: {', '.join(self.toppings)}...")

    def bake(self):
        """Сообщить о процессе запекания пиццы."""
        print("Выпекаю пиццу... Готово!")

    def cut(self):
        """Сообщить о процессе нарезки."""
        print("Нарезаю на аппетитные кусочки...")

    def pack(self):
        """Сообщить о процессе упаковки."""
        print("Упаковываю в фирменную упаковку и готово!")


class PepperoniPizza(Pizza):
    """Класс ПиццаПепперони дополняет класс Пицца."""

    def __init__(self):
        super().__init__()
        self.name = "Пепперони"
        self.dough = "тонкое"
        self.sauce = "томатный"
        self.toppings = ["пепперони", "сыр моцарелла"]
        self.price = 350.00


class BarbecuePizza(Pizza):
    """Класс ПиццаБарбекю дополняет класс Пицца."""

    def __init__(self):
        super().__init__()
        self.name = "Барбекю"
        self.dough = "тонкое"
        self.sauce = "барбекю"
        self.toppings = ["бекон", "ветчина", "зелень", "сыр моцарелла"]
        self.price = 450.00


class SeafoodPizza(Pizza):
    """Класс ПиццаДарыМоря дополняет класс Пицца."""

    def __init__(self):
        super().__init__()
        self.name = "Дары моря"
        self.dough = "пышное"
        self.sauce = "тар-тар"
        self.toppings = ["кальмары", "креветки", "мидии", "сыр моцарелла"]
        self.price = 550.00