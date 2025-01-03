name = input("Type your name: ")
print(f"Welcome {name} to this adventure")

answer = input("You are on a dirt road and you can go left or right. Which way would you like to go? left or right? ").lower()

if answer == 'left':
    answer = input("You come to a river and you can go around it ror swim acorss. What do you do? swim or walk around? ")
    
    if answer == 'swim':
        print("You swam across and you were eaten by an alligator")
    elif answer == 'walk':
        print("You walked for many miles and ran out of water and lost the game")
        
    else:
        print("Not a valid option")
elif answer == 'right':
    answer = input("You come to a bridge. It looks woobly. Do you want to cross it or head back (back or cross )")
    
    if answer == 'back':
        print("you go back and lose.")
    elif answer == 'cross':
        answer = input("You cross the bridge and meet a stranger. Do you talk to them Yes or no")
        
        if answer == 'yes':
            print("You talk to the stranger. They give you gold and you win")
        elif answer == 'no':
            print("You ignore the stranger and you lose.")
        else:
            print("Not a valid option. You lose")
else:
    print("Not valid option")

print("Thank you for trying!")