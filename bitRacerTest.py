from microbit import *
import bitRacer
bitRacer.motorRun(2,0)

def cali():
    bitRacer.motorRun(0,300)
    bitRacer.motorRun(1,-300)
    bitRacer.CalibrateBegin()
    t = running_time()
    while running_time()  < (t + 5000):
        pass
    bitRacer.motorRun(2,0)
    bitRacer.CalibrateEnd('BLACK')

lastdi = 0
PID_Val = 0
Error_P_old = 0
Error_D = 0
Error_P = 0
def PD(v, kP, kD, di):
    global lastdi,Error_P_old,Error_D,Error_P
    if(lastdi==0):
        lastdi = di
    else:
        lastdi-=1
    err = bitRacer.readLine()
    #// Error_P = 0 - 線位置
    Error_P = 0 - err - lastdi*0.001
    Error_D = Error_P - Error_P_old
    Error_P_old = Error_P
    PID_Val = int( Error_P * kP + Error_D * kD )
    bitRacer.motorRun(0, min( max(v + PID_Val, -1000), 1000))
    bitRacer.motorRun(1, min( max(v - PID_Val, -1000), 1000))

def go():
    while True:
        PD(300, 600, 1400, 0)


while True:
    if button_a.was_pressed():
        cali()
    if button_b.was_pressed():
        go()
