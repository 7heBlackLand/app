from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
        self.label = Label(text="Hello from Kivy!", font_size=24)
        button = Button(text="Click Me", font_size=20, size_hint=(1, 0.3))
        button.bind(on_press=self.on_button_click)
        layout.add_widget(self.label)
        layout.add_widget(button)
        return layout

    def on_button_click(self, instance):
        self.label.text = "Button Clicked!"

if __name__ == "__main__":
    MyApp().run()
