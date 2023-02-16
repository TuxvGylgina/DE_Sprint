Итоговая аттестация по курсу "Инженер данных"

Проект №3

Анализ логов

Общая задача: создать скрипт для формирования витрины на основе логов web-сайта.

Подробное описание задачи:

Разработать скрипт формирования витрины следующего содержания:

1.      Суррогатный ключ устройства

2.      Название устройства

3.      Количество пользователей

4.      Доля пользователей данного устройства от общего числа пользователей.

5.      Количество совершенных действий для данного устройства

6.      Доля совершенных действий с данного устройства, относительно других устройств

7.      Список из 5 самых популярных браузеров, используемых на данном устройстве различными пользователями, с указанием доли использования для данного браузера относительно остальных браузеров. 

8.      Количество ответов сервера отличных от 200 на данном устройстве

9.      Для каждого из ответов сервера, отличных от 200, сформировать поле, в котором будет содержаться количество ответов данного типа

Источники:

https://disk.yandex.ru/d/BsdiH3DMTHpPrw 

Предварительный анализ данных: 
В источнике храняться 2 файла (access.log и client_hostname.csv). В файле client_hostname.csv нет данных для работы над данной задачей. Работаем с access.log.
Т.к. данные в файле access.log плохо структурированы, первоочередная задача которая перед нами стоит это очистка и структурирование данных.

Для реализации проекта была выбрана площадка  Jupyterhub (файл находится под именем exem№3) и писалась программа на pyspark, т.к. мощности своего компьютера не позволяют развернуть виртуальную машину.

Выбрала PySpark, т.к. с его возможностями для параллельной обработки данных в оперативной памяти могут существо ускорить процесс работы.

Использованы библиотеки и модули:
import re
from pyspark.sql import SparkSession
from pyspark.sql import Row, Window
import pyspark.sql.types as T   
from pyspark.sql.functions import *
import pyspark.sql.functions as F
from datetime import date
!pip install pandas
import pandas as pd
!pip install pyyaml ua-parser user-agents
from user_agents import parse, 
а так же запущена Spark сесссия.

Схема обработки данных:

Располложенный локально access.log файл с данными загружается в Spark и выполняем преобразования с колонками даты и юзер агент. После чего результат выгружаем в формате csv/
Файл client_hostname.csv был помещен в hdfs для более оперативного чтения. Ранее access.log файл так же был помещен в hdfs, но к сожалению возникли сложности и пришлось от данного метода отказаться.

Основная таблица 
![image](https://user-images.githubusercontent.com/114882919/213023491-45f2dc4b-4e17-42fb-a33e-40ca752c3e8f.png)

Полный файл находится по адресу:

http://146.120.224.166/user/tuhvatullina_gulgina/tree/result.csv

Все операции по преобразванию и анализу данных можно посмотреть в файле exem№3.ipynb