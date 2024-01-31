1. Запуск вашей виртуалки
2. pip3 install -r req.txt
3. python3 file_1.py
4. для создания EXE : pyinstaller -w --onefile --add-data "templates:templates" file_1.py
5. добавление существующей БД:  pyinstaller -w --onefile --add-data "database.db:." --add-data "templates:templates" file_1.py
