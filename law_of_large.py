import random 
def coinToss():
    number = int(input("Coin Toss Amount : "))
    trials = 0
    head = 0
    tails = 0

    for amount in range (number):
        outcome = random.randint(0,1)
        if(outcome == 1):
            head += 1
            trials += 1
        else:
            tails += 1
            trials += 1
        # if(trials % 100 == 0):
        #     print(head - (trials/2))
        
    
    print(head - (trials/2))
    print(head/trials)
coinToss()

