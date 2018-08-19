from spidev import SpiDev

class MCP3008:
    def __init__(self, bus=0, dev=0, max_speed_hz=7629):
        self.bus = bus
        self.dev = dev
        self.max_speed_hz = max_speed_hz
        
        self.spi = SpiDev()
    
    def __enter__(self):
        self.open()
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def read(self, ch=0):
        if ch > 7 or ch < 0:
            return -1
        
        r = self.spi.xfer2([1, 8 + ch << 4, 0])
        data = ((r[1] & 3) << 8) + r[2]

        return data

    def open(self):
        self.spi.open(self.bus, self.dev)
        self.spi.max_speed_hz = self.max_speed_hz

    def close(self):
        self.spi.close()
