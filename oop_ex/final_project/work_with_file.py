from product import *
from datetime import datetime


class WorkWithFiles:
    """
    Class that is used to work with files
    """
    @staticmethod
    def check_data_validity(file_name: str, type_of_action: str, obj_list: list) -> None:
        """
        Function that receives as parameters file name to work with, type of mode for work with file
        and list to add there data from a file
        :param file_name: file to work with
        :param type_of_action: mode of work with a file
        :param obj_list: list where created objects from data that contains a file should be added
        :return: None
        :raises FileNotFoundError if file couldn't be found
        :raises PermissionError if user have no appropriate permission to mode he wants to use
        """
        with open(file_name, type_of_action, encoding='utf-8') as f:
            for line in f:
                # create a list of two elements: the string_to_search and the associated word in the same line
                values = line.rstrip().split(" ")
                p = Product(values[0], values[1], int(values[2]), float(values[3]))
                obj_list.append(p)

    @staticmethod
    def error_log(file_name: str, mode_type: str, error_msg: str) -> None:
        """
        Function gets as parameters filename, type of mode it should fulfil and error message
        and creates a file if it doesn't exist and save there time and date when the message was created and a message
        :param file_name: name of file that should be created or appended
        :param mode_type: type of working mode with a document
        :param error_msg: error message that should be saved
        :return: None
        :raises FileNotFoundError if file couldn't be found
        :raises PermissionError if user have no appropriate permission to mode he wants to use
        """
        str_date = datetime.now().date()  # get only date
        str_time = datetime.now().strftime("%H:%M:%S")  # get time in format "%H:%M:%S"
        with open(file_name, mode_type) as file:
            data = f"{str_date} {str_time} {error_msg}\n"  # Data to be written to the file
            file.write(data)  # Write the data to the file
