from checkings import *


class Product:
    """
    This class is used to create a product object
    """
    # Name length of the catalog number
    __length = 8

    # Product name parameters
    __min_val = 3
    __max_val = 20
    __letter_index_to_check = 0

    # Amount parameter
    __min_amount_val = 0

    # Price parameter
    __price_min_value = 0

    def __init__(self, catalog_num: str, prod_name: str, amount: int, price: float):
        """
         Constructor that initializes product's attributes
         :param catalog_num: product's catalog number value
         :param prod_name: product's name value
         :param amount: number of sold products for last month
         :param price: product's price for one item
         :raise ValueError: If one of products parameter's isn't valid
         :raise TypeError: If one of products parameter's isn't of valid type
         """
        self.catalog_num = catalog_num
        self.prod_name = prod_name
        self.amount = amount
        self.price = price

    @property
    def catalog_num(self) -> str:
        """
        Getter returns catalog number of a product
        :return: catalog number
        :raises AttributeError if a value wasn't set as it didn't pass the checkings in setter
        """
        return self.__catalog_num

    @catalog_num.setter
    def catalog_num(self, catalog_num: str) -> None:
        """
         Setter of a catalog number
        :param catalog_num: catalog number of a new product
        :return: None
        """
        if Chekings.check_catalog_number(catalog_num, self.__length):
            self.__catalog_num = catalog_num

    @property
    def prod_name(self) -> str:
        """
        Getter of a product name
        :return: product's name
        :raises AttributeError if a value wasn't set as it didn't pass the checkings in setter
        """
        return self.__prod_name

    @prod_name.setter
    def prod_name(self, prod_name: str) -> None:
        """
        Setter of a product name
        :param prod_name: name we want to set to the product
        :return: None
        """
        if Chekings.check_prod_name(prod_name, self.__min_val, self.__max_val, self.__letter_index_to_check):
            self.__prod_name = prod_name

    @property
    def amount(self) -> str:
        """
        Getter of an amount of sold product for the month
        :return: product's month sells amount
        :raises AttributeError if a value wasn't set as it didn't pass the checkings in setter
        """
        return self.__amount

    @amount.setter
    def amount(self, amount: int) -> None:
        """
        Setter of product's sells amount for a month
        :param amount: number of sold products for a month
        :return: None
        """
        if Chekings.check_amount_validity(amount, self.__min_amount_val):
            self.__amount = amount

    @property
    def price(self) -> str:
        """
        Getter of products' item price
        :return: price for item of a product
        :raises AttributeError if a value wasn't set as it didn't pass the checkings in setter
        """
        return self.__price

    @price.setter
    def price(self, price: float) -> None:
        """
        Setter of products' item price
        :param price: price for one item of product
        :return: None
        """
        if Chekings.check_price_validity(price, self.__price_min_value):
            self.__price = price

    def __str__(self) -> str:
        """
        String method returns description of created product
        :return: description of a products with all its fields
        """
        return f"It is {self.prod_name} with catalog number {self.catalog_num} which price is {self.price} " \
               f"that was sold this month {self.amount} times"
