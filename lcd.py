import traceback
from serialLcd import SerialLCD

serial_lcd = SerialLCD('/dev/serial0', 9600, writeTimeout=5)

with serial_lcd as lcd:
    try:
        lcd.clear()
        lcd.print('Hello LCD');
    except:
        traceback.print_exc()
