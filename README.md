# Модуль фитнес-трекера
```sh
Fitness tracker module proccesses data for three types of training (jogging, sports walking, swimming)
It performs such functions as:
- to get data from sensors,
- to define the type of training,
- to calculate training results,
- to show info message about results.

Info message should contain such data as:
- type of training,
- duration of training,
- distance,
- average speed (km/h),
- burned calories.
```
```sh
Модуль фитнес-трекера, который обрабатывает данные для трёх видов тренировок (бега, спортивной ходьбы и плавания). 
Этот модуль должен выполнять следующие функции:
- принимать от блока датчиков информацию о прошедшей тренировке,
- определять вид тренировки,
- рассчитывать результаты тренировки,
- выводить информационное сообщение о результатах тренировки.

Информационное сообщение должно включать такие данные:
- тип тренировки (бег, ходьба или плавание);
- длительность тренировки;
- дистанция, которую преодолел пользователь, в километрах;
- среднюю скорость на дистанции, в км/ч;
- расход энергии, в килокалориях.
```

## Running project in dev-mode/Запуск проекта в dev-режиме

Clone repository. Install and activate virtual environment./
Клонировать репозиторий. Установить и активировать виртуальное окружение.

```
# For Mac or Linux:
$ python3 -m venv venv
$ source venv/bin/activate

# For Windows
$ python3 -m venv venv
$ source venv/Scripts/activate 
``` 

Install dependencies  from requirements.txt./
Установить зависимости из файла requirements.txt.

```
pip install -r requirements.txt
``` 

Run the homework.py file./Запустить файл homework.py
