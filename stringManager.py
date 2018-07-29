import string

def concat(first,second):
    master = [] 
    temp = ""
    #if the lists are the same length
    
    # print("First: "+str(len(first)))
    # print("Second: "+str(len(second)))
   
    if(len(first) == len(second)):
        
        for i in range(0, len(second)):
            master.append(first[i]+second[i])

                
    return("\n".join(master))
