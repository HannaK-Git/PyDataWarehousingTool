
class Chekings:
    """
    Class that contains checkings for product creation parameters
    """

    @staticmethod
    def check_catalog_number(catalog_num_to_check: str, len_to_check: int) -> bool:
        """
          Function checks if passed as parameter string is of the passed length and
          contains only alphanumeric symbols
          :param catalog_num_to_check: string that should be checked
          :param len_to_check: permitted length of the passed string
          :return: True is string contains alphanumeric symbols and is of the passed as parameter length
          otherwise False
          """

        return type(catalog_num_to_check) == str and len(
            catalog_num_to_check) == len_to_check and catalog_num_to_check.isalnum()

    @staticmethod
    def check_prod_name(prod_name: str, min_val: int, max_val: int, letter_index_to_check: int) -> bool:
        """
        Function get as a parameter a string and check if its length in a range between min_val and max_val
        and if a letter under the special index is uppercase
        :param prod_name: name of product to check
        :param min_val: minimum number of characters that valid product name can contain
        :param max_val: maximum number of characters that valid product name can contain
        :param letter_index_to_check: index of that letter we want check to be uppercase
        :return: True if all conditions are met otherwise false
        :raises: TypeError if a passed as a parameter prod_name is not of string type
        """
        return min_val < len(prod_name) < max_val and prod_name[letter_index_to_check].isupper()

    @staticmethod
    def check_amount_validity(amount: int, min_val: int):
        """
        Function gets as parameters a number of int type and minimum valid value for this number,
         checks its type and if its value more or equal to minimum value
        :param amount: number that should be checked
        :param min_val: minimum valid value for this number
        :return: True if number meets the conditions, otherwise it returns False
        """
        return type(amount) == int and amount >= min_val

    @staticmethod
    def check_price_validity(price: float, min_val: int):
        """
        Function gets as parameters number of float type and minimum value that is valid for this number
        :param price: positive number of float type
        :param min_val: minimum valid value for this price
        :return: True if price meets conditions, otherwise False
        """
        return type(price) == float and price >= min_val
