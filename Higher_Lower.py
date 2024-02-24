from game_data import data
from Higher_Lower_art import logo, vs
from random import randint
from replit import clear
import pandas as pd

def choose_a_random_person(data):
  '''Choose a random person from the data list'''
  return data[randint(0, len(data) - 1)]

def print_person(person):
  '''Print the person's name, description and country'''
  print(f"{person['name']}, a {person['description']}, from {person['country']}")

def compare_followers(person_a, person_b):
  '''Compare who has more followers'''
  if person_a['follower_count'] > person_b['follower_count']:
    return person_a
  else:
    return person_b

def game(score, game_over,greater):
  print(logo)
  person_a = greater
  print_person(person_a)
  print(vs)
  person_b = choose_a_random_person(data)
  while person_a == person_b:
    person_b = choose_a_random_person(data)
  
  print_person(person_b)
  greater = compare_followers(person_a, person_b)
  answer = input("Who has more followers? Type 'A' or 'B': ").upper()
  if answer == 'A':
    answer = person_a
    if answer == greater:
      score += 1
      clear()
      print(f"You're right! Current score: {score}.")
      game(score, game_over, greater)
    else:
      clear()
      print(f"Sorry, that's wrong. Final score: {score}")
      game_over = True
  elif answer == 'B':
    answer = person_b
    if answer == greater:
      score += 1
      clear()
      print(f"You're right! Current score: {score}.")
      game(score, game_over, greater)
    else:
      clear()
      print(logo)
      print(f"Sorry, that's wrong. Final score: {score}")
      game_over = True

  else:
    print("Invalid input")
    game(score, game_over, greater)



score = 0
game_over = False
greater = choose_a_random_person(data)
game(score, game_over, greater)

      
    

 