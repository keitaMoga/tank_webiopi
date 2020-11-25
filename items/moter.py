import webiopi
import time
import Adafruit_PCA9685

PWM_FREQUENCY=60

R_MOTOR_FWD_CH = 7
R_MOTOR_BCK_CH = 6
L_MOTOR_FWD_CH = 8
L_MOTOR_BCK_CH = 9
R_SERVO_CH = 4
L_SERVO_CH = 11

MIN_SERVO_PULSE_WIDH=150
MAX_SERVO_PULSE_WIDH=450

MAX_PULSE_WIDTH=1250

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(PWM_FREQUENCY)

def loop():
    webiopi.sleep(1)

@webiopi.macro
def right_motor_forward():
    pwm.set_pwm(R_MOTOR_FWD_CH, 0, MAX_PULSE_WIDTH)

@webiopi.macro
def right_motor_back():
    pwm.set_pwm(R_MOTOR_BCK_CH, 0, MAX_PULSE_WIDTH)

@webiopi.macro
def right_motor_stop():
    pwm.set_pwm(R_MOTOR_FWD_CH, 0, 0)
    pwm.set_pwm(R_MOTOR_BCK_CH, 0, 0)

@webiopi.macro
def left_motor_forward():
    pwm.set_pwm(L_MOTOR_FWD_CH, 0, MAX_PULSE_WIDTH)

@webiopi.macro
def left_motor_back():
    pwm.set_pwm(L_MOTOR_BCK_CH, 0, MAX_PULSE_WIDTH)

@webiopi.macro
def left_motor_stop():
    pwm.set_pwm(L_MOTOR_FWD_CH, 0, 0)
    pwm.set_pwm(L_MOTOR_BCK_CH, 0, 0)
