from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image


# Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', 300)
Config.set('graphics', 'height', 610)


class Container(BoxLayout):
    pass

class ShopListApp(App):
    def update_label(self):
        self.label.text = self.inlist

    def choice_pay(self, instance):
        self.inlist += str(instance.text)
        self.update_label()

    def build(self):
        self.inlist = ""
        box = BoxLayout(orientation='vertical', padding=2)
        icons = GridLayout(rows=5, padding=2, spacing=1, size_hint=[1, .50])
        self.label = Label(text="Приветик) тут будет список",
                           text_size=(294, 605 * .5), font_size=14,
                           size_hint=[1, .50],
                           halign='left',
                           valign='top')
        box.add_widget(self.label)
        icons.add_widget(Button(text='Хлеб', background_color=[.20, .35, .25, 1], font_size=13, on_press=self.choice_pay))
        icons.add_widget(Button(text='Мясо',  background_color=[.20, .35, .25, 1], font_size=13, on_press=self.choice_pay))
        icons.add_widget(Button(text='Яйца',  background_color=[.20, .35, .25, 1], font_size=13, on_press=self.choice_pay))
        icons.add_widget(Button(text='Йогурты',  background_color=[.20, .35, .25, 1], font_size=13, on_press=self.choice_pay))

        icons.add_widget(Button(text='Чай', background_color=[.20, .35, .25, 1], font_size=13, on_press=self.choice_pay))
        icons.add_widget(Button(text='Печенье', background_color=[.20, .35, .25, 1], font_size=13, on_press=self.choice_pay))
        icons.add_widget(Button(text='Приправы', background_color=[.20, .35, .25, 1], font_size=13, on_press=self.choice_pay))
        icons.add_widget(Button(text='Картошка', background_color=[.20, .35, .25, 1], font_size=13, on_press=self.choice_pay))

        icons.add_widget(Button(text='Крупы', background_color=[.20, .35, .25, 1], font_size=13, on_press=self.choice_pay))
        icons.add_widget(Button(text='Макароны', background_color=[.20, .35, .25, 1], font_size=13, on_press=self.choice_pay))
        icons.add_widget(Button(text='Помидоры', background_color=[.20, .35, .25, 1], font_size=13, on_press=self.choice_pay))
        icons.add_widget(Button(text='Лук', background_color=[.20, .35, .25, 1], font_size=13, on_press=self.choice_pay))

        icons.add_widget(Button(text='Рыба', background_color=[.20, .35, .25, 1], font_size=13, on_press=self.choice_pay))
        icons.add_widget(Button(text='Соки', background_color=[.20, .35, .25, 1], font_size=13, on_press=self.choice_pay))
        icons.add_widget(Button(text='Шоколадка', background_color=[.20, .35, .25, 1], font_size=13, on_press=self.choice_pay))
        icons.add_widget(Button(text='Капуста', background_color=[.20, .35, .25, 1], font_size=13, on_press=self.choice_pay))

        box.add_widget(icons)
        return box


if __name__ == "__main__":
    ShopListApp().run()
