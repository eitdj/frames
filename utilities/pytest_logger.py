import logging, datetime
from utilities.common_functions import get_parent_framework_path


class SingletonLogger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SingletonLogger, cls).__new__()
            cls._instance.logger = logging.getLogger(__name__)
            cls._instance.logger.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(%asctime)s - %(levelname)s- %(message)s')
            time_now = datetime.datetime.now()
            time_str = time_now.strftime('%Y_%m_%d_%H_%M_%S')
            time_str = time_str.replace(":", "_")
            test_log_path = f"\\reports\\test_logs_{time_str}.log"
            file_handler = logging.FileHandler(get_parent_framework_path() + test_log_path)
            file_handler.setFormatter(formatter)
        return cls._instance
