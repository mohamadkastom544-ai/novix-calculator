
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

class CalculatorApp(App):

    def build(self):
        Window.clearcolor = (0.04, 0.04, 0.09, 1)

        self.first = None
        self.operator = None
        self.new_number = True

        main = BoxLayout(
            orientation="vertical",
            padding=15,
            spacing=12
        )

        title = Label(
            text="NOVIX CALCULATOR",
            font_size=23,
            size_hint=(1, 0.15),
            color=(0.6, 0.5, 1, 1)
        )

        main.add_widget(title)

        self.display = Label(
            text="0",
            font_size=45,
            size_hint=(1, 0.25)
        )

        main.add_widget(self.display)

        grid = GridLayout(cols=4, spacing=9)

        buttons = [
            "7", "8", "9", "÷",
            "4", "5", "6", "×",
            "1", "2", "3", "-",
            "C", "0", ".", "+",
            "=", "", "", ""
        ]

        for item in buttons:
            if item == "":
                grid.add_widget(Label())
                continue

            color = (0.3, 0.2, 0.55, 1)

            if item == "C":
                color = (0.8, 0.2, 0.25, 1)
            elif item in ["+", "-", "×", "÷", "="]:
                color = (0.1, 0.55, 0.7, 1)

            btn = Button(
                text=item,
                font_size=25,
                background_normal="",
                background_color=color
            )

            btn.bind(on_press=self.press)
            grid.add_widget(btn)

        main.add_widget(grid)
        return main

    def press(self, btn):
        value = btn.text

        if value.isdigit():
            if self.new_number or self.display.text == "0":
                self.display.text = value
                self.new_number = False
            else:
                self.display.text += value

        elif value == ".":
            if self.new_number:
                self.display.text = "0."
                self.new_number = False
            elif "." not in self.display.text:
                self.display.text += "."

        elif value == "C":
            self.display.text = "0"
            self.first = None
            self.operator = None
            self.new_number = True

        elif value in ["+", "-", "×", "÷"]:
            self.first = float(self.display.text)
            self.operator = value
            self.new_number = True

        elif value == "=":
            if self.first is None or self.operator is None:
                return

            second = float(self.display.text)

            if self.operator == "+":
                result = self.first + second
            elif self.operator == "-":
                result = self.first - second
            elif self.operator == "×":
                result = self.first * second
            else:
                if second == 0:
                    self.display.text = "Error"
                    self.first = None
                    self.operator = None
                    self.new_number = True
                    return
                result = self.first / second

            self.display.text = str(round(result, 8))
            self.first = None
            self.operator = None
            self.new_number = True

CalculatorApp().run()
main
