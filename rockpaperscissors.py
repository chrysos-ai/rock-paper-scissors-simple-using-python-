import random
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
user_choice = input('Please choose between "Rock", "Paper" or "Scissors" to play: ').lower()
choices = [rock, paper, scissors]
computer_choice = random.choice(choices)
if user_choice == 'rock':
    print(f"You chose Rock: \n {rock}")
    print(f'The computer chose \n {computer_choice}')
    if computer_choice == rock:
        print("It's a draw")
    elif computer_choice == scissors:
        print('You win')
    else:
        print('You loose')
elif user_choice == 'paper':
    print(f"You chose Paper: \n {paper}")
    print(f'The computer chose \n {computer_choice}')
    if computer_choice == paper:
        print("It's a draw")
    elif computer_choice == rock:
        print('You win')
    else:
        print('You loose')
else:
    print(f"You chose Scissors: \n {scissors}")
    print(f'The computer chose \n {computer_choice}')
    if computer_choice == scissors:
        print("It's a draw")
    elif computer_choice == paper:
        print('You win')
    else:
        print('You loose')