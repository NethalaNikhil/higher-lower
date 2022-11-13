import art
import game_data
import random
import replit 
count = 0
d_u_want_play = True
A = random.choice(game_data.data)
B = random.choice(game_data.data)
if (A=B):
  B = random.choice(game_data.data)
while d_u_want_play:
  replit.clear()
  print(art.logo)
  def details():
    if(count>=1):
      print("you 're right! current score : ",count)
    print(f"Compare A: {A['name']}, {A['description']}, from {A['country']}")
    print(A['follower_count'])
    print(art.vs)
    print(f"Against B: {B['name']}, {B['description']}, from {B['country']}")
    print(B['follower_count'])
  details()
  more_followers = input("Who has more followers? Type 'A' or Type 'B'").lower()
  if more_followers == 'a':
   if A['follower_count']>B['follower_count']:
     count +=1
     A = B
     B = random.choice(game_data.data)
     replit.clear()
     #print("you 're right! current score : ",count)
     details()
   else:
     replit.clear()
     print(art.logo)
     print("sorry that's wrong.Final score: ",count)
     d_u_want_play = False
  elif more_followers == 'b':
   if A['follower_count']<B['follower_count']:
     count +=1
     A = B
     B = random.choice(game_data.data)
     replit.clear()
     #print("you 're right! current score : ",count)
     details()
   else:
     replit.clear()
     print(art.logo)
     print("sorry that's wrong.Final score: ",count)
     d_u_want_play = False
    
   
  
