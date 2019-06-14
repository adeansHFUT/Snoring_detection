from machine import PWM
class Mybuzz: # 4 gears of microphone
  buzzs = [ {'duty':0, 'freq':0},
            {'duty':20, 'freq':400},
            {'duty':50, 'freq':600},
            {'duty':100, 'freq':900}]
  def __init__(self, pinxx, freq, duty):
    self.pwm = PWM(pinxx, freq, duty)
  def update(self,n):
    self.pwm.duty(self.buzzs[n]['duty'])
    self.pwm.freq(self.buzzs[n]['freq'])
    
class Mymotor: # 4 gears of  motors
  motors = [{'duty':0, 'freq':0},
            {'duty':60, 'freq':800},
            {'duty':80, 'freq':800},
            {'duty':100, 'freq':800}]
  def __init__(self, pinxx, freq, duty):
    self.pwm = PWM(pinxx, freq, duty)
  def update(self,n):
    self.pwm.duty(self.motors[n]['duty'])
    self.pwm.freq(self.motors[n]['freq'])




