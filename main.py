from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
import os

Window.size = (500, 750)
Window.title = "PIONAN Deutsch Courses"

class PIONANApp(App):
    def build(self):
        # اسکرول ویو برای محتوای زیاد
        scroll = ScrollView(size_hint=(1, 1))
        main_layout = BoxLayout(orientation='vertical',
                               size_hint_y=None,
                               padding=20,
                               spacing=15)
        main_layout.bind(minimum_height=main_layout.setter('height'))
        
        # عنوان
        title = Label(text='[size=28][b]PIONAN Deutsch Courses[/b][/size]',
                     markup=True,
                     size_hint_y=None,
                     height=80,
                     color=(0, 0.3, 0.6, 1))
        main_layout.add_widget(title)
        
        # زیرعنوان
        subtitle = Label(text='Complete German Learning Collection\n(400+ MB Audio Content)',
                        size_hint_y=None,
                        height=60)
        main_layout.add_widget(subtitle)
        
        # دکمه‌های اصلی
        main_layout.add_widget(Label(text='[b]MAIN MENU:[/b]', 
                                    markup=True,
                                    size_hint_y=None,
                                    height=40))
        
        # دکمه راهنما و ثبت‌نام
        for name, file in [('📘 User Guide', 'Guide.html'),
                          ('📝 Registration', 'RegisterActivity.html')]:
            btn = Button(text=name,
                        size_hint_y=None,
                        height=70,
                        background_color=(0.3, 0.5, 0.8, 1))
            btn.file_path = f"Docs/{file}"
            btn.bind(on_press=self.open_file)
            main_layout.add_widget(btn)
        
        # لیست دوره‌ها
        main_layout.add_widget(Label(text='\n[b]COURSES:[/b]',
                                    markup=True,
                                    size_hint_y=None,
                                    height=40))
        
        # پیدا کردن همه دوره‌ها
        courses = self.find_courses()
        
        if courses:
            for course_name, course_path in courses:
                btn = Button(text=f"🎧 {course_name}",
                           size_hint_y=None,
                           height=60,
                           background_color=(0.2, 0.7, 0.4, 1))
                btn.course_path = course_path
                btn.bind(on_press=self.open_course)
                main_layout.add_widget(btn)
        else:
            main_layout.add_widget(Label(text='No courses found in Docs/',
                                        size_hint_y=None,
                                        height=50,
                                        color=(1, 0, 0, 1)))
        
        # اطلاعات پایین
        info = Label(text='\nAudio files installed separately\nTotal: ~400 MB MP3 files',
                    size_hint_y=None,
                    height=80,
                    color=(0.6, 0.2, 0, 1))
        main_layout.add_widget(info)
        
        scroll.add_widget(main_layout)
        return scroll
    
    def find_courses(self):
        """پیدا کردن همه دوره‌ها در پوشه Docs"""
        courses = []
        docs_path = "Docs"
        
        if os.path.exists(docs_path):
            for item in os.listdir(docs_path):
                item_path = os.path.join(docs_path, item)
                if os.path.isdir(item_path) and not item.startswith('.'):
                    # نمایش نام کوتاه‌تر
                    display_name = item
                    if len(display_name) > 30:
                        display_name = display_name[:27] + "..."
                    courses.append((display_name, item_path))
        
        # مرتب کردن
        courses.sort()
        return courses
    
    def open_file(self, instance):
        """باز کردن فایل HTML"""
        file_path = instance.file_path
        print(f"\n📄 Opening: {file_path}")
        
        if os.path.exists(file_path):
            print("✅ File exists")
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    first_lines = [f.readline().strip() for _ in range(3)]
                    print("Preview:", [line for line in first_lines if line])
            except Exception as e:
                print(f"⚠️ Error: {e}")
        else:
            print("❌ File not found")
            
            # بررسی ساختار
            print("\n📁 Checking Docs structure:")
            if os.path.exists("Docs"):
                items = os.listdir("Docs")
                print(f"Found {len(items)} items in Docs/:")
                for item in items[:10]:  # 10 تا اول
                    print(f"  - {item}")
    
    def open_course(self, instance):
        """باز کردن دوره"""
        course_path = instance.course_path
        course_name = os.path.basename(course_path)
        
        print(f"\n{'='*60}")
        print(f"🎓 COURSE: {course_name}")
        print(f"📁 Path: {course_path}")
        print('='*60)
        
        # بررسی محتوای دوره
        if os.path.exists(course_path):
            # شمارش فایل‌ها
            html_files = []
            mp3_files = []
            
            for root, dirs, files in os.walk(course_path):
                for file in files:
                    if file.endswith('.html'):
                        html_files.append(os.path.join(root, file))
                    elif file.endswith('.mp3'):
                        mp3_files.append(os.path.join(root, file))
            
            print(f"📊 Course contains:")
            print(f"  • {len(html_files)} HTML files")
            print(f"  • {len(mp3_files)} MP3 files")
            
            # نمایش ۳ فایل اول
            if html_files:
                print(f"\n📄 Sample HTML files:")
                for html in html_files[:3]:
                    rel_path = os.path.relpath(html, course_path)
                    print(f"  - {rel_path}")
            
            if mp3_files:
                print(f"\n🎵 Sample MP3 files:")
                for mp3 in mp3_files[:3]:
                    rel_path = os.path.relpath(mp3, course_path)
                    print(f"  - {rel_path}")
            
            print(f"\n💾 Total course size: estimated {len(mp3_files) * 5} MB")
        else:
            print("❌ Course folder not found!")

if __name__ == "__main__":
    print("Starting PIONAN Deutsch Courses App...")
    print("=" * 60)
    PIONANApp().run()