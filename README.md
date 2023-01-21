# TS2 Simple Keyboard

![image](https://user-images.githubusercontent.com/66993983/213865476-f6c35e0b-36ef-49bb-b064-3226c053a430.png)

- [TS2 Simple Keyboard](#ts2-simple-keyboard)
	- [How to use](#how-to-use)
	- [How to setup](#how-to-setup)
		- [How to add a language](#how-to-add-a-language)
		- [How to set the language](#how-to-set-the-language)
		- [How to set the style sheet](#how-to-set-the-style-sheet)

## How to use

First open TS2_SimpleKeyboard.exe

- Side buttons are needed to switch letters between

![image](https://user-images.githubusercontent.com/66993983/213865545-dabd12e4-f235-4e6f-826d-99fd9c18f918.png)

- When you click on the button in the middle, it is printed in a line.

![image](https://user-images.githubusercontent.com/66993983/213865604-e6c681bc-a9a8-4bd0-b538-962131eaef56.png)

- Space - Space

- Backspace - Erase a letter

- Shift - Use capital/small letters

- Change language - Change language

![image](https://user-images.githubusercontent.com/66993983/213865775-94bde41a-d9f1-440b-98d6-f353a0afb32f.png)

- Copy - Copy typed text
- Paste - Paste copied text
- Clear - Clear input line

![image](https://user-images.githubusercontent.com/66993983/213865855-a735608e-e711-43eb-8eb2-c69fb58056f4.png)

## How to setup

There are 3 files in the application root folder:
- langs.yml
- langs_settings.yml
- style.css
- config.ini

![image](https://user-images.githubusercontent.com/66993983/213864828-694ea90e-e01d-47c0-9c74-30fe5395d456.png)

### How to add a language

1) Open langs.yml
2) At the very bottom, add the line "\<Language name\>:"
3) Under the added line, add all the letters of the alphabet in the format "- "\<letter\>" "
4) Ready

### How to set the language

1) Open langs_settings.yml
2) Copy the existing language settings in the file.
3) Instead of the name of the language of the copied language, indicate the language you need
4) Now you can change the font and also adjust its size. You can also change the button text.


![image](https://user-images.githubusercontent.com/66993983/213865146-0dc4e1f9-07d3-4e41-8a9c-803c3c02f2f6.png)

### How to set the style sheet

1) Open style.css
2) Now you can specify the styles sheet you need

You can use the following classes:

- .QWidget - styles sheet for window
  
- .QPushButton - styles sheet for buttons
  
- .QLineEdit - styles sheet for line edit