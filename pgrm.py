print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("\t\tSTONE PAPER SCISSOR...")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
options = ['stone', 'paper', 'scissor']
import random
computer = random.choice(options)
optionsuser = ['stone', 'paper', 'scissor', 'quite']
count1 = 0
count2 = 0
user = 0
while user != "quite":
    print("\n(Choice are stone,paper,scissor,quite(for quite the game))")
    user = input("\nEnter your choice : ")
    print("\nUser : " + user)
    print("Computer:" + computer)
    if user == computer:
        print("Tie")
    elif user == "stone" and computer == "sscissor":
        print("User wins")
        count1=count1+1
    elif user == "stone" and computer == "paper":
        print("Computer wins")
        count2=count2+1
    
    elif user == "paper" and computer == "stone":
        print("User wins")
        count1=count1+1
    elif user == "paper" and computer == "scissor":
        print("Computer wins")
        count2=count2+1
    elif user == "scissor" and computer == "paper":
        print("User wins")
        count1=count1+1
    elif user == "scissor" and computer == "stone":
        print("Computer wins")
        count2=count2+1
    elif user == "quite":
        if count1 > count2:
            print("User wins.")
            print("Score : " + str(count1))
            print("Score of computer : " + str(count2))
        else:
            print("Computer wins.")
            print("Score : " + str(count2))
            print("Score of user : " + str(count1))
    else:
        print("Invalid choice")
    print("••••••••••••••••••••••••••••••••••••••••••••••")
