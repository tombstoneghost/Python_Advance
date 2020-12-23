import logging

'''
There are 5 Different Logging Levels:
    1. Debug
    2. Info
    3. Warning
    4. Error
    5. Critical
'''

''' 
helper.py
    Creating own logger
    logger = logging.getLogger(__name__)
    logger.info('Hello from helper')

    import helper
'''

# Creating a Basic Configuration
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')

# Creating a handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

# Level and format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter_log = logging.Formatter('%(name)s - (levelname)s - %(message)s')
stream_h.setFormatter(formatter_log)
file_h.setFormatter(formatter_log)

'''
Now we need to add the above methods to the logger by using the method addHandler() and we'll pass stream_h and file_h
'''
