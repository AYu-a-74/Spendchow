import os # a funciton to clear screen
import random # a funciton used for genreating random number 
import time # diffferent colour refer to different emotions
Victory="\033[1;33m" # diffferent colour refer to different emotions
Wasted="\033[1;35m"
Okay="\033[0;30m"
Chowred="\033[1;31m"
Chowgreen="\033[1;32m"
Chowblue="\033[1;34m"
BluegreenChow="\033[1;36m"
ReverseChow="\033[1;37;40m"
def spendchow():
    os.system('clear') # clear the screen
    print(Chowgreen+"You have $10,000 and you need to control your spending so that you dont experience a force as you overspend your money. Chow Mian already assigned you a large expense on buying Physics textbok for $1,000. So now you only have $9,000 as your current cash."+Okay)
    WhatYouSpend=["RentExpense","FoodExpense","TaxExpense","UtilityExpense","TransportationExpense","TelephoneEpense","MiscellaneousExpense","FineExpense","ChowVaultCharges","PhysicsExpense","ForceExpense"]
    WhatYouNeed=[0,0,0,0,0,0,0,0,0,1000,0]  # the amount of expenses in each categories
    #Every calculation between cash and expense will be at the every 4th week, good luck.
    ready=input(Chowred+"Are you ready for this unbelievable journey of tracking expenses, also full of forces?\n"+Okay)
    if ready =="No" or ready =="no": # if the user enter no, activate the following code 
        print(Wasted+"No, you are ready"+Okay) # force you to be ready :)
        time.sleep(3)
    os.system('clear') #clear screen
    Cash=10000 #main cash
    TotalExpenses=0
    AccountsPayable=0
    Revenue=2500 # revenue for every 2 weeks
    Spendtime=2
    week=1 # record week 1 expenditure
    cheque={1: 'buy Physics Textbook'}
    amount={1: 'Costs $1000'}
    date={1: 'Week0'}
    rangee=range(11) # range used to reset all of the expenses
    lotto=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #current state of your owning. 0 = you dont have it. 1 = you have it
    while week<17: # week 17 will end. all week before week 17 will continue the follwoing program 
        if week%2==0: # every two week , activate the following code 
            print(Victory+"Your revenue! Take it! (Chow Face)")
            Cash=Cash+Revenue # formula for adding revenue into the cash 
        OneTimeSpend=0
        print(Chowred)
        Continue=input("Do you want to continue your day or track your current expenses and assets? ")
        Continue=Continue.lower()
        while True:
            if Continue=="continue": # is the user enter continue, activate following code 
                print(Chowgreen+"As you wish. (Chow Face)"+Okay)
                time.sleep(2)
                break
            elif Continue=="track": 
                print(BluegreenChow+"As you wish. (Chow Face)")
                print(Chowgreen+"Current expense cheques:")
                print(cheque) 
                print(Victory+"Current amount spend:")
                print(amount) 
                print(BluegreenChow+"Current expense date:")
                print(date) # pritn your date of your expesnes
                print(ReverseChow)
                print(f"You have spend:\n${WhatYouNeed[0]} for Rent,\n${WhatYouNeed[1]} for Food,\n${WhatYouNeed[2]} for Tax,\n${WhatYouNeed[3]} for Utility,\n${WhatYouNeed[4]} for Transits,\n${WhatYouNeed[5]} for Telepone,\n${WhatYouNeed[6]} for Minor Uses,\n${WhatYouNeed[7]} for Being Fined\n${WhatYouNeed[8]} for Chowvault's Charges,\n${WhatYouNeed[9]} for Physics,\n${WhatYouNeed[10]} for APPLYING FORCES.") # print how many do the user spend 
                print(Okay)
                print(f"You still have ${Cash}.") # remaining cash 
                for boughtlotto in range(1,30): #user can buy lotto, lotto takes value from 1 to 29
                    if lotto[boughtlotto-1]==1: #ser owns that lottery ball by looking it up in the lotto list if it's a 1, they have it.
                        print(f"You have ball No.{boughtlotto}.")
            else:
                print(Wasted+"I will consider that you said 'continue'.")
                time.sleep(2)
                break
            print(Chowred)
            Continue=input("Do you want to continue your day now? ")
        os.system('clear')
        print(Victory+"Lotto time! You can use $50 to buy a lotto number, and every month, we will have a winner!")
        gamble=input(Chowred+"Do you want to buy that lotto? ")
        gamble=gamble.lower()
        if gamble=="yes": #if the answer for the previous questions is yes, activate following code
            print(Chowgreen+"There are 30 lotto balls and you can buy one each week.")
            print(Chowred)
            while True:
                try: 
                    ball=int(input("Which number do you want to buy? ")) # enter the number that the user would like to buy
                    if lotto[ball-1]==1:
                        print("You already bought that, or do you want to lose all of your money on this lotto?")
                    elif ball<=0: # if the number smaller than 0
                        print("Chow Mian dont afford that for you!")
                    else:
                        lotto[ball-1]=1
                        cheque[Spendtime]=("buy lotto") # record the event of the expenses
                        OneTimeSpend=50 # amount for the expenses
                        amount[Spendtime]="Costs $"+str(OneTimeSpend) #show the cost off the expenses
                        date[Spendtime]="Week"+str(week) # show week number (?)
                        WhatYouNeed[6]+=OneTimeSpend # add the expeses amount to the whatyouneed list categories 6 
                        Spendtime+=1 # record the user have already pass a week
                        break
                except:
                    print("Not valid")
            print(Chowblue)
            print(f"You bought No.{ball}, hope it will win the prize.")
            time.sleep(2)
        else:
            print(Chowblue+"So sad, you give up your chance to become rich.")
            time.sleep(1)
        print(Wasted+"You feel bored and you want to spend money."+Chowred)
        cheque[Spendtime]=("buy "+input("What do you want to buy?"))
        OneTimeSpend=int(input("How much is it?"))
        amount[Spendtime]="Costs $"+str(OneTimeSpend)
        date[Spendtime]="Week"+str(week)
        Spendtime+=1
        
        while True:
            category=int(input("Which category does it belongs to? 1 for rent expense, 2 for food expense, 3 for tax expense, 4 for utility expense, 5 for transportation expense, 6 for telephone expense, 7 for miscellaneous expense, 8 for fine expense, 9 for chowvault charges, 10 for physics expense, 11 for force expense. ")) # different number correspoding to different categories, the user can enter the number
            if category==1 or category==2 or category==3 or category==4 or category==5 or category==6 or category==7 or category==8 or category==9 or category==10 or category==11:
                category-=1 # minus one categories, cuz it starts at 1 in the above line 
                WhatYouNeed[category]+=OneTimeSpend # according to the number of what the user just entered, it refer to different amoutn fo expenses
                break
            else:
                print("These are not valid.")
        fined=random.randint(1,10) # use randome number to determined the fine
        if fined>=8: # if the the number is greater than 8
            print("\n")
            print(Chowred+"Oh No! You are caught by the police due to speeding! You now need to pay a fine now!"+Okay) # fine charge for spedding 
            cheque[Spendtime]="Being Fined By Speeding"
            OneTimeSpend=fined*50 # the number times 50 will be the money charged 
            amount[Spendtime]="Costs $"+str(OneTimeSpend)
            date[Spendtime]="Week"+str(week)
            Spendtime+=1
            WhatYouNeed[7]+=OneTimeSpend
            print(Wasted)
            print(f"You need to pay ${OneTimeSpend}.")
            print(Okay)
            better=input("Are you feeling better now? ")
        ChargeChow=random.randint(1,20) #use randome number to determined the charge chow
        if ChargeChow>=13: # if the number bigger than 13 
            ChangeOrCharge=random.randint(1,10) # again, draw a random number 
            if ChangeOrCharge<=5: # if the new random number is smaller than 5 
                print("\n")
                print(Victory+"The almighty ChowVault made an accounting mistake! In order to make you feel better, ChowVault decide to fund you a 'Large' amount of cash!") # reward/ bonus income 
                OneTimeRevenue=40*ChangeOrCharge # the new random number times 50 will be the money given 
                amount[Spendtime]="Costs $"+str(OneTimeRevenue)
                date[Spendtime]="Week"+str(week)
                Spendtime+=1
                Cash=Cash+OneTimeRevenue # add the extra income with the cash 
                print (f"Congratualtions!! You earned ${OneTimeRevenue}.")
                print (Okay)
                better=input("Are you feeling better now? ")
            elif ChangeOrCharge>5:# if the new random number is bigger than 5 
                print("\n")
                print(Chowred+"ChowVault text message : A 'small' amount of maintainance fee is charged for maintaining an ChowVault account that was messed up by a Thief Chow Mian!"+Okay) # charged fee
                cheque[Spendtime]="Being charged for maintenance fee"
                OneTimeSpend=ChangeOrCharge*40 # the new random number times 50 will be the money charged 
                amount[Spendtime]="Costs $"+str(OneTimeSpend)
                date[Spendtime]="Week"+str(week)
                Spendtime+=1
                WhatYouNeed[8]+=OneTimeSpend # the expesnes amount will be automatically add to category 8
                print(Wasted)
                print(f"Opps! You need to pay ${OneTimeSpend} for ChowVault.")
                print(Okay)
                better=input("Are you feeling better now? ")
        if week%4==0: #every 4 week
            prize=random.randint(1,30) # draw a randome number for the lotto. 
            print(Victory+"Its the monthly Lotto time! Lets see who will win the royal Chow Mian Prize! ")
            time.sleep(0.5)
            print("The winner is..........")
            time.sleep(0.5)
            print(f"Ball No.{prize-1}!!!") # the ball no is what the computer draw just now 
            if lotto[prize-1]==1: # if the rnadom number that was drawn just now is equal to what the user have bought at first
                print(Victory+"Congratulations! Your Chow Mian Lotto wins a prize!")
                Cash+=2000 # add 2000 in cash 
            else:
                print(Wasted+"Sorry, you dont win the prize this time! ChowVault hope you win it next time!")
            lotto=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            print(Okay)
            better=input("Are you feeling better now? ")
        print(Chowgreen+"Current expense cheques:") # a code to show the corrent expenses cheques, amount spend and expenes date 
        print(cheque)
        print(Victory+"Current amount spend:")
        print(amount)
        print(BluegreenChow+"Current expense date:")
        print(date)
        print(ReverseChow)
        print(f"You have spend:\n${WhatYouNeed[0]} for Rent,\n${WhatYouNeed[1]} for Food,\n${WhatYouNeed[2]} for Tax,\n${WhatYouNeed[3]} for Utility,\n${WhatYouNeed[4]} for Transits,\n${WhatYouNeed[5]} for Telepone,\n${WhatYouNeed[6]} for Minor Uses,\n${WhatYouNeed[7]} for Being Fined\n${WhatYouNeed[8]} for Chowvault's Charges,\n${WhatYouNeed[9]} for Physics,\n${WhatYouNeed[10]} for APPLYING FORCES.")
        print(Okay)
        print(f"You still have ${Cash}.")
        for boughtlotto in range(1,30):
            if lotto[boughtlotto-1]==1:
                print(f"You have ball No.{boughtlotto}.")
            

        if week%4==0:
            time.sleep(1)
            print(Chowred+"Oh No! You need to pay your monthly expense now!\n") #The expesens will be charged now. The cash will be deducted right now 
            TotalExpenses = WhatYouNeed [0] + WhatYouNeed [1] + WhatYouNeed [2] + WhatYouNeed [3] + WhatYouNeed [4] + WhatYouNeed [5] + WhatYouNeed [6] + WhatYouNeed [7] + WhatYouNeed [8] + WhatYouNeed [9] + WhatYouNeed [10] # add all the categories in Whatyouneed list and that will become the total expenses
            Cash = Cash - TotalExpenses # cash minus the expeenses calculated just now 
            Cash =Cash-AccountsPayable # minus the accounts patable 
            print(Wasted)
            print(f"You need to pay ${TotalExpenses}.") # print the total expenses
            cheque={}
            amount={}
            date={}
            for i in rangee:
                WhatYouNeed[i]=0
            Spendtime=1
            if Cash>=0: # if the cash is greater than 0 
                print(Okay)
                print(f"Now you have ${Cash} in your bank.") # print the amont of cash
            else: # if the cash is lower than 0
                print(Wasted)
                AccountsPayable=0-Cash # 0 - cash, let the amount become positive and that will become the accounts payable, the user have to repay afterwards
                print(f"Oh No! You are bankrupt! However, your budget dont stop now. You now have an accounts payable of ${AccountsPayable} an you need to pay it ASAP.") # print amount
                Cash=0 # cash will reset to 0
            print(Okay)
        week+=1
        if week==17: # if the week come to week 17, the game completed 
            print(Chowblue)
            result=input("You complete the game! Do you want to see your final results? ")
            result=result.lower()
            if result=="yes": # if the anser for the previous question is yes
                print(Chowgreen+"As you wish. (Chow Face)")
            elif result=="no": # if the anser for the previous question is no
                print(Wasted+"No, you want.")
            time.sleep(2)
            break
        ready=input("Are you ready for the next day? ") 
        if ready=="no" or ready =="No": # if the anser for the previous question is no
            print("No, you are.") # force you to ready :)
        time.sleep(3)
        os.system('clear')
        print(Victory+"A new week to keep track of your money!"+Okay)
    os.system('clear')
    if AccountsPayable>0: # if the account payable is greater than 0 
        print(Wasted+"Oh No! You failed to manage your expenses as you owe Chow Mian some money!") # cuz you bankrupt
        if AccountsPayable>=200: #if the account payable is greater and equal to than 200
            print(f"You only owed ${AccountsPayable} from Chow Mian. Good try but failed, so your result is...")
            print(Chowred+"IM GONNA APPLY A FORCE!")
        elif AccountsPayable>=2000: # if the account payable is greater and equal to than 2000 
            print(f"You are failing this task slightly by oweing ${AccountPayable}, maybe next time you need to be alert. However, now you are only...")
            print(Chowred+"EXPERIENCING A FORRRCEEEE!!!")
        elif AccountsPayable>=20000: # if the account payable is greater and equal to than 20000
            print(f"This is your big failure. You owes ${AccountsPayable}!! You definitely need to practice more or else you cannot even live. I hope you will learn under...")
            print(Chowred+"THIS FOOORRRRRCCCCEEEEEEEE!!!!!")
        elif AccountsPayable>=1000000: # if the account payable is greater and equal to than 1000000
            print(Chowred)
            print(f"What are you doing to owe ${AccountsPayable}! You dont respect Chow Mian's money and it is your pleasure to recive...")
            print("A LARRRRGGEEEE FOOOOORRRRRRCCCCCEEEEEEEEE!!!!!")
        else:
            print(Chowred)
            print(f"What! ${AccountsPayable}!!! Chow Mian is broke! Chow Mian never want to work with you again. And before that...")
            print("IM GONNNNAAAAA AAPPPPLLLYYYYYY AAAAAA FFOOOORRRRCCCEEEEEEEEE!!!!!!!!!!!!!!!")
    else:
        print(Victory+"Congratulations! You successfully managed your expenses within 4 months!") # :)
        if Cash<=500: # if the cash is smaller and equal to than 500 
            print(f"You only have ${Cash} left, so suspenseful.")
        elif Cash<=2500: # if the cash is smaller and equal to than 2500 
            print(f"You managed to keep ${Cash} of cash in your bank, and now you can safely store them in your savings!")
        elif Cash<=10000: # if the cash is smaller and equal to than 10000
            print(f"Wow! You saved ${Cash}! You can enjoy your wealth for at least one month!")
        elif Cash<=29000: # if the cash is smaller and equal to than 29000
            print(f"Oh My God! You must be starving and tiring to save ${Cash}! Poor player, now you can spend them freely!")
        else: # if you have many many money 
            print(ReverseChow+"How are you getting so much money in your bank! You are either too lucky or you are a Hacker! Chow Mian HATES HACKERS!!!")
            print(Chowred+"IM GONNA APPLY A FOOORRRRRCCCCCEEEEEEEEEEEEE!!!!!")
            #A Fun Fact: If you put a large enough negative number in one of your expense entry will cause this situation, which is unfair and nonrelistic.
spendchow()
