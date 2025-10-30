from kivy.app import App
from kivy.uix.label import Label

class HelloApp(App):
    def build(self):
        return Label(text="Hello from Kivy + Buildozer + GitHub Actions!", font_size='20sp')

if __name__ == "__main__":
    HelloApp().run()
