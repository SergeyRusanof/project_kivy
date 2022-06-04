from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

# Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', 300)
Config.set('graphics', 'height', 610)


class ShopListApp(App):
    def build(self):
        box = BoxLayout(orientation='vertical', size_hint=[1, .40])
        box.add_widget(Label(text="Приветик) тут будет список", size_hint=[1, .40]))
        icons = GridLayout(rows=5, padding=2, size_hint=[1, .60])

        for i in range(20):
            icons.add_widget(Button(background_color=[.20, .35, .25, 1]))
        return box


if __name__ == "__main__":
    ShopListApp().run()
