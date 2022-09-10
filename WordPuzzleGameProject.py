import random


def gen_lrandom(ltemp):
    l_li=[list(e) for e in ltemp]#to generate a list of list where inner list consists of characters
    #print(l_li)
    lr=[]
    for e in l_li: #shuffle characters in every single inner list ->  join it back to create a string and finally append the string in a new list
        random.shuffle(e)
        lr.append(''.join(e))
        
    #print(lr)
    lg=random.sample(lr,5)# Generate a list which contains sample of 5 different words as by using random.choice function, getting same words more than once
    return lg

#game function
def game(l3):
    score=0
    print("Arrange the letters to form a valid word:")
    for e in l3:
        print(e)
        ans=input()
        if ans in lans:
           print("")
           print ("Correct")
           print("")
           score=score+1
        else:
            print("")
            print("Wrong")
            print("")
            score=score-1
    print( "Net score is:", score)

#main body
l1=["WHEN", "WHOM", "WHAT", "WHY", "LOVE","CREATOR", "PLANE", "TEACHER", "SIR"]# list of words
llower=[e.lower() for e in l1]
lcap=[e.capitalize() for e in l1]
lans=l1+llower+lcap
lg1=gen_lrandom(l1)
game(lg1)

              
    
        
      
          
          



