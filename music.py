import clef as c
import sys
import key
import stringManager

#ACII ART CREDIT: http://www.chris.com/ascii/index.php?art=music/musical%20notation

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
    master = key.setKey(choice,clef,master) #sets key, adds key signature
    print(master)

if __name__ == '__main__':
    main()