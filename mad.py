import random as r

class MadLibs:
  def __init__(self, count, iList):
    self.count = count
    self.iList = iList

  def convertToInt(self):
    self.count = int(self.count)  

  def store(self):
    self.iList = []
    for i in range(self.count):
      self.iList.append(input("Enter your story: "))

  def display(self):
    r.shuffle(self.iList)
    for x in range(self.count):
      print(self.iList[x])  
      