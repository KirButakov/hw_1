import os
import tempfile

import pytest

from src.decorators import log


# Пример функции, которая будет использоваться в тестах
@log(filename="test_log.txt")
def add(x, y):
    return x + y


def test_log_decorator_stdout(capsys):
    # Тестирование вывода на консоль
    @log()  # Добавляем декоратор здесь
    def add(x, y):
        return x + y

    add(1, 2)
    captured = capsys.readouterr()
    assert "add ok\n" in captured.out


def test_log_decorator_file():
    # Тестирование записи в файл
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_filename = temp_file.name
        temp_file.close()
        try:

            @log(filename=temp_filename)
            def multiply(x, y):
                return x * y

            multiply(3, 4)
            with open(temp_filename, "r") as f:
                content = f.read()
                assert "multiply ok\n" in content
        finally:
            os.remove(temp_filename)


def test_log_decorator_exception(capsys):
    # Тестирование обработки исключений с выводом в консоль
    @log()
    def divide(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    captured = capsys.readouterr()
    assert "divide error: ZeroDivisionError: division by zero. Inputs: (1, 0), {}" in captured.out


def test_log_decorator_exception_file():
    # Тестирование обработки исключений с записью в файл
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_filename = temp_file.name
        temp_file.close()
        try:

            @log(filename=temp_filename)
            def divide(x, y):
                return x / y

            with pytest.raises(ZeroDivisionError):
                divide(1, 0)

            with open(temp_filename, "r") as f:
                content = f.read()
            assert "divide error: ZeroDivisionError: division by zero. Inputs: (1, 0), {}" in content
        finally:
            os.remove(temp_filename)
