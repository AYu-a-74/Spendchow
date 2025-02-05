import os
<<<<<<< HEAD
=======
import random
import time
>>>>>>> ae6034dd9c0a0b5d40b24eb0273c7388a4d363b2
Victory="\033[1;33m"
Wasted="\033[1;35m"
Okay="\033[0;30m"
Chowred="\033[1;31m"
Chowgreen="\033[1;32m"
Chowblue="\033[1;34m"
BluegreenChow="\033[1;36m"
ReverseChow="\033[1;37;40m"
<<<<<<< HEAD
def spendchow():
    os.system('clear')
    print(Chowgreen+"You have $10,000 and you need to control your spending so that you dont experience a force as you overspend your money. Chow Mian already assigned you a large expense on buying Physics textbok for $1,000. So now youu only have $9,000 as your current cash."+Okay)
spendchow()

TotalExpenses = WhatYouNeed [0] + WhatYouNeed [1] + WhatYouNeed [2] + WhatYouNeed [3] + WhatYouNeed [4] + WhatYouNeed [5] + WhatYouNeed [6] + WhatYouNeed [7] + WhatYouNeed [8] + WhatYouNeed [9] + WhatYouNeed [10]
Revenue = NetIncome - TotalExpenses







=======
WhatYouSpend=["RentExpense","FoodExpense","TaxExpense","UtilityExpense","TransportationExpense","TelephoneEpense","MiscellaneousExpense","FineExpense","ChowVaultCharges","PhysicsExpense","ForceExpense"]
WhatYouNeed=[0,0,0,0,0,0,0,0,0,1000,0]
def spendchow():
    os.system('clear')
    print(Chowgreen+"You have $10,000 and you need to control your spending so that you dont experience a force as you overspend your money. Chow Mian already assigned you a large expense on buying Physics textbok for $1,000. So now youu only have $9,000 as your current cash.\n"+Okay)
    #Every calculation between cash and expense will be at the every 4th week, good luck.
    ready=input(Chowred+"Are you ready for this unbelievable journey of tracking expenses, also full of forces?\n"+Okay)
    if ready =="No" or ready =="no":
        print(Wasted+"No, you are ready"+Okay)
        time.sleep(3)
    os.system('clear')
    Cash=10000
    TotalExpenses=0
    NetIncome=0
    Revenue=2500
    Spendtime=2
    week=1
    cheque={1: 'buy Physics Textbook'}
    amount={1: 'Costs $1000'}
    date={1: 'Week0'}
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
            else:
                print(Wasted+"I will consider that you said 'continue'.")
                time.sleep(2)
                break
            print(Chowred)
            Continue=input("Do you want to continue your day now? ")
        os.system('clear')
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
        week+=1
        ready=input("Are you ready for the next day? ")
        if ready=="no" or ready =="No":
            print("No, you are.")
        time.sleep(3)
        os.system('clear')
        print(Victory+"A new week to keep track of your money!"+Okay)
spendchow()
>>>>>>> ae6034dd9c0a0b5d40b24eb0273c7388a4d363b2
