rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

mylist = [rock,paper,scissors]

compchoice = mylist[random.randint (0,2)]

yourchoice = input('Choose your option: ')

print (f'computers choice is  {compchoice}')

if yourchoice =='rock' and compchoice =='rock':
    print (rock)
    print ('Its a tie')
elif yourchoice =='rock' and compchoice =='paper':
    print (rock)
    print ('You loose')
elif yourchoice =='rock' and compchoice =='scissors':
    print (rock)
    print ('You win')


