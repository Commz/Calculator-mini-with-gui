from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.config import Config
from kivy.core.window import Window

#Window.size = (1080//2, 2220//2)

Window.clearcolor = (1, 1, 1, 1)
appendCalcStr = ""
saveStr = ""
operStr = ""

class Calculator(FloatLayout):

    def updateGui(self, num):
        global appendCalcStr
        appendCalcStr = appendCalcStr + num
        self.label.text = appendCalcStr

    def opFunc(self, operator):
        global saveStr
        global operStr
        global appendCalcStr
        saveStr = appendCalcStr
        appendCalcStr = ""
        operStr = operator
        self.label.text = ""

    def delFunc(self):
        global saveStr
        global operStr
        global appendCalcStr
        self.label.text = ""
        saveStr = ""
        operStr = ""
        appendCalcStr = ""

    def equalFunc(self):
        global operStr
        global saveStr
        global appendCalcStr
        final = ""
        try:
            if operStr == "+":
                final = float(saveStr) + float(appendCalcStr)
                saveStr = final

            elif operStr == "-":
                final = float(saveStr) - float(appendCalcStr)
                saveStr = final

            elif operStr == "/":
                if appendCalcStr == "0":
                    self.label.text = "Can't divide by 0"
                else:
                    final = float(saveStr) / float(appendCalcStr)
                    saveStr = final

            elif operStr == "*":
                final = float(saveStr) * float(appendCalcStr)
                saveStr = final

            strFinal = str(final)
            if strFinal[-1] == "0" and strFinal[-2] == ".":
                self.label.text = strFinal[0:len(strFinal)-2]
        except (ValueError, IndexError) as e:
            pass

class MyApp(App):
    def build(self):
        return Calculator()

if __name__=="__main__":
    MyApp().run()
