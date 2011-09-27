##ver 0.3
##     Guessing Game v0.3
##     Add a menu at the beginning of the program where the user can choose an
##     "easy" version and a "hard" version.
##     The easy version gives the user 7 chances to find a number between 1 and 20.
##     The hard version gives the user 10 chances to find a number between 1 and 100.
import random
count =0
inp=1
print "1. Easy"
print "2. Hard"
mode=int(raw_input("Enter your choice (1 or 2): "))
if (mode==1):
    randnum=random.randint(1, 20)
    while (inp!=0 and count<7):
            inp=int(raw_input("Guess a number between 1 & 20.  Enter 0 to give up! : "))
            count+=1
            if (inp-randnum>0):
                print "TOO HIGH!"
            elif(inp-randnum<0):
                print "TOO LOW!"
            if (inp==randnum):
                print count,"guesses were made!"
                cont=raw_input("Do you want to play again? (Y or N) : ")
                if (cont=='Y'):
                    count = 0
                else:
                    print "BYE!"
            elif (inp==0):
                count-=1
                print "You quit,", count," guesses were made!"
                print "The correct answer is", randnum
                exit
            elif(count==6):
                print count," guesses were made!"
                print "The correct answer is", randnum
                cont=raw_input("Do you want to play again? (Y or N) : ")
                if (cont=='Y'):
                    count = 0
                else:
                    print "BYE!"
                    exit()
elif (mode==2):
        randnum=random.randint(1, 100)
        while (inp!=0 and count<10):
            inp=int(raw_input("Guess a number between 1 & 100.  Enter 0 to give up! : "))
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