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


mylist = [rock,paper,scissors]
myliststr = ['rock','paper','scissors']

import random

yourchoice = input('What do you choose? ')
yourindex = myliststr.index(yourchoice)

compchoice = random.randint(0,2)
print (f'Computer chooses {myliststr[compchoice]} {mylist[compchoice]}')

print (f'You choose {myliststr[yourindex]} {mylist[yourindex]}')



if yourchoice == 'rock' and myliststr[compchoice] == 'rock':
    print('Its a tie')
elif yourchoice == 'rock' and myliststr[compchoice] == 'paper':
    print('You loose')
elif yourchoice == 'paper' and myliststr[compchoice] == 'rock':
    print('You win')
elif yourchoice == 'rock' and myliststr[compchoice] == 'scissors':
    print('You win')
elif yourchoice == 'scissors' and myliststr[compchoice] == 'rock':
    print('You loose')
    
    
elif yourchoice == 'paper' and myliststr[compchoice] == 'paper':
    print('Its a tie')
    
elif yourchoice == 'paper' and myliststr[compchoice] == 'scissors':
    print('You loose')
elif yourchoice == 'scissors' and myliststr[compchoice] == 'paper':
    print('You win')


elif yourchoice == 'scissors' and myliststr[compchoice] == 'scissors':
    print('Its a tie')
    



