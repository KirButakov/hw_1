import functools
import traceback


def log(filename=None):
    """
    Декоратор для логирования вызова функции и её результата в файл или консоль.

    Аргументы:
    filename (str, optional): Путь к файлу для записи логов. Если не задан, логи выводятся в консоль.

    Пример:
    @log(filename="mylog.txt")
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """
            Обёртка для логирования вызова функции.

            Аргументы:
            *args: Позиционные аргументы.
            **kwargs: Именованные аргументы.

            Логирует:
            Успех - "<имя функции> ok".
            Ошибка - "<имя функции> error: <ошибка>. Inputs: <args>, <kwargs>".
            """
            log_message = ""
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
                return result
            except Exception as e:
                error_message = traceback.format_exc().strip().split("\n")[-1]
                log_message = f"{func.__name__} error: {error_message}. Inputs: {args}, {kwargs}"
                raise e
            finally:
                if filename:
                    with open(filename, "a") as f:
                        f.write(log_message + "\n")
                else:
                    print(log_message)

        return wrapper

    return decorator
