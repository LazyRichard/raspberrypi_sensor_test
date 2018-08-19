import traceback
from time import sleep
from mcp3008 import MCP3008

adc = MCP3008()

def scaling(val, max, min=0):
    # max와 min 사이에 있는 val을 0과 1의 범위로 스케일링
    return (val - min) / float(max - min)

with adc as a:
    try:    
        while True:
            val_pot = a.read(0)
            val_cds = a.read(1)
            val_pot_p = round(scaling(val_pot, 1024) * 100, 2)
            val_cds_p = round(scaling(val_cds, 1024) * 100, 2)

            print('POT: {} {}%'.format(val_pot, val_pot_p))
            print('CDS: {} {}%'.format(val_cds, val_cds_p))
            print('-' * 20)

            sleep(1)
    except:
        traceback.print_exc()
