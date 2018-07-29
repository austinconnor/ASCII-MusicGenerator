import string
import stringManager as sm

beats = 0
note = 0

def getTime():
    return [beats, note]

def setTime(time, master):
    if(time == "4/4"):
        beats = 4
        note = 4
        string = ''' 
      
      
      
--/|--
 / |  
/__|--
   |  
--/|--
 / |  
/__|--
   |  
------
      
      
      
 '''

    if(time == "3/4"):
        beats = 3
        note = 4
        string = ''' 
      
      
      
-__---
   )  
--<---
 __)  
--/|--
 / |  
/__|--
   |  
------
      
      
      
 '''

    if(time == "2/4"):
        beats = 2
        note = 4
        string = ''' 
      
      
      
-__---
   )  
--/---
 /__  
--/|--
 / |  
/__|--
   |  
------
      
      
      
 '''
    return sm.concat(master.splitlines(),string.splitlines())


def checkTime():
    return