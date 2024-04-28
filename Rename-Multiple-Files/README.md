### [English](#EN)

### [Russian](#RU)

# EN

### Script for rename multiple files

Tested in Python version 3.11.2, but it must working in version 3.5 and above.

### Run

GNU\Linux: `$(which python3) main.py`

Windows: `C:\\Path\\to\\Python3\\Python3.exe main.py`

Folders structure:

```
main.py
root/
   |
   |--- folder1
   |          |
   |          |- file1.txt
   |          |- file2.txt
   |          |- file2.txt
   |
   |--- folder2
   |          |
   |          |- file1.txt
   |          |- file2.txt
   |          |- file2.txt
   |
   |--- folder3
   |          |
   |          |- file1.txt
   |          |- file2.txt
   |          |- file2.txt
```

Output files structure:

```
folder1/folder1-1.txt
folder1/folder1-2.txt
folder1/folder1-3.txt

folder2/folder2-1.txt
folder2/folder2-2.txt
folder2/folder2-3.txt

folder3/folder3-1.txt
folder3/folder3-2.txt
folder3/folder3-3.txt
```

Maybe set outher symbol for `DESTINATION_FILE_DELIMITER` param or just leave blank `DESTINATION_FILE_DELIMITER = ''`

# RU

### Скрипт для переименования большого количества файлов

Тестировался на Python версии 3.11.2, но должен работать на версиях выше 3.5.

### Запуск

GNU\Linux: `$(which python3) main.py`

Windows: `C:\\Path\\to\\Python3\\Python3.exe main.py`

Структура папок:

```
main.py
root/
   |
   |--- папка1
   |         |
   |         |- файл1.txt
   |         |- файл2.txt
   |         |- файл2.txt
   |
   |--- папка2
   |         |
   |         |- файл1.txt
   |         |- файл2.txt
   |         |- файл2.txt
   |
   |--- папка3
   |         |
   |         |- файл1.txt
   |         |- файл2.txt
   |         |- файл2.txt
```

Скрипт переименует файлы в папках так:

```
папка1/папка1-1.txt
папка1/папка1-2.txt
папка1/папка1-3.txt

папка2/папка2-1.txt
папка2/папка2-2.txt
папка2/папка2-3.txt

папка3/папка3-1.txt
папка3/папка3-2.txt
папка3/папка3-3.txt
```

В случае необходимости можно поменять `DESTINATION_FILE_DELIMITER` на нужный символ или вообще оставить пустым `DESTINATION_FILE_DELIMITER = ''`
