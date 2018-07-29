import string
import stringManager as sm

# Two octave range for each clef, two spaces below staff and two spaces above staff
TrebleNotes = ["B5", "A5", "G5", "F5", "E5", "D5", "C5", "B4", "A4", "G4", "F4", "E4", "D4", "C4", "B3"]
BassNotes = ["D4", "C4", "B3", "A3", "G3", "F3", "E3", "D3", "C3", "B2", "A2", "G2", "F2", "E2", "D2"]

def createNote(pitch, duration, clef, master):
    #trying to automate the note building process
    note = [" \n",
            "     \n",
            "     \n",
            "     \n",
            "-----\n",
            "     \n",
            "-----\n",
            "     \n",
            "-----\n",
            "     \n",
            "-----\n",
            "     \n",
            "-----\n",
            "     \n",
            "     \n",
            "     \n",
            " "]
    index = 0

    if(clef == "treble"):
        index = TrebleNotes.index(pitch)+1
    elif(clef == "bass"):
        index = BassNotes.index(pitch)+1

    for i in range(0,17):
        if(i == 0):
            note += ' \n'

        if(i == index and i % 2 == 0 and duration == 4):
            note += '-(x)-'
        elif(i <= 3):
            note += 5*' '
            note += '\n'
        elif(i > 3 and i < 13 and i % 2 == 0):
            note += 5*'-'
            note += '\n'
        elif(i < 3 and i < 13 and i % 2 != 0):
            note += 5*' '
            note += '\n'
        elif(i >= 13):
            note += 5*' '
            note += '\n'
        elif(i == 16):
            note += ' '
            

        



    return



#Trying to automate the building of notes...


#sketching notes
#---|\-
#   |
#-(x)--
#   |
#---|--
#
#-( )--
#
#------