class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Для класса Product определите следующие свойства:
        название (name),
        описание (description ),
        цена (price),
        количество в наличии (quantity)."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product):
        return cls(**product)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = new_price
