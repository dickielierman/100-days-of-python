import time


def pause(t=1):
    time.sleep(t)


def yes_or_no(question):
    answer = input(question + "(y/n): ").lower().strip()
    print("")
    while not (answer == "y" or answer == "yes" or answer == "n" or answer == "no"):
        print("Input yes or no")
        answer = input(question + "(y/n):").lower().strip()
        print("")
    if answer[0] == "y":
        return True
    else:
        return False


def printAsciiPanel(name):
    print(open(f'ascii/{name}.txt', 'r').read())


printAsciiPanel("blank")
printAsciiPanel('treasure-island-welcome')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print()
if not yes_or_no("Do you think you have what it takes?"):
    printAsciiPanel('ship-sailing-away')
    print()
    print("Fair enough then, matey! Fair thee well")
else:
    printAsciiPanel("blank")
    print("Good to hear lad!")
    print("Here's the thing bout that tho...")
    pause(2)
    print("\n\n")
    printAsciiPanel("treasure-map")
    print("\n\nGots no idea how to read this map.")
    print("Should we go to that volcano, or look by the beach?")
    pause(1)
    print()
    direction = input("Type 'volcano' or 'beach'? ").lower().strip()
    while not (direction == "v" or direction == "volcano" or direction == "b" or direction == "beach"):
        print()
        direction = input("Type 'volcano' or 'beach'? ").lower().strip()

    if direction.lower()[0] == 'v':
        printAsciiPanel("blank")
        printAsciiPanel("volcano")
        print()
        pause(2)
        print("Well at din't work out s'well. Ya Died.")
        print("I guess it's back to the drawing board.")
        pause(4)
        printAsciiPanel("blank")
        printAsciiPanel("the-end")
    else:
        printAsciiPanel("blank")
        printAsciiPanel("beach")
        print()
        pause(2)
        print("Arh, we made it safe n' sound!")
        print("The map said it was over em hills thar I think.")
        pause(1)
        print("Should we start climbing, or take the easy round the water?")
        print()
        pause(2)
        direction = input("Type 'climb' or 'beach'? ").lower().strip()
        while not (direction == "c" or direction == "climb" or direction == "b" or direction == "beach"):
            print()
            direction = input("Type 'climb' or 'beach'? ").lower().strip()
        if direction.lower()[0] == 'b':
            printAsciiPanel("blank")
            printAsciiPanel("cliff")
            print()
            print("Ya fell off a cliff into the ocean.")
            pause(2)
            printAsciiPanel("blank")
            pause(1)
            printAsciiPanel("death")
            pause(4)
            printAsciiPanel("blank")
            printAsciiPanel("the-end")
        else:
            printAsciiPanel("blank")
            printAsciiPanel("treasure")
            print()
            print()
            pause(2)
            print("Thar it be matey!")
            print("Should we...")
            print("A. I get it all cuz it bein' my map and all...")
            pause(1)
            print("B. Split it even...")
            pause(1)
            print("C. you gonna try to kill me and take it all?")
            print()
            pause(1)
            door = input("'a', 'b', or 'c'? ").lower().strip()
            while not (door == "a" or door == "A" or door == "b" or door == "B" or door == "c" or door == "C"):
                print()
                door = input("'a', 'b', or 'c'? ").lower().strip()
            if door == 'a' or door == "c":
                printAsciiPanel("blank")
                if door == 'a':
                    print("Can't trust a pirate that ain't willin' to take his fair share matey!")
                if door == 'b':
                    print("Can't trust a pirate fer nothin' I tell ya!")
                    print("Well, you met yer match, and now you'll meet your maker!")
                    pause(2)
                pause(1)
                printAsciiPanel("blank")
                printAsciiPanel("fight1")
                pause(.5)
                printAsciiPanel("blank")
                printAsciiPanel("fight2")
                pause(.5)
                printAsciiPanel("blank")
                printAsciiPanel("fight3")
                pause(.5)
                printAsciiPanel("blank")
                printAsciiPanel("fight2")
                pause(.5)
                printAsciiPanel("blank")
                printAsciiPanel("fight1")
                pause(.5)
                printAsciiPanel("blank")
                printAsciiPanel("fight2")
                pause(.5)
                printAsciiPanel("blank")
                printAsciiPanel("fight3")
                pause(.5)
                printAsciiPanel("blank")
                pause(1)
                printAsciiPanel("death")
                pause(4)
                printAsciiPanel("blank")
                printAsciiPanel("the-end")
            elif door == 'b':
                printAsciiPanel("blank")
                printAsciiPanel('treasure-island-welcome')
                print("\nWell How bout that! We did it! We found the treasure together!")
