from kanowand import Wand, PATTERN

# Custom wand class extending the default wand
class MyWand(Wand):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.colors = ["#a333c8", "2185d0", "0x21ba45", "#fbbd08", "#f2711c", "#db2828"]

    # Do some functions after connecting
    def post_connect(self):
        print("Connected to {}".format(self.name))
        # Vibrate the wand and set its color to red
        self.vibrate(PATTERN.BURST)
        self.set_led(self.colors.pop())
        # Subscribe to notifications
        self.subscribe_button()
        self.subscribe_position()

    # Button callback, automatically called after connecting to wand
    def on_button(self, pressed):
        if pressed:
            self.unsubscribe_position()
            # Update the led
            self.set_led(self.colors.pop())
            # Disconnect if we run out of colors
            if len(self.colors) == 0:
                self.disconnect()

    # Position callback, automatically called after connecting to wand
    def on_position(self, x, y, pitch, roll):
        pitch = "Pitch: {}".format(pitch).ljust(16)
        roll = "Roll: {}".format(roll).ljust(16)
        print("{}{}(x, y): ({}, {})".format(pitch, roll, x, y))