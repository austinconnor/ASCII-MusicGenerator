import string
import stringManager as sm
import note as n
import key as k
import clef as c
import timeSig as ts


def gen(clef, key, time, master):



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