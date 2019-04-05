#variables and objects

def vendingMachine ();  #creates the vending machine object
      count = 0         # defines the variable and gives it value of 0, using this to move through the coinNum
      totalCredit = 0   # defines the totalCredit variable and gives it value of 0
      coinNum = int (input ("how many coins would you like to enter: ")) # defining coinNUm variable and pushing out a string that takes in an int input


#Logic
      while count in range (coinNum) :    #first logic , while count is in range of coinNum
          coin = float ( input ("Enter Coin: $  ")) # this rounds
          totalCredit = totalCredit + coin
          count = count + 1    #when this reaches the



    print("You have ${0} in your bank.".format (round (totalCredit, 2)))   # rounding the int entered to the second decimal this will remove all 0's past the second decimal
    print("")
    print("Choose your item:")
    print("")
    print("1.Coca-Cola")
    print("2.Walkers Cheese & Onion")
    print("3.Pepsi")
    print("4.root Beer")
    print("5.Coca-Cola")
    print("")
    finalCredit = totalCredit
    round (finalCredit, 2)
    item = int (input ("Enter the number for your item: "))   # making the item equivalent to the number the user enters
    while item <1 or item >5:  # we have only 5 items, if the user enters an int that is higher than what we have specified then...
            print ("This item is not available.")  #this will print
            item = int (input ("Enter the number for your item: ")) # this will loop around as long as the user chooses the wrong item
    if item == 1:
        finalCredit = totalCredit - 0.59    # we are setting the price or each while at the same time deducting money from totalCredit
        print ("You now have a Coca- Cola can, costing $0.59.")
        print ("You have {0} remaining in your bank.".format (round(finalCredit,2))) #displaying the current value of totalCredit
    elif item = 2:
        finalCredit = totalCredit - 0.75
        print("You now have a Walkers Cheese & Onion, costing 0.75")
        print("You have {0} remaining in your bank.".format (round(finalCredit,2)))
    elif item = 3:
        finalCredit = totalCredit - 0.99
        print("You now have a Pepsi, costing 0.99")
        print("You have {0} remaining in your bank.".format (round(finalCredit,2)))
    elif item = 4:
        finalCredit = totalCredit - 0.99
        print("You now have a root Beer, costing 0.99")
        print("You have {0} remaining in your bank.".format (round(finalCredit,2)))
    elif item = 5:
        finalCredit = totalCredit - 0.99
        print("You now have a coca-cola, costing 0.99")
        print("You have {0} remaining in your bank.".format (round(finalCredit,2)))
    else:
        print ("This is not an option")
    print ("")
    print ("The rest of your money, ${0} has been outputted").format (round(finalCredit,2)))

    vendingMachine()
