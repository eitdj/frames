import logging, datetime
import os

from utilities.common_functions import get_parent_framework_path


def get_logs_directory():
    logs_directory = os.path.join(os.getcwd(), 'logs')  # Change 'logs' to your preferred directory
    if not os.path.exists(logs_directory):
        os.makedirs(logs_directory)
    return logs_directory


class SingletonLogger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SingletonLogger, cls).__new__(cls)
            cls._instance.logger = logging.getLogger(__name__)
            cls._instance.logger.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(%asctime)s - %(levelname)s- %(message)s')
            time_now = datetime.datetime.now()
            time_str = time_now.strftime('%Y_%m_%d_%H_%M_%S')
            time_str = time_str.replace(":", "_")
            log_filename = f"test_logs_{time_str}.log"
            log_directory = 'C:\\Users\\HP ODC 8\\PycharmProjects\\frames\\tests\\tests\\reports\\'
            log_filepath = os.path.join(log_directory, log_filename)

            # Create directory if it doesn't exist
            os.makedirs(log_directory, exist_ok=True)
            file_handler = logging.FileHandler(log_filepath)
            file_handler.setFormatter(formatter)
        return cls._instance

