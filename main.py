'''
Приложение "Список".
 Предназначено для удобного составления списка покупок
'''


from kivy.app import App
from kivy.properties import ColorProperty
from kivy.uix.button import Button

from kivy.config import Config

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '610')


class MyApp(App):
    def build(self):
        return Button(
            text="Кнопка",
            font_size=25,
            on_press =self.pushbutton,
            background_color = [.42,.32,.55, 1],
            background_normal = ''
        )

    def pushbutton(self, instance):
        print('Кнопка нажата')
        instance.text = "Кнопка нажата"



if __name__ == "__main__":
    MyApp().run()