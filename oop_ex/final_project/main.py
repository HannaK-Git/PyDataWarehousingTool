from products import *
from product_db_queries import *
from work_with_file import *
from query_handler import *

if __name__ == "__main__":

    """
    This code performs various operations on a list of product objects.
    It reads data from a file, validates its content, and creates a list of product objects.
    It then interacts with a database, updating existing products or adding new ones based on their catalog numbers. 
    The script calculates and displays data such as the total income, best-selling product, number of unsold products, 
    cheapest product, and most expensive product. It also provides a description of any products that were not sold. 
    Error handling is implemented to handle file-related errors and other potential exceptions. 
    If error occurs it is added to log.errors
    """
    # try:
    #     # list where would be saved all Product objects
    #     obj_list = []
    #
    #     # name of file with error logs
    #     error_log = "log.errors."
    #
    #     # valid file to work with
    #     file_name = "data.txt"
    #
    #     # invalid file to check if error log works
    #     not_valid_file = "not_valid_data.txt"
    #
    #     # modes to work with a file
    #     mode_append = 'a'
    #     mode_read = 'r'
    #
    #     # check validity of the file and creation of the list of Product objects
    #     WorkWithFiles.check_data_validity(file_name, mode_read, obj_list)
    #
    #     # go through the list of product objects and add them to DB if object
    #     # exists update it according to catalog number
    #     for obj in obj_list:
    #         if ProductQueries.if_catalog_num_exists(obj.catalog_num):
    #             ProductQueries.update_product(obj.prod_name, obj.price, obj.catalog_num)
    #         else:
    #             ProductQueries.add_new_prod(obj.catalog_num, obj.prod_name, obj.price)
    #     # set product objects into list of object Products
    #     prod_list = Products(obj_list)
    #
    #     # Total income for all products in a list
    #     print("Total income for a month for all the products")
    #     print(prod_list.total_prod_income())
    #
    #     # Best seller product
    #     prod = prod_list.bestseller_prod()
    #     print("The bestseller product details: ")
    #     print(prod.__str__())
    #
    #     # How many products weren't sold
    #     print(f"Amount of not sold products for this month is {prod_list.amount_not_sold_prods()}")
    #
    #     # Cheapest product details
    #     cheapest_prod = prod_list.cheapest_prod()
    #     print("The cheapest product details: ")
    #     print(cheapest_prod.__str__())
    #
    #     # The most expensive product details
    #     most_exp_prod = prod_list.most_expensive_prod()
    #     print("The most expensive product details: ")
    #     print(most_exp_prod.__str__())
    #
    #     # Description of not sold products
    #     not_sold_prods = prod_list.not_sold_prods(0)
    #     if len(not_sold_prods) != 0:
    #         for str_description in not_sold_prods:
    #             print(str_description)
    #
    # except FileNotFoundError as v:
    #     # If this error occurs add it to the log errors
    #     WorkWithFiles.error_log(error_log, mode_append, v)
    #     # print the message with description of the problem
    #     print("The specified file doesn't exist")
    # except PermissionError as v:
    #     # If this error occurs add it to the log errors
    #     WorkWithFiles.error_log(error_log, mode_append, v)
    #     # print the message with description of the problem
    #     print("You don't have permission to read from the file")
    # except ValueError as v:
    #     # If this error occurs add it to the log errors
    #     WorkWithFiles.error_log(error_log, mode_append, v)
    #     # print the message with description of the problem
    #     print("Some values are invalid")
    # except TypeError as v:
    #     # If this error occurs add it to the log errors
    #     WorkWithFiles.error_log(error_log, mode_append, v)
    #     # print the message with description of the problem
    #     print("Some data type of an object in an operation is inappropriate")
    # except AttributeError as v:
    #     # If this error occurs add it to the log errors
    #     WorkWithFiles.error_log(error_log, mode_append, v)
    #     # print the message with description of the problem
    #     print("Some attributes references or assignments failed")

    q = QueryHandler("localhost", "products", "root", "")
    res = q.execute_fetch("SELECT AVG(price) FROM product_list", ())
    for l in res:
        print(l.values())