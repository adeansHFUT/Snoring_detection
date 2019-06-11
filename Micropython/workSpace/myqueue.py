# -*- coding: utf-8 -*-
class MYqueue:
  def __init__(self, dic):
    self.items = []
    if dic['size'] < 1:
      self.size = 1
    else:
      self.size = dic['size']
      self.low_limit = dic['low_limit']
      self.mid_limit = dic['mid_limit']
      self.high_limit = dic['high_limit'] 
      
  def enqueue(self, item):   #入队列
    if self.size == len(self.items):
      self.items.pop(0)
      
    self.items.append(item)
      
  def detect(self,snore):  #鼾声检测算法，先最简单-算术平均
    sum = 0
    snore_rank = 0
    for i in self.items:
      sum += i
    average = sum/len(self.items) 
    if average < self.low_limit:
      snore_rank = 0 #没有鼾声
    elif average < self.mid_limit:
      snore_rank = 1 #一级鼾声
    elif average < self.high_limit:
      snore_rank = 2 #二级鼾声
    else:
      snore_rank = 3 #三级（最高）鼾声
    snore.update({'rank':snore_rank, 'average':average})
        
  def empty(self):
    return self.size() == 0

  def size(self):
    return len(self.items)



