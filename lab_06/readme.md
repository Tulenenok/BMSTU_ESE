### Установить Qt5

```bash
python3 -m venv qt_python
. qt_python/bin/activate
pip install --upgrade pip
pip install PyQt5
```

Источник: https://stackoverflow.com/questions/60302293/import-error-symbol-not-found-futimens-with-pyqt5-in-macos-sierra-10-12-6

### Установить все остальное

```bash
pip install numpy
pip install pandas
pip install matplotlib
```

### Запуск программы

```
python3 main.py
```

### Получить exe-файл

```bash
pip install pyinstaller
pyinstaller --add-data "mainwindow.ui;." main.py
```
