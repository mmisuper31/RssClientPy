# RSS_Reader
# Установка
Установка производится запуском команды

$ python install.py
далее программа сама установит необходимые ей модули. И всё :)

Внимание!
Если ваш Linux не Ubuntu 16.04, то вам пизда необходимо вручную установить wxPython
# Описание программы
Исполняемый файл - Reader.py

В строку "URL канала" вставляем адрес RSS и нажимаем "Загрузить". В окне слева появляются загрузившиеся статьи. Если кликнуть мышкой, то появится краткое содержание статьи снизу, если сделать дабл клик, то статья откроется в виджете браузера справа.

Можно осуществлять поиск по ключевым словам в названиях статей полученных после загрузки статей. Также возможно осуществлять поиск по ключевым словам в кратком содержании статей.

При нажатии на зеленый плюс можно добавить категорию, после чего выбрать статью кликом мышки и нажать красный плюс. В таком случае выбранная статья будет добавлена в базу данных, которую можно просмотреть при нажатии на кнопку с изображением двух листов.

Список импортируемых модулей
wx, feedparser, os, wx.html2, re, sqlite3, sys, ObjectListView
