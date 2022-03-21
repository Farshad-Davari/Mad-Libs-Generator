from mad import MadLibs

if __name__ == "__main__":
  count = input("How many story you want to tell ?")
  madObj = MadLibs(count, [])
  madObj.convertToInt()
  madObj.store()
  madObj.display()