from query_handler import *


class ProductQueries:
    """
    Class is responsible to fulfill sql queries ,
    according to the passed data
    """

    @staticmethod
    def if_catalog_num_exists(catalog_num: str) -> bool:
        """
        Function that gets as a parameter string and checks if there is such a catalog number in a Table of selected db
        :param catalog_num: catalog number we want to check in a table of a chose db
        :return: True if catalog number exists, otherwise False
        :raises QueryExecutionError exceptions could be raised if there is an error executing the SQL query or interacting with the database
        :raises DatabaseError exceptions could be raised if there is an error executing the SQL query or interacting with the database
        :raises ConnectionError exceptions could be raised if there are issues with the database connection
        :raises OperationalError exceptions could be raised if there are issues with the database connection
        """
        q = QueryHandler("localhost", "products", "root", "")
        check_catalog_num_query = q.execute_fetch("SELECT catalog_num FROM product_list WHERE catalog_num=%s ",
                                                  (catalog_num,))
        if len(check_catalog_num_query) != 0:
            return True
        return False

    @staticmethod
    def update_product(prod_name: str, price: float, catalog_num: str) -> None:
        """
        Function that takes as parameters product name, price and catalog number
         checks if such a product exists, if it exists updates the item according to catalog number
        :param prod_name: product name that should be updated
        :param price: price that should be updated
        :param catalog_num: catalog number according to what the products should be found and updated
        :return: None
        :raises QueryExecutionError exceptions could be raised if there is an error executing the SQL query or interacting with the database
        :raises DatabaseError exceptions could be raised if there is an error executing the SQL query or interacting with the database
        :raises ConnectionError exceptions could be raised if there are issues with the database connection
        :raises OperationalError exceptions could be raised if there are issues with the database connection
        """
        q = QueryHandler("localhost", "products", "root", "")
        if ProductQueries.if_catalog_num_exists(catalog_num):
            query = "UPDATE product_list SET prod_name=%s, price=%s WHERE catalog_num=%s"
            params = (prod_name, price, catalog_num)
            q.execute_non_fetch(query, params)

    @staticmethod
    def add_new_prod(catalog_num: str, prod_name: str, price: float) -> None:
        """
        Create new product in a chosen db according to passed parameters
        :param catalog_num: catalog number of a product
        :param prod_name: name of a product
        :param price: product's price
        :return: None
        :raises QueryExecutionError exceptions could be raised if there is an error executing the SQL query or interacting with the database
        :raises DatabaseError exceptions could be raised if there is an error executing the SQL query or interacting with the database
        :raises ConnectionError exceptions could be raised if there are issues with the database connection
        :raises OperationalError exceptions could be raised if there are issues with the database connection
        """
        q = QueryHandler("localhost", "products", "root", "")
        query = "INSERT INTO product_list( catalog_num, prod_name, price) VALUES (%s,%s, %s)"
        params = (catalog_num, prod_name, price)
        q.execute_non_fetch(query, params)
