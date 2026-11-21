import sys

def main():
    code = "417"
    puzzle_break = False
    keys = 0
    reveal_option_e = False
    
    # Introduction
    print()
    print("You find a paper that slid under your front door. It reads, '97 Abigail Street.'")
    print("You search up this address and find that it is not far. You decide to go.")

    # Entrance/Long Hallway
    print()
    print("You arrive at a large mansion, with a large door. You get out of your car and")
    print("approach the door. The door automatically opens, and you are presented with")
    print("a long hallway. Decorated with bookshelves, tables, paintings, and statues, this")
    print("house is very interesting. A door lies at the end of the hallway.")

    # Puzzle (text, questions, answers)
    while True:
        print()
        print("You walk down the hallway, and find a bookshelf filled with books. What do you do?")
        print("    a. Inspect the bookshelf")
        print("    b. Try to open the door")
        print("    c. Look around the hallway")
        print("    d. Leave the mansion")
        input_puzzle1 = input("Answer: ").lower()

        # Puzzle Problem 1 Option A
        if input_puzzle1 == "a":
            print()
            print("There are books with colors of red, blue, yellow, and green, each organized in their own set. Which color do you look at?")
            print("    a. Red")
            print("    b. Blue")
            print("    c. Yellow")
            print("    d. Green")
            input_puzzle1A = input("Answer: ").lower()

            if input_puzzle1A == "c":
                print("You find a number 7. Interesting.")
            elif input_puzzle1A in ['a', 'b', 'd']:
                print("You find nothing.")
            else:
                print()
                print("Invalid Input")

        elif input_puzzle1 == "b":
            print()
            print("The door is locked. There is a padlock with 3 numbers that requires a code. Do you know the code?")
            print("    a. Yes, I do")
            print("    b. No, I don't")
            input_puzzle1B = input("Answer: ").lower()

            while True:
                if input_puzzle1B == "a":
                    print()
                    print("What is the 3 number code?")
                    input_puzzle_code = input("Code: ")

                    if input_puzzle_code == code:
                        puzzle_break = True
                        break
                    else:
                        print()
                        print("The padlock does not budge.")
                        break
                elif input_puzzle1B == "b":
                    break
                else:
                    print()
                    print("Invalid Input")
                    break
            if puzzle_break == True:
                break
        
        elif input_puzzle1 == "c":
            while True:
                print()
                print("You look down the hallway and find many decorative features. Where do you go?")
                print("    a. Go to the paintings")
                print("    b. Go to the sculptures")
                print("    c. Go to the bookshelves")
                print("    d. Go to the table next to the door")
                input_puzzle1C = input("Answer: ").lower()
            
                if input_puzzle1C == "a":
                    print()
                    print("There are many paintings on the left wall that hold famous paintings. What do you do?")
                    print("    a. Look at some paintings")
                    print("    b. Walk away")
                    print("    c. Fix the crooked 'Mona Lisa'")
                    input_puzzle1CA = input("Answer: ").lower()

                    if input_puzzle1CA == "a":
                        print()
                        print('You recognize some of the paintings here. “The Starry Night,” “The Last Supper,” and “The Scream.”')
                    if input_puzzle1CA == "b":
                        continue
                    if input_puzzle1CA == "c":
                        print()
                        print('You re-level the painting titled, “Mona Lisa.” It reveals the number 4.')
                
                elif input_puzzle1C == "b":
                    print()
                    print("You see life sized sculptures that each seem to depict a famous person from a different time period. Which sculpture do you look at?")
                    print("    a. Bruce Lee")
                    print("    b. Augustus Ceasar")
                    print("    c. Shakira")
                    print("    d. Michael Jackson")
                    input_puzzle1CB = input("Answer: ").lower()

                    if input_puzzle1CB == "a":
                        print()
                        print("Bruce Lee is seen with nunchucks while holding his guard up.")
                    elif input_puzzle1CB == "b":
                        print()
                        print("Augustus Caesar has military armor while standing in a confident and idealized pose. He is engraved with a small number one.")
                    elif input_puzzle1CB == "c":
                        print()
                        print("Shakira is in the middle of doing her iconic dance from her music video and song, 'Hips Don't Lie'")
                    elif input_puzzle1CB == "d":
                        print()
                        print("Michael Jackson is holding his pet chimpanzee, Bubbles, while sitting on a bed of roses.")
                    else:
                        print()
                        print("Invalid Input")

                elif input_puzzle1C == "c":
                    break

                elif input_puzzle1C == "d":
                    print()
                    print("You find a table next to the door. You are not quite sure if there is anything there. What do you do?")
                    print("    a. Open the drawer")
                    print("    b. Turn on the lamp")
                    print("    c. Look under the table")
                    print("    d. Look behind the table")
                    input_puzzle1CD = input("Answer: ").lower()

                    if input_puzzle1CD == "a":
                        print()
                        print("You open the drawer. Inside, the letters “PSB” are found.")
                    elif input_puzzle1CD == "b":
                        print()
                        print('The lamp shines onto the table. The table appears to be a simple wooden table. There lies a picture of the “Mona Lisa.”')
                    elif input_puzzle1CD == "c":
                        print()
                        print("You look under the table. The table is very yellow from what you can see.")
                    elif input_puzzle1CD == "d":
                        print()
                        print('You drag the table so you can see its back. The back of the table has the name, “Augustus Ceasar.”')
                    else:
                        print()
                        print("Invalid Input")
                    
                else:
                    print()
                    print("Invalid Input")
        
        elif input_puzzle1 == "d":
            leave_mansion()
            break

        else:
            print()
            print("Invalid Input")



    # Crossroad
    while True:
        print()
        print("You are at a crossroad. There is a door to your left, right, and straight ahead. Which door do you go to?")
        print("    a. Left door")
        print("    b. Right door")
        print("    c. The door in front")
        print("    d. Leave the mansion")
        input_cross = input("Answer: ").lower()

        if input_cross == 'a':
            print()
            print("You walk in and see a soldier. He starts charging at you with a sword! What do you do?")
            print("    a. Dodge the attack")
            print("    b. Punch back")
            print("    c. Try taking the sword")
            print("    d. Run away")
            input_left1 = input("Answer: ").lower()

            if input_left1 == 'a':
                print()
                print("Nice! You dodged the sword. Quick, the sword is next to your neck, what do you do?")
                print("    a. Fight back")
                print("    b. Try taking the sword")
                print("    c. Run away")
                input_left1A = input("Answer: ").lower()

                if input_left1A == 'a':
                    print()
                    print("You punch him, and he falls. Now what?")    
                    print("    a. Take his sword")
                    print("    b. Go look at what he was guarding")
                    print("    c. Run away")
                    input_left1AA = input("Answer: ").lower()

                    if input_left1AA == 'a':
                        print()
                        print("You take his sword, and he surrenders. He points to the back of")
                        print("the room, where there is a key. You thank him and leave.")
                        keys += 1

                    if input_left1AA == 'b':
                        print()
                        print("You find a key and take it. You turn around, only to find the soldier up again!")
                        print("He attacks and you cannot dodge his attack. Would you like to try again? (yes or no)")
                        input_left1AAB = input("Answer: ").lower()

                        if input_left1AAB == 'yes':
                            for i in range(3):
                                print()
                            main()
                        elif input_left1AAB == 'no':
                            print()
                            print("You were too scared to try again…")
                            sys.exit()
                        else:
                            print()
                            print("Invalid Input")
                            sys.exit()

                    if input_left1AA == 'c':
                        print()
                        print("You run away from the soldier, back into the crossroads.")
                        continue
                
                if input_left1A == 'b':
                    print()
                    print("You try to grab the sword, but the sword is so sharp that it slices your hand!")
                    print("The soldier slices again and you fall unconscious. Would you like to try again from the beginning? (yes or no)")
                    input_left1AB = input("Answer: ").lower()

                    if input_left1AB == 'yes':
                        for i in range(3):
                            print()
                        main()
                    elif input_left1AB == 'no':
                        print()
                        print("You were too scared to try again…")
                        sys.exit()
                    else:
                        print()
                        print("Invalid Input")
                        sys.exit()

                if input_left1A == "c":
                    print()
                    print("You run away from the soldier, back into the crossroads")
                    continue

            if input_left1 == "b":
                print()
                print("You try to punch back, but the sword still penetrates you, going straight through your heart!")
                print("You died! Would you like to try again from the beginning? (yes or no)")
                input_left1B = input("Answer: ").lower()

                if input_left1B == 'yes':
                    for i in range(3):
                        print()
                    main()
                elif input_left1B == 'no':
                    print()
                    print("You were too scared to try again…")
                    break
                else:
                    print()
                    print("Invalid Input")
                    sys.exit()
            
            if input_left1 == "c":
                print()
                print("You try to grab the sword, but the sword is so sharp that it slices your hand!")
                print("The soldier slices again and you fall unconscious. Would you like to try again from the beginning? (yes or no)")
                input_left1C = input("Answer: ").lower()

                if input_left1C == 'yes':
                    for i in range(3):
                        print()
                    main()
                elif input_left1C == 'no':
                    print()
                    print("You were too scared to try again…")
                    break
                else:
                    print()
                    print("Invalid Input")
                    sys.exit()
                
            
            if input_left1 == 'd':
                print()
                print("You run away from the soldier, back into the crossroads.")
                continue

        
        # Right Door
        elif input_cross == 'b':
            print()
            print('You walk in, and find a person with a microphone. You hear cheering, and realize')
            print('that you are now in a game show! The host says, "Congratulations for making it this far!')
            print('Now you have to answer three trivia questions to progress.')
            print('Your first question is math related. What is the square root of 81?”')
            print("    a. 7")
            print("    b. 8")
            print("    c. 9")
            print("    d. 10")
            input_right1 = input("Answer: ").lower()

            if input_right1 == 'c':
                print()
                print('The host says, “Correct! Your next question is, who was the first person to walk on the Moon?”')
                print("    a. Buzz Aldrin")
                print("    b. Yuri Gagarin")
                print("    c. Michael Collins")
                print("    d. Neil Armstrong")
                input_right2 = input("Answer: ").lower()

                if input_right2 == "d":
                    print()
                    print('The host says, “Correct! Your next question is, what is the name of the fictional country where Black Panther takes place?”')
                    print("    a. Wakanda")
                    print("    b. Wakandia")
                    print("    c. Tazmania")
                    print("    d. Wakanya")
                    input_right3 = input("Answer: ").lower()

                    if input_right3 == 'a':
                        print()
                        print('The host says, “Congratulations! You passed the trivia quiz! Your prize is this key. Okay, goodbye now.”')
                        keys += 1
                        continue
                    elif input_right3 in ['b', 'c', 'd']:
                        print('The host says, “Incorrect! Sorry, you must leave now. If you come back, I may give you another chance!"')
                    else:
                        print()
                        print("Invalid Input")
                elif input_right2 in ['b', 'c', 'a']:
                    print('The host says, “Incorrect! Sorry, you must leave now. If you come back, I may give you another chance!"')
                else:
                    print()
                    print("Invalid Input")
            elif input_right1 in ['b', 'a', 'd']:
                print('The host says, “Incorrect! Sorry, you must leave now. If you come back, I may give you another chance!"')
            else:
                print()
                print("Invalid Input")
        
        # The Door in the front
        elif input_cross == 'c':
            print()
            if keys == 0:
                print('The door is locked. It requires two keys.')
            elif keys == 1:
                print('The door is locked. It now requires only one key.')
            else:
                print("The door is unlocked. Do you choose to go in?")
                print("    a. Yes, I do")
                print("    b. No, I don't")
                print("    c. I want to leave")
                input_front = input("Answer: ").lower()

                if input_front == "a":
                    break
                elif input_front == "b":
                    continue
                elif input_front == "c":
                    leave_mansion()
                    break
                else:
                    print()
                    print("Invalid Input")
        
        # Leave the mansion
        elif input_cross == 'd':
            leave_mansion()
            break

        else:
            print()
            print("Invalid Input")
    
    # Fake Treasure Room
    print()
    print("You walk into the room. It blinds you. You adjust to it,")
    print("and find piles of gold, jewelry, and precious gems! You did it!",end="")
    while True:
        print()
        print("What do you want to do?")
        print("    a. Enjoy your riches")
        print("    b. Pick up some gold")
        print("    c. Look around the room")
        print("    d. Leave the mansion")
        if reveal_option_e:
            print("    e. Inspect what’s under the blankets")
        input_ftreasure1 = input("Answer: ").lower()

        if input_ftreasure1 == 'a':
            print()
            print("You dive into the pile of gems, but you don’t feel yourself")
            print("hitting the ground. Everything was a fake! You fall into a pit dug")
            print("fifty feet down, finding a door at the end.",end="")

            while True:
                print()
                print("What do you do?")
                print("    a. Try to climb up the pit")
                print("    b. Open the door")
                input_ftreasureA = input("Answer: ").lower()

                if input_ftreasureA == 'a':
                    print()
                    print("You try to climb up the pit, but your legs")
                    print("are injured from the fall. You fall down.")

                elif input_ftreasureA == 'b':
                    print()
                    print("You open the door to the stairs. You slowly crawl up and")
                    print("find yourself back at the entrance. You walk to the door")
                    print("and find that it is locked. You survived, but you gained")
                    print("nothing.")
                    sys.exit()
                
                else:
                    print()
                    print("Invalid Input")
            
        elif input_ftreasure1 == 'b':
            print()
            print("You pick up a massive bar of gold and throw it around. It is very light.")
        
        elif input_ftreasure1 == 'c':
            print()
            print("You look around the room. It is filled to the brim with potential money.")
            print("Some things are covered in blankets.")
            reveal_option_e = True
        
        elif input_ftreasure1 == 'd':
            leave_mansion()
            break
        
        elif input_ftreasure1 == 'e' and reveal_option_e:
            print()
            print('You uncover a blanket on a wall. It reveals another room with more gold!"')
            print('"You step in, and the previous room’s items are all gone. You realize that the first room was a fake!')
            print('"On the wall, it says, “Take all you want. I assure you that there is nothing wrong here.”')
            print('"You find bags next to the door and stuff them with everything. You exit the mansion, becoming a billionaire in one day.')
            sys.exit()

        else:
            print()
            print("Invalid Input")




def leave_mansion():
    print()
    print("You left the mansion and went back home.")
    sys.exit()




if __name__ == "__main__":
    main()