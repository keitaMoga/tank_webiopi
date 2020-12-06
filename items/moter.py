import webiopi
import time
import Adafruit_PCA9685

PWM_FREQUENCY=60

R_MOTER_FWD_CH = 7
R_MOTER_BCK_CH = 6
L_MOTER_FWD_CH = 8
L_MOTER_BCK_CH = 9
R_SERVO_CH = 4
L_SERVO_CH = 11

MIN_SERVO_PULSE_WIDH=150
MAX_SERVO_PULSE_WIDH=450

MAX_PULSE_WIDTH=1250

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(PWM_FREQUENCY)

r_servo_val=MIN_SERVO_PULSE_WIDH
l_servo_val=MIN_SERVO_PULSE_WIDH

def right_servo_controller(r_servo_state):
    if r_servo_state != 0:
        global r_servo_val
        r_servo_val = r_servo_val + r_servo_state
        if r_servo_val < MIN_SERVO_PULSE_WIDH or r_servo_val > MAX_SERVO_PULSE_WIDH:
            r_servo_val = r_servo_val - r_servo_state
        else:
            pwm.set_pwm(R_SERVO_CH, 0, global r_servo_val)

def left_servo_controller(l_servo_state):
    if l_servo_state != 0:
        global l_servo_val
        l_servo_val = l_servo_val + l_servo_state
        if l_servo_val < MIN_SERVO_PULSE_WIDH or l_servo_val > MAX_SERVO_PULSE_WIDH:
            l_servo_val = l_servo_val - l_servo_state
        else:
            pwm.set_pwm(L_SERVO_CH, 0, global l_servo_val)

def loop():
    webiopi.sleep(1)

@webiopi.macro
def right_moter_forward():
    pwm.set_pwm(R_MOTER_FWD_CH, 0, MAX_PULSE_WIDTH)

@webiopi.macro
def right_moter_back():
    pwm.set_pwm(R_MOTER_BCK_CH, 0, MAX_PULSE_WIDTH)

@webiopi.macro
def right_moter_stop():
    pwm.set_pwm(R_MOTER_FWD_CH, 0, 0)
    pwm.set_pwm(R_MOTER_BCK_CH, 0, 0)

@webiopi.macro
def left_moter_forward():
    pwm.set_pwm(L_MOTER_FWD_CH, 0, MAX_PULSE_WIDTH)

@webiopi.macro
def left_moter_back():
    pwm.set_pwm(L_MOTER_BCK_CH, 0, MAX_PULSE_WIDTH)

@webiopi.macro
def left_moter_stop():
    pwm.set_pwm(L_MOTER_FWD_CH, 0, 0)
    pwm.set_pwm(L_MOTER_BCK_CH, 0, 0)

@webiopi.macro
def right_servo_forward():
    right_servo_controller(1)

@webiopi.macro
def right_servo_back():
    right_servo_controller(-1)

@webiopi.macro
def right_servo_stop():
    right_servo_controller(0)

@webiopi.macro
def left_servo_forward():
    left_servo_controller(1)

@webiopi.macro
def left_servo_back():
    left_servo_controller(-1)

@webiopi.macro
def left_servo_stop():
    left_servo_controller(0)
