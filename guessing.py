import random

class guess: #created a class
    
    
    def game(): #define methods/blocks for the function
        print("You playing the game")

guess.game()
    

tries=0
loop=0
win=0
hints=0

endnumber=int(input("Enter end boundary: "))
ans=random.randint(0,endnumber)

ask=str.upper(input("Do you want hints? Y/N "))

if ask=="Y":
    hints=1
else:
    hints=0


while tries<10:
    user=int(input("Guessing "))
    
    if user == ans:
        print("Correct")
        tries=10 #exit condition
        win=1
    else:
        print("Incorrect")
        if hints==1:
            if user>ans:
                print("You're too high")
            elif user<ans:
                print("You're too low")
        tries+=1
        
if win == 0:
    print("No more guesses")
elif win==1:
    print("You won")
    
    
    
    