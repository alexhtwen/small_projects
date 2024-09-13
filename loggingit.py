import logging
import logging.config
import yaml
from datetime import datetime

class CustomFormatter(logging.Formatter):
    def formatTime(self, record, datefmt=None):
        ct = self.converter(record.created)
        if datefmt:
            s = datetime.fromtimestamp(record.created).strftime(datefmt)
        else:
            t = datetime.fromtimestamp(record.created)
            s = t.strftime("%Y-%m-%d %H:%M:%S")
        return s

def configure_logger_for_project(project_name: str, config: dict) -> logging.Logger:
    # Get the generic logger
    logger = logging.getLogger('my_logger')

    # Retrieve the existing formatter from the configuration
    formatter_config = config['formatters']['simple']
    formatter = CustomFormatter(formatter_config['format'], formatter_config.get('datefmt'))

    # Create a new handler with the dynamic filename
    file_handler = logging.FileHandler(f'{project_name}.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # Add the new handler to the logger
    logger.addHandler(file_handler)

    return logger

# Load logging configuration from the YAML file
with open('./logging_config.yml', 'r') as file:
    config = yaml.safe_load(file.read())
    logging.config.dictConfig(config)

# Example usage
project1_logger = configure_logger_for_project('project1', config)
project1_logger.debug('Debug message for Project 1')
project1_logger.info('Info message for Project 1')

project2_logger = configure_logger_for_project('project2', config)
project2_logger.debug('Debug message for Project 2')
project2_logger.info('Info message for Project 2')
