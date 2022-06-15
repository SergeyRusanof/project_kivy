from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

Window.size = (300, 610)


class ShopListApp(App):
    # def update_label(self):
    #     self.label.text = self.inlist
    #
    # def choice_pay(self, instance):
    #     self.inlist += str(instance.text)
    #     self.update_label()

    def build(self):
        main_block = GridLayout(rows=2, padding=5)
        top_block = BoxLayout(orientation='horizontal', size_hint=[1,.5])
        amount = Label(text='am', size_hint=[.15, 1])
        check_box = Label(text='ch', size_hint=[.15, 1])
        bottom_block = GridLayout(rows=5, size_hint=[1,.5])
        show = TextInput(readonly=True)

        top_block.add_widget(show)
        top_block.add_widget(amount)
        top_block.add_widget(check_box)
        main_block.add_widget(top_block)
        main_block.add_widget(bottom_block)

        bottom_block.add_widget(Button(text='Молоко'))
        bottom_block.add_widget(Button(text='Молоко'))
        bottom_block.add_widget(Button(text='Молоко'))
        bottom_block.add_widget(Button(text='Молоко'))
        bottom_block.add_widget(Button(text='Молоко'))

        bottom_block.add_widget(Button(text='Молоко'))
        bottom_block.add_widget(Button(text='Молоко'))
        bottom_block.add_widget(Button(text='Молоко'))
        bottom_block.add_widget(Button(text='Молоко'))
        bottom_block.add_widget(Button(text='Молоко'))



        return main_block


if __name__ == "__main__":
    ShopListApp().run()
