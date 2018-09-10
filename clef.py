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
c = ""
def getClef():
    return c

def setClef(clef):
    c = clef
    if(clef == "treble"):
        
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