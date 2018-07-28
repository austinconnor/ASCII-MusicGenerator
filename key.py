import string
import stringManager as sm

def setKey(key,clef,master):
    sharps = ['F','C','G','D','A','E','B']
    flats = ['B','E','A','D','G','C','F']

    # if (key == 'C'):
    #     #no sharps or flats
    # elif (key == 'G'):
    #     #1 sharp
    # elif (key == 'D'):
    #     #2 sharps
    # elif (key == 'A'):
    #     #3 sharps
    # elif (key == 'E'):
    #     #4 sharps
    # elif (key == 'B'):
    #     #5 sharps
    # elif (key == 'F#'):
    #     #6 sharps
    # elif (key == 'C#'):
    #     #7 sharps
    if (key == 'F'):
        string = ''' 
-----

-----
|
|)---

-----

-----'''
    elif (key == 'Bb'):
        string = ''' 
--|--
  |)
-----
|
|)---

-----

-----'''
    elif (key == 'Eb'):
        string = ''' 
--|----
  |)
-------
|
|)---|-
     |)
-------

------'''
    # elif (key == 'Ab'):
    #     #4 flats
    # elif (key == 'Db'):
    #     #5 flats
    # elif (key == 'Gb'):
    #     #6 flats
    # elif (key == 'Cb'):
    #     #7 flats

    return(sm.concat(master.splitlines(), key.splitlines()))