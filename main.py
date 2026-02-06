import kivy
kivy.require('2.0.0')
from kivy.app import App
from kivy.uix.label import Label

class PimonApp(App):
    def build(self):
        return Label(text='PIONAN Deutsch')

if __name__ == '__main__':
    PimonApp().run()
