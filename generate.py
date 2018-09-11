import string
import stringManager as sm
import note as n
import random as r



def gen(clef, key, time, master, measures):
    r.seed()
    #dis is the maximum number of diatonic steps between notes
    dis = 4
    MAXIND = 14
    MININD = 0

    totalBeats = 0
    durations = [1,2,4,8] # need to add 3 and 6
    if(clef == "treble"): # Getting range of usable notes
        notes = n.getTreble()
    elif(clef == "bass"):
        notes = n.getBass()
    # beats for measures in that time signature, aka. how many eighth notes there are
    beatsPerMeasure = (int(8/int(time[2]) * int(time[0])))
    beats = beatsPerMeasure * measures #can expand number of measures here
    # gonna add settings to randomize note duration or set it manually (keep it static)
    # Find root note
    root = n.getRoot(clef ,key)
    ind = notes.index(root)
    leftInMeasure = beatsPerMeasure

    while(totalBeats < beats):

        dif = beats - totalBeats
        dur = 0
        pitch = ""
        while(1):
            dur = durations[r.randint(0,3)] # make sure that the note duration doesn't exceed the 4 measures
            if(dur <= dif and dur <= leftInMeasure):
                break
        while(1):
            if(totalBeats == 0 or dif == dur): #if the note is first or last
                pitch = root
                totalBeats += dur
                leftInMeasure -= dur
                break
            else:
                if(ind == MININD):
                    ind = r.randint(MININD, ind+dis)
                elif(ind == MAXIND):
                    ind = r.randint(ind-dis, MAXIND)
                else:
                    ind = r.randint(ind-dis, ind+dis)
                if(ind < MININD): ind = MININD
                if(ind > MAXIND): ind = MAXIND
                pitch = notes[ind]
                totalBeats += dur
                leftInMeasure -= dur
                break
        master = n.createNote(pitch, dur, clef, master)
        if(leftInMeasure == 0):
            if(totalBeats < beats):
                master = barLine(master)
                leftInMeasure = beatsPerMeasure
            else:
                master = DbarLine(master)
        


    return master




def barLine(master):
    string = ''' 
   
   
   
-┬-
 | 
-|-
 | 
-|-
 | 
-|-
 | 
-┴-
   
   
   
 '''

    return sm.concat(master.splitlines(), string.splitlines())

def DbarLine(master):
    string = ''' 
   
   
   
-┬┐
 ||
-||
 ||
-||
 ||
-||
 ||
-┴┘
   
   
   
 '''

    return sm.concat(master.splitlines(), string.splitlines())