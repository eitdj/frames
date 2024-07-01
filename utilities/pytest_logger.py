import logging, datetime
import os

from utilities.common_functions import get_parent_framework_path

import logging
import os
import datetime


class SingletonLogger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SingletonLogger, cls).__new__(cls)
            cls._instance.logger = logging.getLogger(__name__)
            cls._instance.logger.setLevel(logging.DEBUG)

            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            time_now = datetime.datetime.now()
            time_str = time_now.strftime('%Y_%m_%d_%H_%M_%S')
            log_filename = f"test_logs_{time_str}.log"

            log_directory = get_parent_framework_path()
            os.makedirs(log_directory, exist_ok=True)  # Ensure the directory exists

            log_filepath = os.path.join(log_directory, log_filename)
            print(f"Log Directory: {log_directory}")  # Debug print to verify the log directory path
            print(f"Log Filepath: {log_filepath}")  # Debug print to verify the log file path

            file_handler = logging.FileHandler(log_filepath)
            file_handler.setFormatter(formatter)
            cls._instance.logger.addHandler(file_handler)

        return cls._instance
