"""
Kivy Demo Program
Estimate: 15 minutes
Actual:
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

# Read KV file
Builder.load_file("kivy_layout.kv")

class MyRoot(BoxLayout):
    pass

class KivyDemoApp(App):
    def build(self):
        return MyRoot()

if __name__ == "__main__":
    KivyDemoApp().run()

