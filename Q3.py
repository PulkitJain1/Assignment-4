import math
from random import randint
gamenumber=0
while gamenumber<10:
    x=randint(1,10)
    y=randint(1,10)
    print("the multiplication of", x, "*", y)
    a=int(input("your answer"))
    if a==x*y:
        print("correct")
    else:
        print("incorrect", "correct value=", x*y)
    gamenumber+=1

else:
    print("the game is ended")

