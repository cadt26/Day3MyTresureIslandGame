print("Welcome to Tresure Island. ")
print("Your mission is to find the treasure.")

choice1 = input('you\'re at a crossroad, where you want to go? Type "left" or "right".').lower()

if choice1 == "left":
    #continue in the game.
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.').lower()
    if choice2 == "wait":
        #wait
        choice3 = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color you choose?').lower()
        if choice3 == 'red':
            print("It's a room full of fire")
        elif choice3 == 'yellow':
            print("You found the treasure! you win!!")
        else:
            print("You enter a room of beasts. Game over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
