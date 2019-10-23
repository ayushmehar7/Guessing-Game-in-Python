#GUESSING GAME:
    #I'm going to store a random number ,you have to guess it.
    #If you're closer than 10 , I'll say WARM.
    #If you're farther than 10 I'll say COLD.
    #Let's PLAY!!


from random import randint
random_number= randint(1,100)



a = True
guess_list =[]



while a:
    n = int(input("Please enter your guess :"))
    
    
    if n!=random_number:
        guess_list.append(n)
        
    
    if n == random_number:
        
        print("Finally ,you guessed it right!! in {} guessess".format(len(guess_list)+1))
        
        a =False
    
    elif abs(random_number-n in range(1,11)):
        
        print("WARM!!")
        
        
    else:
        
        print("COLD!!")
        

