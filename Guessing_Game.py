import random

number = random.randint(1, 9)
chances = 0

while  chances <5 :
 guess  = int(input("Guess a number (Between 1 & 9)"))
 chances = chances + 1

 if(guess == number) :
  print("Congratulations ! You won")

  break

if not chances <5 :
 print("You Lose ! The correct number is", number)