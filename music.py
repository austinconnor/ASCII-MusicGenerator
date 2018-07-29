import clef as c
import sys
import key as k
import note
import timeSig as ts
import generate
import stringManager

#ASCII ART CREDIT: http://www.chris.com/ascii/index.php?art=music/musical%20notation

def main():
    print("Welcome to Connor's ASCII sheet music generator!")
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
    print("Enter a time signature: (i.e. '4/4', '3/4', '6/8')")
    choice = input("> ")
    time = choice
    master = ts.setTime(choice, master)
    print(master)
    choice = input("Press ENTER to generate music!")
    #master = generate.gen(clef, key, time, master)
    master = note.createNote("F4", 2, clef, master)
    master = note.createNote("G4", 2, clef, master)
    master = note.createNote("A4", 2, clef, master)
    master = note.createNote("B4", 2, clef, master)
    master = generate.barLine(master)
    master = note.createNote("C5", 2, clef, master)
    master = note.createNote("D5", 2, clef, master)
    master = note.createNote("E5", 2, clef, master)
    master = note.createNote("F5", 2, clef, master)
    master = generate.DbarLine(master)

    print(master)

    

if __name__ == '__main__':
    main()