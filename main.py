from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class Shield360App(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        layout.add_widget(Label(text='Shield360', font_size='32sp', bold=True))
        layout.add_widget(Label(text='Your Security App is Running!', font_size='18sp'))
        layout.add_widget(Label(text='Version 1.0 - By 01101562', font_size='14sp'))
        btn = Button(text='Activate Shield', size_hint=(1, 0.3))
        btn.bind(on_press=lambda x: setattr(btn, 'text', 'Shield Activated!'))
        layout.add_widget(btn)
        return layout

Shield360App().run()