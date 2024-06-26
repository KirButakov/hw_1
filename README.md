# Проект H

## Описание:

Проект H - это домашняя работа . Данная работа включает в себя : 

1)функцию, которая принимает на вход список словарей и значение для ключа 
state(опциональный параметр со значением по умолчанию 
EXECUTED) и возвращает новый список, содержащий только те словари, у которых ключ 
state содержит переданное в функцию значение.

2)функцию, которая принимает на вход список словарей и возвращает новый список, в котором исходные словари отсортированы по убыванию даты (ключ 
date). Функция принимает два аргумента, второй необязательный задает порядок сортировки (убывание, возрастание).

3)Функцию, которая  умеет работать как с банковскими  картами, так и со счетами.

# Тестирование:

Этот раздел README предоставит пользователям и разработчикам всю необходимую информацию для установки и запуска тестов, а также даст представление о структуре тестов и используемых библиотеках.

## Установка необходимых библиотек

Для запуска тестов вам потребуется установить `pytest`. Вы можете установить его с помощью pip:

pip install pytest

## Запуск тестов

Чтобы запустить тесты, выполните следующую команду в корневой директории проекта:

pytest

Эта команда автоматически найдет все файлы, начинающиеся с test_ или заканчивающиеся на _test.py, и выполнит содержащиеся в них тесты.

## Структура тестов
Тесты расположены в файле test_homework.py в пакете tests

## Используемые библиотеки

pytest: Основная библиотека для написания и выполнения тестов.


