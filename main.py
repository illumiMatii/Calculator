#kivy.require("1.10.1")
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config


class CalculatorLayout(GridLayout):
    def calc(self, calculate):
        if calculate:
            try:
                self.display.text = str(eval(calculate))
            except Exception:
                self.display.text = "ERROR"


class CalculatorApp(App):
    def build(self):
        Config.set("graphics", "width", "430")
        Config.set("graphics", "height", "600")
        Config.set("graphics", "resizable", "0")
        return CalculatorLayout()


if __name__ == "__main__":
    CalculatorApp().run()



'''
<Widgets>:
    Button:
        text: "1"
        size: 100, 75
        pos: 0, 0
        color: 0, 1, 0, 1
        font_size: 32
'''