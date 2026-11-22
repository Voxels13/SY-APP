import logging

# Configure the logger
logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)

# Create handlers
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("app.log")

# Set level for handlers
console_handler.setLevel(logging.INFO)
file_handler.setLevel(logging.DEBUG)

# Create formatters and add them to handlers
console_handler.setFormatter(logging.Formatter("%(levelname)s - %(message)s"))
file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Add logging messages
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")