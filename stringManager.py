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
    #if the previous list is shorter than the latter
    #flipping this later will be easy, i.e. len(first) > len(second)
    elif(len(first) < len(second)): #if first picture has smaller height of second picture

        for i in range(0, len(second)):

            if(second[i][0] != '-'):

                for j in range(0, len(first[0])): 
                    temp += " "
                master.append(temp+second[i])
                temp = ""

            elif(second[i][0] == '-'):
                
                for j in range(i, len(second)):
                    
                    if(j < len(first)): #when the first runs out of space, switch to appending just the second
                        master.append(first[j]+second[j])
                    else:
                        master.append(len(first[len(first)-1])*" "+second[j])
                break
                
    return("\n".join(master))
