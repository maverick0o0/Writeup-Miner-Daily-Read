import datetime
import logging

# class colors:
#     PURPLE = '\033[95m'
#     BLUE = '\033[94m'
#     CYAN = '\033[96m'
#     GREEN = '\033[92m'
#     WARNING_COLOR = '\033[93m'
#     ERROR = '\033[91m'
#     ENDC = '\033[0m'

class Logger_type:
    ERROR = 'Error'
    DEBUG = 'Debug'
    INFO = 'Info'
    REPORT = 'Report'


# def Customlogger(debug, message ,logger_type):
#     current_time = datetime.datetime.now()
#     formatted_time = current_time.strftime("%H:%M:%S")
#     if debug == True:
#         print(colors.CYAN + "[" + colors.WARNING_COLOR + logger_type + colors.CYAN + "][" + colors.ENDC + formatted_time + colors.CYAN + "] " + colors.ENDC + message)


# Create the first logger for 'log_file.txt'
logger1 = logging.getLogger('Logger1')
logger1.setLevel(logging.DEBUG)

file_handler1 = logging.FileHandler('log_file.txt')
file_handler1.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
formatter2 = logging.Formatter('%(asctime)s  %(message)s')
file_handler1.setFormatter(formatter)

logger1.addHandler(file_handler1)

# Create the second logger for 'report.txt'
logger2 = logging.getLogger('Logger2')
logger2.setLevel(logging.DEBUG)

# file_handler2 = logging.FileHandler('report.txt')
# file_handler2.setLevel(logging.DEBUG)

# file_handler2.setFormatter(formatter2)

# logger2.addHandler(file_handler2)

# Setting the log level for 'asyncio' logger to WARNING
logging.getLogger('asyncio').setLevel(logging.WARNING)

def Customlogger(debug, message, logger_type):
    if debug:
            logger1.debug(f"[{logger_type}] {message}")
            print(f"[{logger_type}] {message}")
            
#     if logger_type == Logger_type.REPORT:
#             logger2.debug(f"[{logger_type}] {message}")
    
    if logger_type == Logger_type.ERROR:
            logger1.error(f"[{logger_type}] {message}")
            # send_error(message)