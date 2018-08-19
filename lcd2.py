import traceback
from datetime import datetime, timedelta, timezone
from time import sleep
from serialLcd import SerialLCD

serial_lcd = SerialLCD('/dev/serial0', 9600, writeTimeout=5)

tz_seoul = timezone(timedelta(hours=9))

with serial_lcd as lcd:
    try:
        lcd.clear()
        
        while True:
            now = datetime.now(timezone.utc)
            now_local = now.astimezone(tz_seoul)

            str_date = datetime.strftime(curr_time, '%y-%m-%d')
            str_time = datetime.strftime(curr_time, '%p %l:%M:%S')

            lcd.write('Today {}'.format(str_date))
            lcd.write('{}'.format(str_time, row=2, col=5))

            sleep(1)
    except:
        traceback.print_exc()
