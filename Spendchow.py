import os
import random
import time
Victory="\033[1;33m"
Wasted="\033[1;35m"
Okay="\033[0;30m"
Chowred="\033[1;31m"
Chowgreen="\033[1;32m"
Chowblue="\033[1;34m"
BluegreenChow="\033[1;36m"
ReverseChow="\033[1;37;40m"
def spendchow():
    os.system('clear')
    print(Chowgreen+"You have $10,000 and you need to control your spending so that you dont experience a force as you overspend your money. Chow Mian already assigned you a large expense on buying Physics textbok for $1,000. So now you only have $9,000 as your current cash."+Okay)
    WhatYouSpend=["RentExpense","FoodExpense","TaxExpense","UtilityExpense","TransportationExpense","TelephoneEpense","MiscellaneousExpense","FineExpense","ChowVaultCharges","PhysicsExpense","ForceExpense"]
    WhatYouNeed=[0,0,0,0,0,0,0,0,0,1000,0]
    #Every calculation between cash and expense will be at the every 4th week, good luck.
    ready=input(Chowred+"Are you ready for this unbelievable journey of tracking expenses, also full of forces?\n"+Okay)
    if ready =="No" or ready =="no":
        print(Wasted+"No, you are ready"+Okay)
        time.sleep(3)
    os.system('clear')
    Cash=10000
    TotalExpenses=0
    AccountsPayable=0
    Revenue=2500
    Spendtime=2
    week=1
    cheque={1: 'buy Physics Textbook'}
    amount={1: 'Costs $1000'}
    date={1: 'Week0'}
    rangee=range(11)
    lotto=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    while week<17:
        if week%2==0:
            print(Victory+"Your revenue! Take it! (Chow Face)")
            Cash=Cash+Revenue
        OneTimeSpend=0
        print(Chowred)
        Continue=input("Do you want to continue your day or track your current expenses and assets? ")
        Continue=Continue.lower()
        while True:
            if Continue=="continue":
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
                print(date)
                print(ReverseChow)
                print(f"You have spend:\n${WhatYouNeed[0]} for Rent,\n${WhatYouNeed[1]} for Food,\n${WhatYouNeed[2]} for Tax,\n${WhatYouNeed[3]} for Utility,\n${WhatYouNeed[4]} for Transits,\n${WhatYouNeed[5]} for Telepone,\n${WhatYouNeed[6]} for Minor Uses,\n${WhatYouNeed[7]} for Being Fined\n${WhatYouNeed[8]} for Chowvault's Charges,\n${WhatYouNeed[9]} for Physics,\n${WhatYouNeed[10]} for APPLYING FORCES.")
                print(Okay)
                print(f"You still have ${Cash}.")
                for boughtlotto in range(1,30):
                    if lotto[boughtlotto-1]==1:
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
        if gamble=="yes":
            print(Chowgreen+"There are 30 lotto balls and you can buy one each week.")
            print(Chowred)
            while True:
                try:
                    ball=int(input("Which number do you want to buy? "))
                    if lotto[ball-1]==1:
                        print("You already bought that, or do you want to lose all of your money on this lotto?")
                    elif ball<=0:
                        print("Chow Mian dont afford that for you!")
                    else:
                        lotto[ball-1]=1
                        cheque[Spendtime]=("buy lotto")
                        OneTimeSpend=50
                        amount[Spendtime]="Costs $"+str(OneTimeSpend)
                        date[Spendtime]="Week"+str(week)
                        WhatYouNeed[6]+=OneTimeSpend
                        Spendtime+=1
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
            category=int(input("Which category does it belongs to? 1 for rent expense, 2 for food expense, 3 for tax expense, 4 for utility expense, 5 for transportation expense, 6 for telephone expense, 7 for miscellaneous expense, 8 for fine expense, 9 for chowvault charges, 10 for physics expense, 11 for force expense. "))
            if category==1 or category==2 or category==3 or category==4 or category==5 or category==6 or category==7 or category==8 or category==9 or category==10 or category==11:
                category-=1
                WhatYouNeed[category]+=OneTimeSpend
                break
            else:
                print("These are not valid.")
        fined=random.randint(1,10)
        if fined>=8:
            print("\n")
            print(Chowred+"Oh No! You are caught by the police due to speeding! You now need to pay a fine now!"+Okay)
            cheque[Spendtime]="Being Fined By Speeding"
            OneTimeSpend=fined*50
            amount[Spendtime]="Costs $"+str(OneTimeSpend)
            date[Spendtime]="Week"+str(week)
            Spendtime+=1
            WhatYouNeed[7]+=OneTimeSpend
            print(Wasted)
            print(f"You need to pay ${OneTimeSpend}.")
            print(Okay)
            better=input("Are you feeling better now? ")
        ChargeChow=random.randint(1,20)
        if ChargeChow>=13:
            ChangeOrCharge=random.randint(1,10)
            if ChangeOrCharge<=5:
                print("\n")
                print(Victory+"The almighty ChowVault made an accounting mistake! In order to make you feel better, ChowVault decide to fund you a 'Large' amount of cash!")
                OneTimeRevenue=40*ChangeOrCharge
                amount[Spendtime]="Costs $"+str(OneTimeRevenue)
                date[Spendtime]="Week"+str(week)
                Spendtime+=1
                Cash=Cash+OneTimeRevenue
                print (f"Congratualtions!! You earned ${OneTimeRevenue}.")
                print (Okay)
                better=input("Are you feeling better now? ")
            elif ChangeOrCharge>5:
                print("\n")
                print(Chowred+"ChowVault text message : A 'small' amount of maintainance fee is charged for maintaining an ChowVault account that was messed up by a Thief Chow Mian!"+Okay)
                cheque[Spendtime]="Being charged for maintenance fee"
                OneTimeSpend=ChangeOrCharge*40
                amount[Spendtime]="Costs $"+str(OneTimeSpend)
                date[Spendtime]="Week"+str(week)
                Spendtime+=1
                WhatYouNeed[9]+=OneTimeSpend
                print(Wasted)
                print(f"Opps! You need to pay ${OneTimeSpend} for ChowVault.")
                print(Okay)
                better=input("Are you feeling better now? ")
        if week%4==0:
            prize=random.randint(1,30)
            print(Victory+"Its the monthly Lotto time! Lets see who will win the royal Chow Mian Prize! ")
            time.sleep(0.5)
            print("The winner is..........")
            time.sleep(0.5)
            print(f"Ball No.{prize-1}!!!")
            if lotto[prize-1]==1:
                print(Victory+"Congratulations! Your Chow Mian Lotto wins a prize!")
                Cash+=2000
            else:
                print(Wasted+"Sorry, you dont win the prize this time! ChowVault hope you win it next time!")
            lotto=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            print(Okay)
            better=input("Are you feeling better now? ")
        print(Chowgreen+"Current expense cheques:")
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
            print(Chowred+"Oh No! You need to pay your monthly expense now!\n")
            TotalExpenses = WhatYouNeed [0] + WhatYouNeed [1] + WhatYouNeed [2] + WhatYouNeed [3] + WhatYouNeed [4] + WhatYouNeed [5] + WhatYouNeed [6] + WhatYouNeed [7] + WhatYouNeed [8] + WhatYouNeed [9] + WhatYouNeed [10]
            Cash = Cash - TotalExpenses
            Cash =Cash-AccountsPayable
            print(Wasted)
            print(f"You need to pay ${TotalExpenses}.")
            cheque={}
            amount={}
            date={}
            for i in rangee:
                WhatYouNeed[i]=0
            Spendtime=1
            if Cash>=0:
                print(Okay)
                print(f"Now you have ${Cash} in your bank.")
            else:
                print(Wasted)
                AccountsPayable=0-Cash
                print(f"Oh No! You are bankrupt! However, your budget dont stop now. You now have an accounts payable of ${AccountsPayable} an you need to pay it ASAP.")
                Cash=0
            print(Okay)
        week+=1
        if week==17:
            print(Chowblue)
            result=input("You complete the game! Do you want to see your final results? ")
            result=result.lower()
            if result=="yes":
                print(Chowgreen+"As you wish. (Chow Face)")
            elif result=="no":
                print(Wasted+"No, you want.")
            time.sleep(2)
            break
        ready=input("Are you ready for the next day? ")
        if ready=="no" or ready =="No":
            print("No, you are.")
        time.sleep(3)
        os.system('clear')
        print(Victory+"A new week to keep track of your money!"+Okay)
    os.system('clear')
    if AccountsPayable>0:
        print(Wasted+"Oh No! You failed to manage your expenses as you owe Chow Mian some money!")
        if AccountsPayable>=200:
            print(f"You only owed ${AccountsPayable} from Chow Mian. Good try but failed, so your result is...")
            print(Chowred+"IM GONNA APPLY A FORCE!")
        elif AccountsPayable>=2000:
            print(f"You are failing this task slightly by oweing ${AccountPayable}, maybe next time you need to be alert. However, now you are only...")
            print(Chowred+"EXPERIENCING A FORRRCEEEE!!!")
        elif AccountsPayable>=20000:
            print(f"This is your big failure. You owes ${AccountsPayable}!! You definitely need to practice more or else you cannot even live. I hope you will learn under...")
            print(Chowred+"THIS FOOORRRRRCCCCEEEEEEEE!!!!!")
        elif AccountsPayable>=1000000:
            print(Chowred)
            print(f"What are you doing to owe ${AccountsPayable}! You dont respect Chow Mian's money and it is your pleasure to recive...")
            print("A LARRRRGGEEEE FOOOOORRRRRRCCCCCEEEEEEEEE!!!!!")
        else:
            print(Chowred)
            print(f"What! ${AccountsPayable}!!! Chow Mian is broke! Chow Mian never want to work with you again. And before that...")
            print("IM GONNNNAAAAA AAPPPPLLLYYYYYY AAAAAA FFOOOORRRRCCCEEEEEEEEE!!!!!!!!!!!!!!!")
    else:
        print(Victory+"Congratulations! You successfully managed your expenses within 4 months!")
        if Cash<=500:
            print(f"You only have ${Cash} left, so suspenseful.")
        elif Cash<=2500:
            print(f"You managed to keep ${Cash} of cash in your bank, and now you can safely store them in your savings!")
        elif Cash<=10000:
            print(f"Wow! You saved ${Cash}! You can enjoy your wealth for at least one month!")
        elif Cash<=29000:
            print(f"Oh My God! You must be starving and tiring to save ${Cash}! Poor player, now you can spend them freely!")
        else:
            print(ReverseChow+"How are you getting so much money in your bank! You are either too lucky or you are a Hacker! Chow Mian HATES HACKERS!!!")
            print(Chowred+"IM GONNA APPLY A FOOORRRRRCCCCCEEEEEEEEEEEEE!!!!!")
            #A Fun Fact: If you put a large enough negative number in one of your expense entry will cause this situation, which is unfair and nonrelistic.
spendchow()
