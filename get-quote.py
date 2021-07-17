import random

def notMain():

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  randomNum = random.randint(0, len(quotes))

  print(quotes[randomNum].rstrip())

if __name__== "__main__":
  notMain()
