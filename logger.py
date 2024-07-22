import logging
import os

# Создаем папку для логов, если она еще не существует
LOGS_DIR = 'logs'
os.makedirs(LOGS_DIR, exist_ok=True)

# Устанавливаем базовый путь к файлам логов
LOG_FILENAME_MASKS = os.path.join(LOGS_DIR, 'masks.log')
LOG_FILENAME_UTILS = os.path.join(LOGS_DIR, 'utils.log')

# Создаем логгер для модуля masks
logger_masks = logging.getLogger('masks')
logger_masks.setLevel(logging.DEBUG)  # Устанавливаем уровень логирования

# Создаем обработчик для записи в файл
handler_masks = logging.FileHandler(LOG_FILENAME_MASKS, mode='w', encoding='utf-8')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler_masks.setFormatter(formatter)

# Добавляем обработчик к логгеру
logger_masks.addHandler(handler_masks)

# Создаем логгер для модуля utils
logger_utils = logging.getLogger('utils')
logger_utils.setLevel(logging.DEBUG)  # Устанавливаем уровень логирования

# Создаем обработчик для записи в файл
handler_utils = logging.FileHandler(LOG_FILENAME_UTILS, mode='w', encoding='utf-8')
handler_utils.setFormatter(formatter)

# Добавляем обработчик к логгеру
logger_utils.addHandler(handler_utils)

# Примеры использования логгера
def example_function():
    logger_masks.debug('Это сообщение DEBUG для модуля masks')
    logger_utils.info('Это сообщение INFO для модуля utils')

# Вызов примерной функции
example_function()
