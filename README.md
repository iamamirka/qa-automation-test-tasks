# QA Automation Engineer test tasks

## Common info
В файле ```requirements.txt``` перечислены библиотеки и их версии, необходимые для работы проекта.
### Запуск проекта
* Создание виртуального окружения: ```python3 -m venv venv```
* Активировать virtual environment: ```source venv/bin/activate```
* Установить необходимые зависимости: ```pip install -r requirements.txt```

## First task. Pytest
Решение лежит в директории first_task.

Задание решил двумя способами (директории e2e, unit).
Первый способ - с использованием библиотеки ```Selenium```.
Второй способ - с испольованием библиотек ```requests, beautifulsoup```.
В подходах немного отличаются механизмы валидации, сообщения об ошибках выводятся по-разному.
### Запуск тестов
Из директории first_task выполнить команды
  * ```python3 -m pytest e2e/test_popularity.py```
  * ```python3 -m pytest unit/test_popularity.py```

## Second task. OOP
Решение лежит в директории second_task.

Пример работы программы описан в файле example.py (Запуск: ```python3 example.py```)
### Запуск тестов
Из директории second_task выполнить команды
  * ```pytest test_engine2d.py```
  * ```pytest test_geometrical_figures.py```

## Third task. Algorithms
Решение лежит в директории third_task.

В классе ```AppInitializer``` происходит:
* обработка введенных пользователем параметров карты, местоположения плота и пункта назначения
* инициализация карты с отрисованной на ней водой, сушей, плотом и пунктом назначения

В классе ```BreadthFirstSearch``` описан алгоритм поиска в ширину (breadth-first search), который служит для нахождения кратчайшего пути от плота до пункта назначения.

Поскольку ожидаю, что начало отсчета у пользователя с единицы, а не с нуля, при обработке введенных значений отнимаю единицу, а при выводе на экран, добавляю единицу.

### Запуск проекта 
Из директории third_task выполнить команду:
* ```python3 app.py```