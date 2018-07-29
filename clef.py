import string
import stringManager as sm

staff_begin = ''' 
   
   
 / 
|+-
|| 
||-
|| 
||-
|| 
||-
|| 
|+-
 \\ 
   
   
 '''

def setClef(clef):
    if(clef == "treble"): #PROGRESS
        
        string = ''' 


    /\\   
----|-|--
    |/   
----|----
   /|    
--/-|----
 |  | _  
-|-(@)-)-
  \ | /  
----|----
    |    
  (_|
  
 '''
  
    elif(clef == "bass"):
        string =''' 
       
       
       
-------
 ,-.   
-o  |:-
   /   
--/----
 /     
-------
       
-------
       
       
       
 '''
    master = sm.concat(staff_begin.splitlines(),string.splitlines())
    return master