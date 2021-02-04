def letterPos(w, x):
   
    for i in range(0, len(w)):
        
        if w[i] == x:
            
            return i + 1 
    return 0

print (letterPos("sunshine", "b"))