'''
Приложение "Список".
 Предназначено для удобного составления списка покупок
'''


from kivy.app import App
from kivy.properties import ColorProperty
from kivy.uix.button import Button
from kivy.config import Config

from kivy.uix.floatlayout import FloatLayout

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '610')


class MyApp(App):
    def build(self):
        fl = FloatLayout(size=(150, 150))
        fl.add_widget(
            Button(
                text="Кнопка",
                font_size=16,
                on_press=self.pushbutton,
                background_color=[.42, .32, .55, 1],
                background_normal='',
                size_hint = (.5, .25),
                pos = (0, 0)))
        return fl

    def pushbutton(self, instance):
        print('Кнопка нажата')
        instance.text = "Кнопка нажата"



if __name__ == "__main__":
    MyApp().run()