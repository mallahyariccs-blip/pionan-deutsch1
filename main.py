import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle

# تنظیم رنگ پس‌زمینه پنجره
Window.clearcolor = (0.1, 0.1, 0.3, 1)  # آبی تیره

class PimonDeutschApp(App):
    def build(self):
        # ساخت Layout اصلی
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # عنوان برنامه
        title_label = Label(
            text='PIONAN Deutsch Courses',
            font_size='28sp',
            bold=True,
            color=(1, 1, 1, 1)  # سفید
        )
        
        # زیرعنوان
        subtitle_label = Label(
            text='آموزش زبان آلمانی',
            font_size='22sp',
            color=(0.8, 0.8, 1, 1)  # آبی روشن
        )
        
        # دکمه‌های نمونه
        button_layout = BoxLayout(spacing=10, size_hint=(1, 0.3))
        
        btn_vocab = Button(
            text='📚 واژه‌نامه',
            background_color=(0.2, 0.6, 0.8, 1),
            bold=True
        )
        
        btn_quiz = Button(
            text='🧠 آزمون',
            background_color=(0.8, 0.5, 0.2, 1),
            bold=True
        )
        
        btn_lessons = Button(
            text='🎓 دروس',
            background_color=(0.3, 0.7, 0.4, 1),
            bold=True
        )
        
        # اضافه کردن ویجت‌ها به layout
        button_layout.add_widget(btn_vocab)
        button_layout.add_widget(btn_quiz)
        button_layout.add_widget(btn_lessons)
        
        layout.add_widget(title_label)
        layout.add_widget(subtitle_label)
        layout.add_widget(button_layout)
        
        # وضعیت پایین صفحه
        status_label = Label(
            text='آماده برای یادگیری...',
            font_size='16sp',
            color=(0.7, 0.7, 0.7, 1)
        )
        layout.add_widget(status_label)
        
        return layout

if __name__ == '__main__':
    PimonDeutschApp().run()
