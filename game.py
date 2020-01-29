import random
def randomfn():
  no = random.randint(0,20)
  return no
no=randomfn()
guess = int(input("enter your guess:"))
print(no)
if(guess==no):
  print("you won")
else:
  print("you lost")