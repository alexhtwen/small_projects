import logging
import logging.config
import yaml

def configure_logger_for_project(project_name: str, config: dict) -> logging.Logger:
    # Get the generic logger
    logger = logging.getLogger('my_logger')

    # Retrieve the existing formatters from the configuration
    formatter_with_milliseconds_config = config['formatters']['with_milliseconds']
    formatter_without_milliseconds_config = config['formatters']['without_milliseconds']

    formatter_with_milliseconds = logging.Formatter(
        formatter_with_milliseconds_config['format'],
        formatter_with_milliseconds_config['datefmt']
    )
    formatter_without_milliseconds = logging.Formatter(
        formatter_without_milliseconds_config['format'],
        formatter_without_milliseconds_config['datefmt']
    )

    # Create new handlers with dynamic filenames
    file_handler_with_milliseconds = logging.FileHandler(f'{project_name}_with_milliseconds.log')
    file_handler_with_milliseconds.setLevel(logging.DEBUG)
    file_handler_with_milliseconds.setFormatter(formatter_with_milliseconds)

    file_handler_without_milliseconds = logging.FileHandler(f'{project_name}_without_milliseconds.log')
    file_handler_without_milliseconds.setLevel(logging.DEBUG)
    file_handler_without_milliseconds.setFormatter(formatter_without_milliseconds)

    # Add the new handlers to the logger
    logger.addHandler(file_handler_with_milliseconds)
    logger.addHandler(file_handler_without_milliseconds)

    return logger

# Load logging configuration from the YAML file
with open('./logging_config1.yml', 'r') as file:
    config = yaml.safe_load(file.read())
    logging.config.dictConfig(config)

# Example usage
project1_logger = configure_logger_for_project('project1', config)
project1_logger.debug('Debug message for Project 1')
project1_logger.info('Info message for Project 1')

project2_logger = configure_logger_for_project('project2', config)
project2_logger.debug('Debug message for Project 2')
project2_logger.info('Info message for Project 2')
