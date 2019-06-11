
# -*- coding: utf-8 -*-
from test import buzzer_test
from myconfig import Mybuzz,Mymotor
from myqueue import MYqueue
from machine import Pin,Timer,ADC,PWM
import time
def update_queue(t):
  snoreq.enqueue(mic.read()) 
def my_init(): #初始化:电机，麦克风，定时时钟，队列
  motor = Mymotor(Pin(4), freq=800, duty=0)
  mic = ADC(0)
  buzz = Mybuzz(Pin(5), freq=100, duty=30)
  dic = {'size':10, 'low_limit':100, 'mid_limit':250, 'high_limit':500}
  snoreq = MYqueue(dic) 
  tim_update = Timer(-1) 
  tim_update.init(period=100, mode=Timer.PERIODIC, callback=update_queue)
  return motor,mic,buzz,snoreq
motor,mic,buzz,snoreq = my_init()
buzzer_test(buzz)
'''
if __name__ == '__main__':    
  motor,mic,snoreq = my_init()
  snore = {}
  time.sleep(2) #延时，让其采集满一个队列
  while True:
    snoreq.detect(snore)
    print(snore)
    rank = snore['rank']
    if rank == 0:
      motor.duty(0)
    elif rank == 1:
      motor.duty(60)
      time.sleep(1)
    elif rank == 2:
      motor.duty(80)
      time.sleep(1)
    elif rank == 3:
      motor.duty(100)
      time.sleep(1)
    else:
      print('error!')
'''













