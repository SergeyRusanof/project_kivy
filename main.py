from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.config import Config

Config.set('kivy', 'keyboard_mode', 'systemanddock')
Window.size = (300, 610)


class ShopListApp(App):
    def update_label(self):
        self.show.text = self.inlist

    def choice_pay(self, instance):
        self.inlist += str(instance.text)
        self.update_label()

    def clean(self, instance):
        self.show.text = ''
        self.inlist = ''

    def build(self):
        self.inlist = ''
        main_block = GridLayout(rows=3, padding=5)
        top_block = BoxLayout(orientation='horizontal', size_hint=[1, .47])
        menu = BoxLayout(orientation='horizontal', size_hint=[.03, .03])
        bottom_block = GridLayout(rows=5, size_hint=[1, .47])
        self.show = TextInput(readonly=True, font_size='13', line_spacing='1', padding=[10, 1, 0, 1])
        self.show2 = TextInput( font_size='13', padding=[10, 1, 2, 1])

        top_block.add_widget(self.show)
        top_block.add_widget(self.show2)
        main_block.add_widget(top_block)
        main_block.add_widget(menu)
        main_block.add_widget(bottom_block)

        menu.add_widget(Button(text='Стереть', background_color=[.88,.35,.31, 1], font_size='11', on_press=self.clean))

        bottom_block.add_widget(Button(text='хлеб\n', background_color=[.22,.37,.64, 1], font_size='12', on_press=self.choice_pay))
        bottom_block.add_widget(Button(text='йогурты\n', background_color=[.22,.37,.64, 1], font_size='12', on_press=self.choice_pay))
        bottom_block.add_widget(Button(text='яйца\n', background_color=[.22,.37,.64, 1], font_size='12', on_press=self.choice_pay))
        bottom_block.add_widget(Button(text='шоколадка\n', background_color=[.22,.37,.64, 1], font_size='11', on_press=self.choice_pay))
        bottom_block.add_widget(Button(text='мясо\n', background_color=[.22,.37,.64, 1], font_size='12', on_press=self.choice_pay))

        bottom_block.add_widget(Button(text='помидоры\n', background_color=[.22,.37,.64, 1], font_size='11', on_press=self.choice_pay))
        bottom_block.add_widget(Button(text='огурцы\n', background_color=[.22,.37,.64, 1], font_size='12', on_press=self.choice_pay))
        bottom_block.add_widget(Button(text='лук\n', background_color=[.22,.37,.64, 1], font_size='12', on_press=self.choice_pay))
        bottom_block.add_widget(Button(text='печенье\n', background_color=[.22,.37,.64, 1], font_size='12', on_press=self.choice_pay))
        bottom_block.add_widget(Button(text='чай\n', background_color=[.22,.37,.64, 1], font_size='12', on_press=self.choice_pay))

        bottom_block.add_widget(Button(text='колбаса\n', background_color=[.22,.37,.64, 1], font_size='12', on_press=self.choice_pay))
        bottom_block.add_widget(Button(text='сырки\n', background_color=[.22,.37,.64, 1], font_size='12', on_press=self.choice_pay))
        bottom_block.add_widget(Button(text='косичка\n', background_color=[.22,.37,.64, 1], font_size='12', on_press=self.choice_pay))
        bottom_block.add_widget(Button(text='картошка\n', background_color=[.22,.37,.64, 1], font_size='11', on_press=self.choice_pay))
        bottom_block.add_widget(Button(text='рыба\n', background_color=[.22,.37,.64, 1], font_size='12', on_press=self.choice_pay))

        bottom_block.add_widget(Button(text='молоко\n', background_color=[.22,.37,.64, 1], font_size='12', on_press=self.choice_pay))
        bottom_block.add_widget(Button(text='приправы\n', background_color=[.22,.37,.64, 1], font_size='11', on_press=self.choice_pay))
        bottom_block.add_widget(Button(text='масло\n', background_color=[.22,.37,.64, 1], font_size='12', on_press=self.choice_pay))
        bottom_block.add_widget(Button(text='сахар\n', background_color=[.22,.37,.64, 1], font_size='12', on_press=self.choice_pay))
        bottom_block.add_widget(Button(text='майонез\n', background_color=[.22,.37,.64, 1], font_size='12', on_press=self.choice_pay))

        bottom_block.add_widget(Button(text='кетчуп\n', background_color=[.22,.37,.64, 1], font_size='12', on_press=self.choice_pay))
        bottom_block.add_widget(Button(text='рис\n', background_color=[.22,.37,.64, 1], font_size='12', on_press=self.choice_pay))
        bottom_block.add_widget(Button(text='гречка\n', background_color=[.22,.37,.64, 1], font_size='12', on_press=self.choice_pay))
        bottom_block.add_widget(Button(text='макароны\n', background_color=[.22,.37,.64, 1], font_size='11', on_press=self.choice_pay))
        bottom_block.add_widget(Button(text='мивина\n', background_color=[.22,.37,.64, 1], font_size='12', on_press=self.choice_pay))

        return main_block


if __name__ == "__main__":
    ShopListApp().run()
