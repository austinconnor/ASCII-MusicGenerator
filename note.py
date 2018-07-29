import string
import stringManager as sm

# Two octave range for each clef, two spaces below staff and two spaces above staff
TrebleNotes = ["B5", "A5", "G5", "F5", "E5", "D5", "C5", "B4", "A4", "G4", "F4", "E4", "D4", "C4", "B3"]
BassNotes = ["D4", "C4", "B3", "A3", "G3", "F3", "E3", "D3", "C3", "B2", "A2", "G2", "F2", "E2", "D2"]

def createNote(pitch, duration, clef, master):
    #trying to automate the note building process
    #duration, eighth = 1, quarter = 2, half = 4, dotted half = 6, whole = 8
    note = [" ",
            "     ",
            "     ",
            "     ",
            "-----",
            "     ",
            "-----",
            "     ",
            "-----",
            "     ",
            "-----",
            "     ",
            "-----",
            "     ",
            "     ",
            "     ",
            " "]
    
    index = 0
    s = ""
    if(clef == "treble"):
        index = TrebleNotes.index(pitch)+1
    elif(clef == "bass"):
        index = BassNotes.index(pitch)+1

    if(index < 8):
        if(duration == 1):
            note[index] = note[index][:1] + "(x)" + note[index][4:]
            note[index+1] = note[index+1][:1] + "|" + note[index+1][2:]
            note[index+2] = note[index+2][:1] + "|" + note[index+2][2:]
            note[index+2] = note[index+2][:2]+"/" + note[index+2][3:]
        elif(duration == 2):
            note[index] = note[index][:1] + "(x)" + note[index][4:]
            note[index+1] = note[index+1][:1] + "|" + note[index+1][2:]
            note[index+2] = note[index+2][:1] + "|" + note[index+2][2:]
        elif(duration == 4):
            note[index] = note[index][:1] + "( )" + note[index][4:]
            note[index+1] = note[index+1][:1] + "|" + note[index+1][2:]
            note[index+2] = note[index+2][:1] + "|" + note[index+2][2:]
        elif(duration == 8):
            note[index] = note[index][:1] + "( )" + note[index][4:]
    elif(index >= 8):
        if(duration == 1):
            note[index] = note[index][:1] + "(x)" + note[index][4:]
            note[index-1] = note[index-1][:3] + '|' + note[index-1][4:]
            note[index-2] = note[index-2][:3] + '|' + note[index-2][4:]
            note[index-2] = note[index-2][:4] + '\\' + note[index-2][5:]
        elif(duration == 2):
            note[index] = note[index][:1] + "(x)" + note[index][4:]
            note[index-1] = note[index-1][:3] + '|' + note[index-1][4:]
            note[index-2] = note[index-2][:3] + '|' + note[index-2][4:]
        elif(duration == 4):
            note[index] = note[index][:1] + "( )" + note[index][4:]
            note[index-1] = note[index-1][:3] + '|' + note[index-1][4:]
            note[index-2] = note[index-2][:3] + '|' + note[index-2][4:]
        elif(duration == 8):
            note[index] = note[index][:1] + "( )" + note[index][4:]
            
    
       
            

    return(sm.concat(master.splitlines(), '\n'.join(note).splitlines()))



#Trying to automate the building of notes...


#sketching notes
#---|\-
#   |
#-(x)-
# |   
#\|----
#
#-( )--
#
#------