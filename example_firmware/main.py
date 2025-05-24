# You import all the IOs of your board
import board

# These are imports from the kmk and neopixel library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from neopixel import NeoPixel

# This is the main instance of your keyboard
keyboard = KMKKeyboard()
# This is the NeoPixel code.
pin = board.D14   # set D14 pin (aka: GDIO17) for NeoPixel data
neo = NeoPixel(pin, 1)   # create NeoPixel driver on GPIO48 for 1 pixel
neo[0] = (255, 255, 255) # set the first pixel to white
neo.write()              # write data to all pixels
r, g, b = neo[0]         # get first pixel colour
# This is the code for the OLED.
# create I2C interface
i2c = machine.I2C(1, sda=board.D4, scl=board.D5)
print(i2c.scan())

# create SSD1306 interface
display_width:int = 128
display_height:int = 64
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
# display text
oled.text("Hello, world!", 0, 0) # print text "Hello, world!" at position (0, 0) (top left)
oled.show()
# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Define your pins here!
PINS = [board.D18, board.D17, board.D16, board.D15]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [KC.A, KC.B, KC.C, KC.Macro("Hello World!"),]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()