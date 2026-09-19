x = 2000

if x % 4 == 0:
    
    if x % 100 == 0:
        if x % 400 == 0:
            
            print("Leap year") 
        else:
            print("Not a leap year")  
    else:
        print("Leap year") 
else:
    print("Not a leap year")