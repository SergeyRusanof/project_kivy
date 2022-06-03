'''
Приложение "Список".
 Предназначено для удобного составления списка покупок
'''

from kivy.app import App
from kivy.properties import ColorProperty
from kivy.uix.button import Button
from kivy.config import Config

from kivy.uix.floatlayout import FloatLayout

from kivy.uix.boxlayout import BoxLayout

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '610')


class ListApp(App):
    def build(self):
        menu_list = BoxLayout()
        menu_list.add_widget(Button(text='1'))
        menu_list.add_widget(Button(text='1'))
        menu_list.add_widget(Button(text='1'))
        return menu_list


if __name__ == "__main__":
    ListApp().run()
