'''
Приложение "Список".
 Предназначено для удобного составления списка покупок
'''

from kivy.app import App
from kivy.properties import ColorProperty
from kivy.uix.button import Button
from kivy.config import Config

from kivy.uix.floatlayout import FloatLayout

from kivy.uix.gridlayout import GridLayout

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '610')


class ListApp(App):
    def build(self):
        menu_list = GridLayout(cols=6, padding=[0,250,0,0])

        for x in range(36):
            menu_list.add_widget(Button(text='ok'))

        return menu_list


if __name__ == "__main__":
    ListApp().run()
