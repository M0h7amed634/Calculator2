from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class CalculatorApp(App):
    def build(self):
        # Main layout
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Input field
        self.result = TextInput(
            multiline=False,
            readonly=True,
            halign="right",
            font_size=32,
            background_color=(0.9, 0.9, 0.9, 1)
        )
        layout.add_widget(self.result)

        # Buttons layout
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["C", "0", ".", "+"],
            ["√", "="]
        ]

        for row in buttons:
            row_layout = BoxLayout(spacing=10)
            for label in row:
                button = Button(
                    text=label,
                    font_size=24,
                    background_color=(0.2, 0.6, 0.8, 1),  # لون الأزرق للأزرار
                    color=(1, 1, 1, 1)  # لون النص أبيض
                )
                button.bind(on_press=self.on_button_press)
                row_layout.add_widget(button)
            layout.add_widget(row_layout)

        return layout

    def on_button_press(self, instance):
        text = instance.text

        if text == "C":
            self.result.text = ""
        elif text == "=":
            try:
                self.result.text = str(eval(self.result.text))
            except Exception:
                self.result.text = "Error"
        elif text == "√":
            try:
                value = eval(self.result.text)
                self.result.text = str(value ** 2)  # مربع الرقم
            except Exception:
                self.result.text = "Error"
        else:
            self.result.text += text


if __name__ == "__main__":
    CalculatorApp().run()

