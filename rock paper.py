import random
print('What do you choose 0 for rock,1 for paper or 2 for scissors.')
user=int(input())
rock=0
paper=1
scissors=2
rockk='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
Rock
'''

paperr = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
Paper
'''

scissorss = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
Scissors
'''
print('You chose:')
if user==0:
    print(rockk)
elif user==1:
    print(paperr)
else: 
    print(scissorss)
computer=random.randint(0,2)
print('Computer chose:')
if computer==0:
    print(rockk)
elif computer==1:
    print(paperr)
else: 
    print(scissorss)

if user >= 3 or user< 0: 
  print("You typed an invalid number, you lose!") 
elif user == 0 and computer == 2:
  print("You win!")
elif computer == 0 and user == 2:
  print("You lose")
elif computer > user:
  print("You lose")
elif user > computer:
  print("You win!")
elif computer == user:
  print("It's a draw")