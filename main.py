#go to
#https://replit.com/@appbrewery/higher-lower-final?v=1
#and play game draw a flow chart for the game

import random
import art
from game_data import data


def game(data, person_1, score):
  """Game function plays the game"""
  right = True
  person_2 = random.choice(data)
  while person_2 == person_1:
    person_2 = random.choice(data)
  
  print(art.logo)
  print(
    f"Compare A: {person_1['name']}, a {person_1['description']}, from {person_1['country']}."
  )
  print(art.vs)
  print(
    f"Compare B: {person_2['name']}, a {person_2['description']}, from {person_2['country']}."
  )
  selected = input("Who has more followers? Type 'A' or 'B':").upper()
  if selected == "A":
    if person_1['follower_count'] < person_2['follower_count']:
      right = False
  else:
    if person_1['follower_count'] > person_2['follower_count']:
      right = False
      
  if right:
    score += 1
    print("You're right! Current score: ", score)
    game(data, person_2, score)
  else:
    print(f"Sorry, that's wrong. Final score: {score}")


play_game = True
while play_game:
  score = 0
  game(data, random.choice(data), score)
  play_game = input("Would you like to play again? Type 'yes' or 'no':").lower()
  if play_game == "no":
    play_game = False
    print("Thanks for playing!")
