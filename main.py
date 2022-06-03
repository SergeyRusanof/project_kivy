'''
Приложение "Список".
 Предназначено для удобного составления списка покупок
'''

from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config

from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout

# Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '610')


class ListApp(App):
    def build(self):
        main_list = AnchorLayout(anchor_y='bottom')
        main_list.add_widget(Button(text='List body',
                                    background_color=[.60,.38,.71,1],
                                    background_normal=''))

        menu_list = GridLayout(cols=6, spacing=1, size_hint=[None, None], size=[300, 300])

        for x in range(36):
            menu_list.add_widget(Button(text='ok'))
        main_list.add_widget(menu_list)
        return main_list


if __name__ == "__main__":
    ListApp().run()
