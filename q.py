import random
list1=["PINEAPPLE","ORANGE","APPLE","GRAPES", "WATERMELON", "MELON", "LYCHEE","KIWI","PEAR","MANGO","POMEGRANATE","PAPAYA","GUAVA","PLUM","CHERRY","PEACH"]
word=random.choice(list1)

print("Keep guessing letters to find out the correct fruit!")
list2=['- ']*len(word)

lettersinword=list(word)

guesslist=[]




for i in range(0,20):
    guess=input("\nGuess a letter: ")
    guess1=guess.upper()
    if guess1 in guesslist:
        print("You already guessed this letter")
    guesslist.append(guess1)
    
    if guess1 in word:
       
        for i in range(len(word)):
            if word[i]==guess1:
                list2[i]=guess1
        print("You have used these letters:",' '.join(guesslist))
        print(' '.join(list2))
  
       
        if lettersinword==list2:
           print("\nYay you win!")
           break
    else:
        print(' '.join(list2))
       


   
    
 
    



        
                
    
        
        
   
        



        
        
    
    
    
