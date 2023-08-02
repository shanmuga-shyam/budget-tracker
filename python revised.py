budgets=[]
budget1={'amount':'1000','category':'food'}
budgets.append(budget1)
budget2={'amount':'2000','category':'grocieres'}
budgets.append(budget2)
def removebudget():
    while True:
        listbudgets()
        print("what budget do u like to remove?")
        try:
          budgetToRemove= int(input("> "))
          del budgets[budgetToRemove]
          break
        except:
          print("Invaild input, please try again.")


def addbudget(amount,category):
    budget={'amount':amount,'category':category}
    budgets.append(budget)
    



def printMenu():
    print("choose from one of the following options....")
    print("1. Add new budget")
    print("2. Remove an budget")
    print("3. list all budget")

def listbudgets():
    print("\nHere is a list of your budgets...")
    print("-----------------------------------")
    counter=0
    for budget in budgets:
        print("#",counter,"-",budget['amount'],"-",budget['category'])
        counter +=1
    print("\n\n")
    

if __name__ =="__main__":
    while True:
      ### prompt the user
      printMenu()
      optionSelected=input("> ")

      if(optionSelected=="1"):
          print("How much was the budget?")
          while True:
              try:
                amountToAdd=input("> ")
                break
              except:
                  print("Invaild input, please try again.")
                  
          print("what category was the budget?")
          while True:
              try:
                category=input("> ")
                break
              except:
                  print("Invaild input,please try again.")

          addbudget(amountToAdd, category)
      elif(optionSelected=="2"):
        removebudget()
      elif(optionSelected=="3"):
        listbudgets()
      else:
        print("Invaild input, plesae try again.")
          
