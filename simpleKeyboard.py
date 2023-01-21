# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Shoker2/Desktop/TS2_Simple_Keyboard/ui template/Simple Keyboard.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QShortcut
from PyQt5.QtGui import QKeySequence
import pyperclip
import yaml
from yaml.loader import SafeLoader

import sys
import os
import configparser

class Ui_SimpleKeyboard(QMainWindow):
	resized = QtCore.pyqtSignal()

	select_button = 0
	shift_active = False
	lang_id = 0
	lang_name = "English"

	alphet = []
	addition_symbols = [
		"-",
		"+",
		"_",
		"=",
		"!",
		"?",
		"@",
		"#",
		"$",
		"%",
		"^",
		"*",
		"\"",
		"№",
		"`",
		"~",
		"(",
		")",
		"[",
		"]",
		";",
		":",
		"'",
		"\\",
		",",
		".",
		"/",
		"0",
		"1",
		"2",
		"3",
		"4",
		"5",
		"6",
		"7",
		"8",
		"9"
	]
	
	def __init__(self, icon_path=''):
		super(Ui_SimpleKeyboard, self).__init__()

		if icon_path != '':
			self.setWindowIcon(QtGui.QIcon(icon_path))
		
		if os.path.isfile('./style.css'):
			with open('./style.css', 'r', encoding='utf-8') as style:
				self.setStyleSheet(style.read())

		self.setObjectName("SimpleKeyboard")
		self.resize(800, 350)
		self.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
		self.centralwidget = QtWidgets.QWidget(self)
		self.centralwidget.setObjectName("centralwidget")
		self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
		self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 40, 661, 291))
		self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
		self.mainVerticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
		self.mainVerticalLayout.setContentsMargins(0, 0, 0, 0)
		self.mainVerticalLayout.setObjectName("mainVerticalLayout")
		self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_4.setObjectName("horizontalLayout_4")
		self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
		font = QtGui.QFont()
		font.setPointSize(16)
		self.lineEdit.setFont(font)
		self.lineEdit.setText("")
		self.lineEdit.setObjectName("lineEdit")
		self.horizontalLayout_4.addWidget(self.lineEdit)
		self.copyPushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.copyPushButton.sizePolicy().hasHeightForWidth())
		self.copyPushButton.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setPointSize(18)
		font.setBold(False)
		font.setWeight(50)
		self.copyPushButton.setFont(font)
		self.copyPushButton.setFocusPolicy(QtCore.Qt.NoFocus)
		self.copyPushButton.setObjectName("copyPushButton")
		self.horizontalLayout_4.addWidget(self.copyPushButton)
		self.pastePushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.pastePushButton.sizePolicy().hasHeightForWidth())
		self.pastePushButton.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setPointSize(18)
		font.setBold(False)
		font.setWeight(50)
		self.pastePushButton.setFont(font)
		self.pastePushButton.setFocusPolicy(QtCore.Qt.NoFocus)
		self.pastePushButton.setObjectName("pastePushButton")
		self.horizontalLayout_4.addWidget(self.pastePushButton)
		self.clearPushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.clearPushButton.sizePolicy().hasHeightForWidth())
		self.clearPushButton.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setPointSize(18)
		font.setBold(False)
		font.setWeight(50)
		self.clearPushButton.setFont(font)
		self.clearPushButton.setFocusPolicy(QtCore.Qt.NoFocus)
		self.clearPushButton.setObjectName("clearPushButton")
		self.horizontalLayout_4.addWidget(self.clearPushButton)
		self.mainVerticalLayout.addLayout(self.horizontalLayout_4)
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.leftPushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.leftPushButton.sizePolicy().hasHeightForWidth())
		self.leftPushButton.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setPointSize(34)
		self.leftPushButton.setFont(font)
		self.leftPushButton.setFocusPolicy(QtCore.Qt.NoFocus)
		self.leftPushButton.setObjectName("leftPushButton")
		self.horizontalLayout.addWidget(self.leftPushButton)
		self.middlePushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.middlePushButton.sizePolicy().hasHeightForWidth())
		self.middlePushButton.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setPointSize(34)
		self.middlePushButton.setFont(font)
		self.middlePushButton.setFocusPolicy(QtCore.Qt.NoFocus)
		self.middlePushButton.setObjectName("middlePushButton")
		self.horizontalLayout.addWidget(self.middlePushButton)
		self.rightPushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.rightPushButton.sizePolicy().hasHeightForWidth())
		self.rightPushButton.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setPointSize(34)
		font.setBold(False)
		font.setWeight(50)
		self.rightPushButton.setFont(font)
		self.rightPushButton.setFocusPolicy(QtCore.Qt.NoFocus)
		self.rightPushButton.setObjectName("rightPushButton")
		self.horizontalLayout.addWidget(self.rightPushButton)
		self.mainVerticalLayout.addLayout(self.horizontalLayout)
		self.spacePushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.spacePushButton.sizePolicy().hasHeightForWidth())
		self.spacePushButton.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setPointSize(18)
		font.setBold(False)
		font.setWeight(50)
		self.spacePushButton.setFont(font)
		self.spacePushButton.setFocusPolicy(QtCore.Qt.NoFocus)
		self.spacePushButton.setObjectName("spacePushButton")
		self.mainVerticalLayout.addWidget(self.spacePushButton)
		self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_3.setObjectName("horizontalLayout_3")
		self.backspacePushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.backspacePushButton.sizePolicy().hasHeightForWidth())
		self.backspacePushButton.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setPointSize(18)
		font.setBold(False)
		font.setWeight(50)
		self.backspacePushButton.setFont(font)
		self.backspacePushButton.setFocusPolicy(QtCore.Qt.NoFocus)
		self.backspacePushButton.setObjectName("backspacePushButton")
		self.horizontalLayout_3.addWidget(self.backspacePushButton)
		self.ChangePushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.ChangePushButton.sizePolicy().hasHeightForWidth())
		self.ChangePushButton.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setPointSize(18)
		font.setBold(False)
		font.setWeight(50)
		self.ChangePushButton.setFont(font)
		self.ChangePushButton.setFocusPolicy(QtCore.Qt.NoFocus)
		self.ChangePushButton.setObjectName("ChangePushButton")
		self.horizontalLayout_3.addWidget(self.ChangePushButton)
		self.shiftPushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.shiftPushButton.sizePolicy().hasHeightForWidth())
		self.shiftPushButton.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setPointSize(18)
		font.setBold(False)
		font.setWeight(50)
		self.shiftPushButton.setFont(font)
		self.shiftPushButton.setFocusPolicy(QtCore.Qt.NoFocus)
		self.shiftPushButton.setObjectName("shiftPushButton")
		self.horizontalLayout_3.addWidget(self.shiftPushButton)
		self.mainVerticalLayout.addLayout(self.horizontalLayout_3)
		self.setCentralWidget(self.centralwidget)

		# self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

		self.leftPushButton.setFocusPolicy(QtCore.Qt.NoFocus)
		self.middlePushButton.setFocusPolicy(QtCore.Qt.NoFocus)
		self.rightPushButton.setFocusPolicy(QtCore.Qt.NoFocus)
		self.shiftPushButton.setFocusPolicy(QtCore.Qt.NoFocus)
		self.ChangePushButton.setFocusPolicy(QtCore.Qt.NoFocus)
		self.backspacePushButton.setFocusPolicy(QtCore.Qt.NoFocus)
		self.spacePushButton.setFocusPolicy(QtCore.Qt.NoFocus)
		self.copyPushButton.setFocusPolicy(QtCore.Qt.NoFocus)
		self.pastePushButton.setFocusPolicy(QtCore.Qt.NoFocus)
		self.clearPushButton.setFocusPolicy(QtCore.Qt.NoFocus)

		self.setFocus()
		app.focusChanged.connect(self.onFocusChanged)

		QtCore.QMetaObject.connectSlotsByName(self)

		self.setWindowTitle("Simple Keyboard")
		self.ChangePushButton.setText("Change language")
		self.shiftPushButton.setText("Shift")
		self.copyPushButton.setText("Copy")
		self.pastePushButton.setText("Paste")
		self.clearPushButton.setText("Clear")
		self.backspacePushButton.setText("Backspace")
		self.spacePushButton.setText("Space")

		self.load_lang(self.lang_id)
		self.set_keys(self.select_button)
		self.set_font()

		self.resized.connect(self.auto_resize) # Делаю ивент на изменение размера окна

		self.pastePushButton.setShortcut(QKeySequence("Ctrl+V"))

		self.close_shortcut = QShortcut(QKeySequence("Esc"), self) # Выход при 'esc'
		self.close_shortcut.activated.connect(lambda: sys.exit(0))
		
		self.leftPushButton.clicked.connect(lambda: self.left_btn())
		self.middlePushButton.clicked.connect(lambda: self.set_symbol(self.middlePushButton.text()))
		self.rightPushButton.clicked.connect(lambda: self.right_btn())
		self.shiftPushButton.clicked.connect(lambda: self.shift_btn())
		self.ChangePushButton.clicked.connect(lambda: self.change_btn())
		self.backspacePushButton.clicked.connect(lambda: self.backspace_btn())
		self.clearPushButton.clicked.connect(lambda: self.clear_btn())
		self.spacePushButton.clicked.connect(lambda: self.set_symbol(" "))
		self.copyPushButton.clicked.connect(lambda: self.copy())
		self.pastePushButton.clicked.connect(lambda: self.paste())
	
	def resizeEvent(self, event):
		self.resized.emit()
		return super(Ui_SimpleKeyboard, self).resizeEvent(event)

	def auto_resize(self):
		self.verticalLayoutWidget.setGeometry(0,0, self.size().width(), self.size().height())
	
	def onFocusChanged(self):
		if not self.isActiveWindow() and config["General"]['auto_close'] == '1':
			self.close()
	
	def load_lang(self, id):
		with open('./langs.yml', 'r', encoding="utf-8") as yml:
			langs = yaml.load(yml, Loader=SafeLoader)

			if len(list(langs.keys()))-1 < id:
				id = 0
			
			lang = list(langs.keys())[id]
			self.alphet = langs[lang] + self.addition_symbols

			self.lang_id = id
			self.lang_name = lang
	
	def set_font(self):
		with open('./langs_settings.yml', 'r', encoding="utf-8") as yml:
			lang_data = yaml.load(yml, Loader=SafeLoader)[self.lang_name]

			font = QtGui.QFont()
			font.setFamily(lang_data['font'])

			font.setPointSize(lang_data['symbol buttons point size'])
			self.leftPushButton.setFont(font)
			self.middlePushButton.setFont(font)
			self.rightPushButton.setFont(font)

			font.setPointSize(lang_data['lineEdit button point size'])
			self.lineEdit.setFont(font)

			font.setPointSize(lang_data['up buttons point size'])
			self.copyPushButton.setFont(font)
			self.clearPushButton.setFont(font)
			self.pastePushButton.setFont(font)

			font.setPointSize(lang_data['space button point size'])
			self.spacePushButton.setFont(font)

			font.setPointSize(lang_data['down buttons point size'])
			self.backspacePushButton.setFont(font)
			self.ChangePushButton.setFont(font)
			self.shiftPushButton.setFont(font)

			self.ChangePushButton.setText(lang_data['change language button text'])
			self.shiftPushButton.setText(lang_data['shift button text'])
			self.copyPushButton.setText(lang_data['copy button text'])
			self.pastePushButton.setText(lang_data['paste button text'])
			self.clearPushButton.setText(lang_data['clear button text'])
			self.backspacePushButton.setText(lang_data['backspace button text'])
			self.spacePushButton.setText(lang_data['space button text'])
	
	def set_keys(self, n):
		l_btn = ''
		m_btn = ''
		r_btn = ''

		if n == -1:
			n = len(self.alphet)-1
			self.select_button = n 
		
		elif n == len(self.alphet):
			n = 0
			self.select_button = n 

		if n > 0 and n < len(self.alphet)-1:
			self.select_button = n

			if self.shift_active:
				l_btn = self.alphet[n-1].upper()
				m_btn = self.alphet[n].upper()
				r_btn = self.alphet[n+1].upper()
			
			else:
				l_btn = self.alphet[n-1].lower()
				m_btn = self.alphet[n].lower()
				r_btn = self.alphet[n+1].lower()
		
		elif n == 0:
			self.select_button = n

			if self.shift_active:
				l_btn = self.alphet[-1].upper()
				m_btn = self.alphet[n].upper()
				r_btn = self.alphet[n+1].upper()
			
			else:
				l_btn = self.alphet[-1].lower()
				m_btn = self.alphet[n].lower()
				r_btn = self.alphet[n+1].lower()
		
		elif n == len(self.alphet)-1:
			self.select_button = n

			if self.shift_active:
				l_btn = self.alphet[n-1].upper()
				m_btn = self.alphet[n].upper()
				r_btn = self.alphet[0].upper()
			
			else:
				l_btn = self.alphet[n-1].lower()
				m_btn = self.alphet[n].lower()
				r_btn = self.alphet[0].lower()
		
		self.leftPushButton.setText(f"{l_btn}\n←")
		self.middlePushButton.setText(f"{m_btn}")
		self.rightPushButton.setText(f"{r_btn}\n→")
	
	def change_btn(self):
		self.load_lang(self.lang_id+1)
		self.select_button = 0
		self.set_keys(self.select_button)
		self.set_font()

	def shift_btn(self):
		if self.shift_active:
			self.shift_active = False
		else:
			self.shift_active = True

		self.set_keys(self.select_button)

	def left_btn(self):
		self.set_keys(self.select_button-1)

	def right_btn(self):
		self.set_keys(self.select_button+1)
	
	def set_symbol(self, symbol):
		cursorPosition = self.lineEdit.cursorPosition()
		text = self.lineEdit.text()

		if len(text) != 0:
			text1 = text[:cursorPosition]
			text2 = text[cursorPosition:]

			self.lineEdit.setText(text1 + symbol + text2)
			self.lineEdit.setCursorPosition(cursorPosition+1)

		else:
			self.lineEdit.setText(self.lineEdit.text() + symbol)

	def clear_btn(self):
		self.lineEdit.setText("")
	
	def backspace_btn(self):
		cursorPosition = self.lineEdit.cursorPosition() - 1

		text = self.lineEdit.text()

		if len(text) != 0:
			text1 = text[:cursorPosition]
			text2 = ""

			if len(text) != cursorPosition:
				text2 = text[cursorPosition+1:]
			
			text = text1 + text2
		
			self.lineEdit.setText(text)
			self.lineEdit.setCursorPosition(cursorPosition)
	
	def copy(self):
		pyperclip.copy(self.lineEdit.text())
	
	def paste(self):
		self.set_symbol(str(pyperclip.paste()))

if __name__ == "__main__":
	config = configparser.ConfigParser()

	if not os.path.isfile('./config.ini'):
		config['General'] = {
			'auto_close': '1'
		}
		with open('./config.ini', 'w+', encoding='utf-8') as configfile:
			config.write(configfile)

	config.read('./config.ini', encoding='utf-8')

	app = QtWidgets.QApplication(sys.argv)

	global simple_keyboard
	simple_keyboard = Ui_SimpleKeyboard('./logo.png')
	simple_keyboard.show()

	sys.exit(app.exec_())
