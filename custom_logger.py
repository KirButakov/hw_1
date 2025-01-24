import logging
import os

# Создаем директорию logs, если её нет
log_directory = "logs"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Создаем логгер
logger = logging.getLogger("project_logger")
logger.setLevel(logging.DEBUG)

# Создаем обработчик, который будет записывать логи в файл
log_file = os.path.join(log_directory, "application.log")
file_handler = logging.FileHandler(log_file, mode="w")
file_handler.setLevel(logging.DEBUG)

# Создаем форматтер и добавляем его в обработчик
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(module)s - %(funcName)s - %(lineno)d - %(levelname)s - %(message)s"
)
file_handler.setFormatter(formatter)

# Добавляем обработчик в логгер
logger.addHandler(file_handler)
