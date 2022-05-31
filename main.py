from kivy.app import App
from kivy.properties import ColorProperty
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        return Button(
            text="Кнопка",
            font_size=25,
            on_press =self.pushbutton,
            background_color = [1, 0, 0, 1],
            background_normal = ''
        )

    def pushbutton(self, instance):
        print('Кнопка нажата')
        instance.text = "Кнопка нажата"



if __name__ == "__main__":
    MyApp().run()