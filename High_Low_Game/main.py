import random
from art import logo,vs
from game_data import data
print(logo)
count=0
A=random.choice(data)
B=random.choice(data)

while True :
  a=A['follower_count']
  b=B['follower_count']
  print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
  print(vs)
  print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}")
  ans= input('who has more followers ? type A or B')
  if ans=="A":
    if a>=b:
      count+=1
      print(f"you are right. current score is {count} ")
      data.remove(B)
      C=random.choice(data)
      B=C
      continue
    else :
      print(f"Sorry , that is wrong . Final score is {count}")
      break
  else:
    if b>=a:
      count+=1
      print(f"you are right. current score is {count} ")
      C=A
      A=B
      data.remove(C)
      C=random.choice(data)
      B=C
      continue
    else :
      print(f"Sorry , that is wrong . Final score is {count}")
      break
        

