import string
import stringManager as sm
import note as n
import random as r



def gen(clef, key, time, master):
    totalBeats = 0
    beats = int(time[0])
    k = key[0]
    beats = beats * 8 # beats for 4 measures in that time signature, aka. how many eighth notes there are
    # gonna add settings to randomize note duration or set it manually (keep it static)


    




def barLine(master):
    string = ''' 
   
   
   
-|-
 | 
-|-
 | 
-|-
 | 
-|-
 | 
-|-
   
   
   
 '''

    return sm.concat(master.splitlines(), string.splitlines())

def DbarLine(master):
    string = ''' 
   
   
   
-|┐
 ||
-||
 ||
-||
 ||
-||
 ||
-|┘
   
   
   
 '''

    return sm.concat(master.splitlines(), string.splitlines())