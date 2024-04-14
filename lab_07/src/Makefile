.PHONY: run gui

run: main.py
	python3 main.py

gui : ./gui/form.ui
	pyuic5 ./gui/form.ui -o gui.py
	mv gui.py gui
