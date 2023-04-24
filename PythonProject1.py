import sys, time

#Variables used for different choices.
option1 = 1
option2 = 2

#Global variable for item-carrying mechanic
global haveBun
haveBun = 0

#Function that will print characters 1 by 1.
def print1by1(text, delay=0.1):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print1by1

#Function that will printcharacters 1 by 1 at a slower rate.
def slow1by1(text, delay=0.2):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    slow1by1


#Functions for both endings.
def goodEnding():
    print1by1("You give the Spice Bun to you roomate and he cooperatively turns his keyboard's volume down.\n")
    print1by1("You have successfully found the source of loud and terrible music, and stopped it!\n")
    print1by1("The End!\n")
def badEnding():
   print1by1("'Now, I'll never turn it down' he says as he sets his keybord to the maximum volume\n")
   print1by1("You've have successfully found the source of loud and terrible music, but failed to stop it.\n")
   print1by1("The End!\n")

#Functions to progress through game.
def roommateRoom():
    print1by1("You enter your roommate's room to find\n...\n")
    slow1by1("...\n")
    slow1by1("...\n")
    slow1by1("...\n")
    slow1by1("IT WAS YOUR ROOMMATE ALL ALONG: MATTHEW!\n")
    print1by1("He was the one behind the terrible tune you've been listening to since you entered your apartment.\n")
    print1by1("You ask him politely 'Hey, could you please turn it down?'\n")
    print1by1("'Fine, but only if you get me that Spice Bun that downstairs in the kitchen.' he says.\n")
    print("-----------------------------------------------------------------------------------------------------")
    if haveBun == -1:
        print1by1("'Uhhhh, I ate it' you tell him\n")
        print1by1("'WHAT!?' he shouts. 'It was mine!'\n")
        badEnding()
    elif haveBun == 1:
        goodEnding()
    elif haveBun == 0:
        print1by1("You head downstairs into the kitchen to find a scrumptious-looking loaf of Spice Bun on the counter.\nYou grab it and head back upstairs to your roommate's Room\n")
        goodEnding()

def kitchen():
    print1by1("You enter the kitchen and the sound of that awful melody gets quieter, as if it's further away.\nAlthough it isn't as loud, the music still bothers you. \n")
    print1by1("Now standing in the kitchen, you have the option of searching the kitchen or moving on to upstairs.\n")
    decision_1 = int(input("What will you do[Enter 1 to Search the kitchen or 2 to Head upstairs]\n"))
    print("-----------------------------------------------------------------------------------------------------")
    if decision_1 == option1:
        print1by1("You search the entire kitchen, only to find that there is nobody there,\nhowever, there is an unopened loaf of Spice Bun that you pick up.\n")
        print1by1("+1 Spice Bun!\n")
        print1by1("You can eat the Spice Bun or Carry it for later\n")
        bunDecision = int(input("What will you do [Enter 1 to eat the Spice Bun or 2 to Carry it for later]\n"))
        if bunDecision == option1:
            print("-----------------------------------------------------------------------------------------------------")
            print1by1("You indulge yourself and eat the Spice Bun whole. It was delicious!\n") 
            haveBun = -1
        if bunDecision == option2:
            print("-----------------------------------------------------------------------------------------------------")
            print1by1("You decided to save the bun for later.\n")
            haveBun = 1
        print1by1("After some time in the kitchen, you decided to head upstairs as it is your only other option\n")
        print("-----------------------------------------------------------------------------------------------------")
        goneUpstairs()
    if decision_1 == option2:
        print1by1("After some time in the kitchen, you decided to head upstairs as it is your only other option\n")
        print("-----------------------------------------------------------------------------------------------------")
        goneUpstairs()

def goneUpstairs():
    print1by1("You go upstairs and hear the foul piano-playing get louder as you get closer.\n")
    print1by1("You see your room and roommate's room in the hallway.\nThe sound is obviously coming from your roommate's room.\n")
    decision2 = int(input("What will you do [Enter 1 to Enter Your Roommate's Room or 2 to Enter Your Room]\n"))
    print("-----------------------------------------------------------------------------------------------------")
    if decision2 == option1:
        roommateRoom()

    if decision2 == option2:
        print1by1("You enter your room and to no one's surprise, nobody is in it.\n")
        print1by1("You figure that there is only one place this piano man could be and head to your roommate's room\n")
        print("-----------------------------------------------------------------------------------------------------")
        roommateRoom()

#The game
def game():
    if decision1 == option1:
        goneUpstairs()
    if decision1 == option2:
        kitchen()

print1by1("Matthew's Text Based Adventure Game\n")
print1by1("Welcome! There is a man playing piano in your apartment. There is no rhythm or flow to his playing.\nThe awful music is causing you to visually cringe, as you are a world renowned pianist yourself.\n")
print1by1("Your mission is to find the villainous piano man.\n")
print("-----------------------------------------------------------------------------------------------------")
print1by1("You walk into your apartment and hear a wretched sound. You have the option of going upstairs or walking into the kitchen.\n")
decision1 =  int(input("What will you do [Enter 1 for Upstairs or 2 for Kitchen]\n"))
print("-----------------------------------------------------------------------------------------------------")
game()

