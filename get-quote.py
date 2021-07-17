import random

def notMain():

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  randomNum = random.randint(0, 13)

  print(quotes[randomNum])

if __name__== "__main__":
  notMain()
