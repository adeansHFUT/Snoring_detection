
# -*- coding: utf-8 -*-
from test import buzzer_test
from myconfig import Mybuzz,Mymotor
from myqueue import MYqueue
from machine import Pin,Timer,ADC,PWM
import time
def update_queue(t):
  snoreq.enqueue(mic.read()) 
def my_init(): #初始化:电机，麦克风，定时时钟，队列
  motor = Mymotor(pinxx=Pin(4), freq=800, duty=0) #电机初始化
  mic = ADC(0)  #麦克风初始化
  buzz = Mybuzz(pinxx=Pin(5), freq=100, duty=0) #蜂鸣器初始化
  dic = {'size':10, 'low_limit':100, 'mid_limit':250, 'high_limit':500}
  snoreq = MYqueue(dic) 
  tim_update = Timer(-1) 
  tim_update.init(period=100, mode=Timer.PERIODIC, callback=update_queue)
  return motor,buzz,snoreq,tim_update,mic
#motor,mic,buzz,snoreq = my_init()
#buzzer_test(buzz)

def my_deinit(motor,buzz,tim_update): #turn off the motor microphone timer
  motor.update(0)
  buzz.update(0)
  tim_update.deinit()
  
if __name__ == '__main__':  
  motor,buzz,snoreq,tim_update,mic = my_init()
  snore = {}
  time.sleep(2) #延时，让其采集满一个队列
  while True:
    snoreq.detect(snore)
    rank = snore['rank']
    if rank == 0:  # rank 0 snoring
      motor.update(0)
    elif rank == 1: # rank 1 snoring
      motor.update(1)
      print(snore)
      time.sleep(1)
      snoreq.set_sonreitems_zero()   #clear off the snore items in order to not detect the snore when treatment 
    elif rank == 2:
      motor.update(2)
      print(snore)
      time.sleep(1)
      snoreq.set_sonreitems_zero()
    elif rank == 3:
      motor.update(3)
      print(snore)
      time.sleep(1)
      snoreq.set_sonreitems_zero()
    else:
      print('error!')















