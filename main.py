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

        menu.add_widget(Button(text='Стереть', font_size='11', on_press=self.clean))

        bottom_block.add_widget(Button(text='хлеб\n', font_size='12', on_press=self.choice_pay))
        bottom_block.add_widget(Button(text='йогурты\n', font_size='12', on_press=self.choice_pay))
        bottom_block.add_widget(Button(text='яйца\n', font_size='12', on_press=self.choice_pay))
        bottom_block.add_widget(Button(text='шоколадка\n', font_size='11', on_press=self.choice_pay))
        bottom_block.add_widget(Button(text='мясо\n', font_size='12', on_press=self.choice_pay))

        bottom_block.add_widget(Button(text='помидоры\n', font_size='11', on_press=self.choice_pay))
        bottom_block.add_widget(Button(text='огурцы\n', font_size='12', on_press=self.choice_pay))
        bottom_block.add_widget(Button(text='лук\n', font_size='12', on_press=self.choice_pay))
        bottom_block.add_widget(Button(text='печенье\n', font_size='12', on_press=self.choice_pay))
        bottom_block.add_widget(Button(text='чай\n', font_size='12', on_press=self.choice_pay))

        bottom_block.add_widget(Button(text='колбаса\n', font_size='12', on_press=self.choice_pay))
        bottom_block.add_widget(Button(text='сырки\n', font_size='12', on_press=self.choice_pay))
        bottom_block.add_widget(Button(text='косичка\n', font_size='12', on_press=self.choice_pay))
        bottom_block.add_widget(Button(text='картошка\n', font_size='11', on_press=self.choice_pay))
        bottom_block.add_widget(Button(text='рыба\n', font_size='12', on_press=self.choice_pay))

        bottom_block.add_widget(Button(text='молоко\n', font_size='12', on_press=self.choice_pay))
        bottom_block.add_widget(Button(text='приправы\n', font_size='11', on_press=self.choice_pay))
        bottom_block.add_widget(Button(text='масло\n', font_size='12', on_press=self.choice_pay))
        bottom_block.add_widget(Button(text='сахар\n', font_size='12', on_press=self.choice_pay))
        bottom_block.add_widget(Button(text='майонез\n', font_size='12', on_press=self.choice_pay))

        bottom_block.add_widget(Button(text='кетчуп\n', font_size='12', on_press=self.choice_pay))
        bottom_block.add_widget(Button(text='рис\n', font_size='12', on_press=self.choice_pay))
        bottom_block.add_widget(Button(text='гречка\n', font_size='12', on_press=self.choice_pay))
        bottom_block.add_widget(Button(text='макароны\n', font_size='11', on_press=self.choice_pay))
        bottom_block.add_widget(Button(text='мивина\n', font_size='12', on_press=self.choice_pay))

        return main_block


if __name__ == "__main__":
    ShopListApp().run()
