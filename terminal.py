from order import Order
from pizza import PepperoniPizza, BarbecuePizza, SeafoodPizza


class Terminal:
    """Класс Терминал обеспечивает взаимодействие с клиентом."""

    COMPANY = "Пиццерия #1"
    CANCEL_ORDER_COMMAND = -1
    CONFIRM_ORDER_COMMAND = 0

    def __init__(self):
        """Конструктор класса."""
        self.menu = [PepperoniPizza(), BarbecuePizza(), SeafoodPizza()]
        self.order = None
        self.show_menu_flag = True

    def __str__(self):
        """Вернуть строковое представление класса."""
        return f"{Terminal.COMPANY}\nДобро пожаловать!"

    def show_menu(self):
        """Показать меню."""
        if not self.show_menu_flag:
            return

        print("\nМеню:")
        for i, pizza in enumerate(self.menu, 1):
            print(f"{i}. {pizza}")
            print()

        print("Для выбора укажите цифру через <ENTER>.")
        print("Для отмены заказа введите -1")
        print("Для подтверждения заказа введите 0")
        print()

        self.show_menu_flag = False

    def process_command(self, menu_item):
        """Обработать действие пользователя."""
        try:
            menu_item = int(menu_item)

            if menu_item == Terminal.CANCEL_ORDER_COMMAND:
                if self.order is None:
                    print("Заказ не создан. Нечего отменять.")
                else:
                    print("Заказ отменен.")
                    self.order = None
                    self.show_menu_flag = True

            elif menu_item == Terminal.CONFIRM_ORDER_COMMAND:
                if self.order is None or not self.order.ordered_pizzas:
                    print("Заказ пуст. Добавьте пиццы перед подтверждением.")
                else:
                    print("Заказ подтвержен.")
                    print()
                    print(self.order)
                    self.accept_payment()
                    self.order.execute()
                    self.order = None
                    self.show_menu_flag = True

            elif 1 <= menu_item <= len(self.menu):
                if self.order is None:
                    self.order = Order()

                selected_pizza = self.menu[menu_item - 1]
                # Создаем новую пиццу того же типа
                new_pizza = type(selected_pizza)()
                self.order.add(new_pizza)

            else:
                raise ValueError()

        except ValueError:
            print("Не могу распознать команду! Проверьте ввод.")
        except Exception as e:
            print("Во время работы терминала произошла ошибка...")
            if self.order:
                self.order = None
                self.show_menu_flag = True

    def calculate_change(self, payment):
        """Вернуть сдачу для 'оплата'."""
        order_total = self.order.total()
        if payment < order_total:
            raise ValueError(f"Недостаточно средств. Нужно: {order_total:.2f} р.")
        return payment - order_total

    def accept_payment(self):
        """Обработать оплату."""
        try:
            order_total = self.order.total()
            payment = float(input(f"Введите сумму: "))

            change = self.calculate_change(payment)
            print(f"Вы внесли {payment:.2f} р. Сдача: {change:.2f} р.")
            print()

        except Exception as e:
            print(f"Оплата не удалась: {e}. Заказ будет отменен.")
            raise