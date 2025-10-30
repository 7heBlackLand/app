from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text="হ্যালো, এটি আমার প্রথম Android অ্যাপ!")

if __name__ == "__main__":
    MyApp().run()
