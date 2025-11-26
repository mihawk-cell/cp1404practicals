from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label  #import the Label class
# the kivy.uix.label module. The Label class allows you
# to create a text label in your Kivy application
# to display static text or be dynamically updated.
from kivy.properties import StringProperty #StringProperty
# is used to create a property that holds a string value.
# It can be dynamically updated and make changes to the
# property in Kivy application.

NEW_COLOUR = (1, 0, 0, 1)  # RGBA for red
ALTERNATIVE_COLOUR = (1, 0, 1, 1)


class DynamicLabelsApp(App):
    name_display = StringProperty()

    def __init__(self, **kwargs):
        """Initialise construct """
        super().__init__(**kwargs)
        self.name_to_phone = {"Bob Brown": "0414144411", "Cat Cyan": "0441411211", "Oren Ochre": "0432123456"}

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create buttons from data and add them to the GUI."""
        for name in self.name_to_phone:
            temp_label = Label(text=name)
            temp_label.color = NEW_COLOUR
            self.root.ids.label_box.add_widget(temp_label)
            # add_widget() is a method is used to add a child
            # It allows to build complex layouts by nesting widget
            # Here's a breakdown of how add_widget() works within
            # Parent Widget: The widget to which you want to add
            # Child Widget: The widget that you want to add to that


DynamicLabelsApp().run()