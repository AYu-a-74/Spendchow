import os
Victory="\033[1;33m"
Wasted="\033[1;35m"
Okay="\033[0;30m"
Chowred="\033[1;31m"
Chowgreen="\033[1;32m"
Chowblue="\033[1;34m"
BluegreenChow="\033[1;36m"
ReverseChow="\033[1;37;40m"
WhatYouSpend=["RentExpense","TaxExpense","UtilityExpense","TransportationExpense","TelephoneEpense","MiscellaneousExpense","FineExpense","ChowVaultCharges","PhysicsExpense","ForceExpense"]
WhatYouNeed=[0,0,0,0,0,0,0,0,1000,0]
Cash=10000
TotalExpenses=0
NetIncome=0
Revenue=2500
def spendchow():
    os.system('clear')
    print(Chowgreen+"You have $10,000 and you need to control your spending so that you dont experience a force as you overspend your money. Chow Mian already assigned you a large expense on buying Physics textbok for $1,000. So now youu only have $9,000 as your current cash."+Okay)
    #Every calculation between cash and expense will be at the every 4th week, good luck.
spendchow()