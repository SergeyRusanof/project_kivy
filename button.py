class MyApp(App):
    def build(self):
        fl = FloatLayout(size=(150, 150))
        fl.add_widget(
            Button(
                text="Кнопка",
                font_size=16,
                on_press=self.pushbutton,
                background_color=[.42, .32, .55, 1],
                background_normal='',
                size_hint = (.5, .10),
                pos = (150-75, 300)))
        return fl

    def pushbutton(self, instance):
        print('Кнопка нажата')
        instance.text = "Кнопка нажата"
