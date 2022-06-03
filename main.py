'''
Приложение "Список".
 Предназначено для удобного составления списка покупок
'''

from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

# Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '610')


class ListPayApp(App):
    def build(self):
        show_list = BoxLayout(orientation='vertical', padding=5)  # мониторчик с выводом списка
        show_list.add_widget(Label(text='Text', font_size=20, size_hint=[1, .50]))
        menu_list = GridLayout(cols=5, padding=2, spacing=1, size_hint=[1, .50])  # кнопки с наименованиями
        for x in range(20):
            menu_list.add_widget(Button(background_color=[.20, .35, .25, 1]))

        return menu_list


if __name__ == "__main__":
    ListPayApp().run()
