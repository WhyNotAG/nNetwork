# nNetwork
## Отчет по производственной практике

### Определение лиц на основе библиотки dlib

#### С чего начать
Для распознания лиц необходимо:
>Найти на изображении лицо.

>Выделить уникальные черты лица.

>Сравнить эти характеристики на двух фотографиях.

#### Поиск лица
Для поиска воспользуемся гистограммой направленных градиентов (HOG).
>Делаем наше изображение черно-белым.

>Рассмотрим каждый пиксель и группу примыкающую к нему.

>Проведем вектор в сторону затемнения отностиельно данного пикселя.

>Разбиваем изображение на небольшие квадраты 16х16 пикселей в каждом. 
В каждом квадрате следует подсчитать, сколько градиентных векторов показывает в каждом главном направлении.

>Затем рассматриваемый квадрат на изображении заменяется вектором с направлением, преобладающим в этом квадрате.

Для сравнения используется выделение на лице 68 точек.
После этого мы получаем 128 значений (закодированные параметры лица) которые и можем сравнивать между двумя фотографиями.

### Структура проекта
Проект состоит:
> Python файл для обработки фотографии.

> Python файл для отображения пользовательского интерфейса.

> База данных.

> Обученные модели для работы с лицами.

В базе данных есть два параметра: Name и Path

### Запуск проекта
Проект запускается из файла tkgui.py
С помощью кнопки "Добавить", можно выбрать фотографию для сравнения
После нажатия на кнопку "Сравнить", нейронная сеть проходит по базе данных выдавая соответствующий результат
