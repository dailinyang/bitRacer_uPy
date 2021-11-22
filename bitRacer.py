from microbit import *
import struct

#motorRun(index: Motors, PWM: number)
#PWM.min=-1000 PWM.max=1000
#motor right:0, left:1, all:2
def motorRun(index, PWM):
    if(index == 0):
        i2c.write(0x10, struct.pack('BBB', 0x02, (PWM>>8), PWM ))
    elif(index == 1):
        i2c.write(0x10, struct.pack('BBB', 0x00, (PWM>>8), PWM ))
    elif(index ==2):
        i2c.write(0x10, struct.pack('BBB', 0x02, (PWM>>8), PWM ))
        i2c.write(0x10, struct.pack('BBB', 0x00, (PWM>>8), PWM ))

#CalibrateBegin
def CalibrateBegin():
    i2c.write(0x10, struct.pack('B',0x09))

#CalibrateEnd
#White = 0x0A,
#Black = 0x0B
def CalibrateEnd(color:str):
    if color=='WHITE':
        i2c.write(0x10, struct.pack('B',0x0A))
    else:
        i2c.write(0x10, struct.pack('B',0x0B))

#read IR2
#leftmost = 0 , rightmost = 4
def readIR2(i:int):
    if (0<=i<=4):
        #i2c.write(0x10, struct.pack('B',i+3));a,=struct.unpack('>H',i2c.read(0x10, 2 ));print(a);
        i2c.write(0x10, struct.pack('B',i+3))
        return struct.unpack('>H',i2c.read(0x10, 2 ))[0]
    else:
        raise ValueError('IR value in [0~4]')

#readLine
def readLine():
    #i2c.write(0x10, struct.pack('B',0x08));a,=struct.unpack('>h',i2c.read(0x10, 2 ));print(a);
    i2c.write(0x10, struct.pack('B',0x08))
    return struct.unpack('>h',i2c.read(0x10, 2 ))[0] / 1000

#a,=struct.unpack('b',i2c.read(0x12,4))
