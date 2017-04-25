#import sys

user1 = input("What's your name?")
user2 = input("And your name?")
user1_answer = input("%s, do yo want to choose rock, paper or scissors?" % user1)
user2_answer = input("%s, do you want to choose rock, paper or scissors?" % user2)

l = ['rock', 'paper' , 'scissors']

for i in user1_answer:
    if user1_answer == l:
        print (user1_answer)
    else:
        print("invalid entry:")

    
for j in user2_answer :
    if user2_answer == l:
        print (user2_answer)
    else:
        print("invalid entry:")
def compare(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return("Scissors win!")
        else:
            return("Rock wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return("Paper wins!")
        else:
            return("Scissors win!")
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")
        sys.exit()

print(compare(user1_answer, user2_answer))