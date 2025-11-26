"""
CP1404/CP5632 Practical - Suggested Solution
GUI program to convert miles to kilometres
Lindsay Ward, IT@JCU
Print statements included to see when functions run
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
                                             # eg: Numeric

FACTOR_MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """ Kivy App for converting miles to kilometres."""
    output_km = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, text):
        """ Handle calculation (could be button press or other call), output result to label widget """
        print("handle calculate")
        miles = self.convert_to_number(text)
        self.update_result(float(miles))

    def handle_increment(self, text, change):
        """Handle up/down button press, update the text input with new value, call calculation function :param change: the amount to change"""
        print("handle increment")
        miles = self.convert_to_number(text) + change
        self.root.ids.input_miles.text = str(miles)
        # Since the TextInput.text has changed, it's on_text event will trigger handle_calculate()

    def update_result(self, miles):
        """Convert mile to kilometer"""
        print("update")
        self.output_km = str(miles * FACTOR_MILES_TO_KM)

    @staticmethod
    def convert_to_number(text):
        """Convert text to float or 0.0 if invalid."""
        try:
            return float(text)
        except ValueError:
            return 0.0


MilesConverterApp().run()
