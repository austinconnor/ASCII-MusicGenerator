import clef as c
import sys
import key as k
import note
import timeSig as ts
import generate
import stringManager

#ASCII ART CREDIT: http://www.chris.com/ascii/index.php?art=music/musical%20notation

def main():
    print("\nWelcome to Connor's ASCII sheet music generator!")
    print("------------------------------------------------")
    print("Choose a clef: (1) Treble")
    print("               (2) Bass  ")
    choice = input("> ")
    if(choice == "1"):
        clef = "treble"
        print("You chose: Treble Clef!")
    elif(choice == "2"):
        clef = "bass"
        print("You chose: Bass Clef!")
    master = c.setClef(clef)
    print(master)
    print("Enter a key: (i.e. 'Bb', 'C#', 'A')")
    choice = input("> ")
    key = choice
    master = k.setKey(choice,clef,master) #sets key, adds key signature
    print(master)
    print("Enter a time signature: (i.e. '4/4', '3/4', '2/4')")
    choice = input("> ")
    time = choice
    master = ts.setTime(choice, master)
    print(master)
    print("Enter the amount of measures you want to generate")
    measures = int(input("> "))
    choice = input("Press ENTER to generate music!")

    master = generate.gen(clef, key, time, master, measures) # music is generated here

    print(master) #prints final sheet music

    

if __name__ == '__main__':
    main()