##ver 0.2
import random
randnum=random.randint(1, 50)
count =0
inp=1
while (inp!=0 and count<10):
    inp=int(raw_input("Guess a number between 1 & 50. Enter 0 to give up! : "))
    count+=1
    if (inp-randnum>0):
        print "TOO HIGH!"
    elif(inp-randnum<0):
        print "TOO LOW!"
    if (inp==randnum):
        print count,"guesses were made!"
    elif (inp==0):
        count-=1
        print "You quit,", count," guesses were made!"
        print "The correct answer is", randnum
        exit
    elif(count==9):
        cont=raw_input("Do you want to play again? (Y or N) : ")
    if (cont=='Y'):
        count =0
    else:
        print "BYE!"
