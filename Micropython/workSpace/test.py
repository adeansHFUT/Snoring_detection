from machine import Pin,Timer,ADC,PWM
import time
def duty_test(motor, x, y, z):  #80,100,120
  while True:
    motor.duty(x)
    time.sleep(3)
    motor.duty(y)
    time.sleep(3)
    motor.duty(z)
    time.sleep(3)
    
def ADC_test(mic):
  while True:
    print(mic.read())
    time.sleep_ms(100)
def buzzer_test(buzz):   #duty:50 200 400 freq:100 300 600
  while True:
    buzz.update(0)
    time.sleep(2)
    buzz.update(1)
    time.sleep(2)
    buzz.update(2)
    time.sleep(2)




