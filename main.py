from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
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
        top_block = BoxLayout(orientation='horizontal', size_hint=[1,.45])
        amount = Label(text='am', size_hint=[.15, 1])
        check_box = Label(text='ch', size_hint=[.15, 1])
        menu = BoxLayout(orientation='horizontal', size_hint=[.05,.05])
        bottom_block = GridLayout(rows=5, size_hint=[1,.45])
        self.show = TextInput(readonly=True, font_size='13')
        scroll = ScrollView(size='')

        self.show.add_widget(scroll)
        top_block.add_widget(self.show)
        top_block.add_widget(amount)
        top_block.add_widget(check_box)
        main_block.add_widget(top_block)
        main_block.add_widget(menu)
        main_block.add_widget(bottom_block)

        menu.add_widget(Button(text='Продукты', font_size='11'))
        menu.add_widget(Button(text='Быт.хим.', font_size='11'))
        menu.add_widget(Button(text='Разное', font_size='11'))
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
