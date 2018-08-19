from serial import Serial

class SerialLCD:
    def __init__(self, dev, baudrate=9600, **kwargs):
        self.ser = Serial(dev, baudrate, **kwargs)

    def __enter__(self):
        if not self.ser.is_open:
            self.ser.open()
            
        return self

    def __exit__(self, type, value, traceback):
        self.ser.close()

    def print(self, msg, row=1):
        self.write(row=row, msg=msg)
    
    def write(self, msg ,row=1, col=1):
        self.ser.write('$GO {} {}\n'.format(row, col).encode())
        self.ser.write('$PRINT {}\n'.format(msg).encode())

    def clear(self):
        self.ser.write('$CLEAR\n'.encode())
