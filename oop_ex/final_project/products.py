class Products:
    """
    This class represents a list of Product objects and provides
    functionality to work with the data of these objects. It allows for managing and
     manipulating the Products information, performing various operations,
     and accessing relevant information associated with each product
    """
    def __init__(self, products: list):
        """
        Constructor that initializes products' attribute
        :param products: list of Products
        :raises TypeError if parameter that was sent isn't of an appropriate type
        """
        self.products = products

    @property
    def products(self) -> list:
        """
        Getter of a products list
        :return: list of products
        :raises TypeError if there are no parameters or they are invalid
        """
        return self.__products

    @products.setter
    def products(self, products: list) -> None:
        """
        Setter for products list
        :param products: list of products
        :return: None
        """
        self.__products = products

    def total_prod_income(self) -> float:
        """
        Function that return total income of all products
        :return: income for all products that were sold this month
        :raises TypeError if parameters of a product are passed in incorrect type or list of products is empty
        """
        return sum(product.price * product.amount for product in self.products)

    def bestseller_prod(self) -> object:
        """
        Function that check what product is bestseller of the month and returns this Product object
        :return: Product object bestseller of the month
        :raises TypeError if parameters of a product are passed in incorrect type or list of products is empty
        """
        max_price = 0
        for product in self.products:
            if product.price * product.amount > max_price:
                max_price = product.price * product.amount
                bestseller_prod = product

        return bestseller_prod

    def amount_not_sold_prods(self) -> int:
        """
        Function that returns amount of not sold products
        :return: amount of not sold products in the list of products
        :raises TypeError if parameters of a product are passed in incorrect type or list of products is empty
        """
        return sum(1 for product in self.products if product.amount == 0)

    def cheapest_prod(self) -> object:
        """
        Function that returns Product object in a list that has the smallest price
        :return: Product object with the smallest price
        :raises TypeError if parameters of a product are passed in incorrect type or list of products is empty
        """
        min_price = self.products[0].price
        cheapest_prod = self.products[0]
        for product in self.products:
            if product.price < min_price:
                min_price = product.price
                cheapest_prod = product
        return cheapest_prod

    def most_expensive_prod(self) -> object:
        """
        Function that returns Product object in a list that has the highest price
        :return: Product object with the highest price
        :raises TypeError if parameters of a product are passed in incorrect type or list of products is empty
        """
        max_price = self.products[0].price
        expensive_prod = self.products[0]
        for product in self.products:
            if product.price > max_price:
                max_price = product.price
                expensive_prod = product
        return expensive_prod

    def not_sold_prods(self, zero_sold_prod: int) -> str:
        """
        Function that returns Products objects details in a list that weren't sold this month
        :param zero_sold_prod: parameter to indicate products that were not sold
        :return: Products objects details that weren't sold this month
        :raises TypeError if parameters of a product are passed in incorrect type or list of products is empty
        """
        not_sold = [product.__str__() for product in self.products if product.amount == zero_sold_prod]
        return not_sold
