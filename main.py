# Olga Sotiriadi
# Lab:              Lab 4
# Date:             01.31.2022, 2.1.2022, 2.3.2022
# Program description: This program called the Mortgage calculation. The program will promp user for mortage related inputs. Then it will calculate Monthly mortgage payment and closing cost.
# Input: float principal as p, float interest rate as r, float loan term as n, float property tax as tax
# Output:float monthlyMorg, float closCost
# Files: main.py, closingCost.py, monthlyMorg.py, printStatementMenu.py

import monthlyMorg, closingCost, printStatementMenu

def main():
#display a welcome message
  print("Welcome to the Mortgage Calculator.")
  #blank line
  print()

  #assign "YES" to variable 'choice'
  choice = "y"
  #while the user enters lower "y" on the quiestion if want to run the program again with new input, the program keep calling userInput, closing and monthlyMorg functions
  while choice.lower() == "y":
    print()
    monthlyMorgage, principal, annualInterestRate, years, annualPropTax = monthlyMorg.monthlyPayment()
    closingCos = closingCost.calculateClosingCost(principal)
    #see if the user wants to start Over
    print()
    output(monthlyMorgage, closingCos, principal, annualInterestRate, years, annualPropTax, closingCos)
    while True:
      try:
        choice = input("Get entries for another Mortgage Calculation (y/n)?: ")
        if choice.lower() == "y" or choice.lower() == "n":
          break
        else:
          print("Invalid! Enter 'y' or 'n'.")
          continue
      except ValueError:
        print("Invalid!")
        continue
        
  #blank line
  print()
  printStatementMenu.menu(monthlyMorgage, principal, annualInterestRate, years, annualPropTax, closingCos)
  print()
  print("Thank you for using the Mortgage Calculator. \nHave a nice day!")
   
def output(monthlyMorg, closCost,principal, annualInterestRate, years, annualPropTax, closingCos):
  print()
  #outro message
  print("Your MONTHLY PAYMENT is\t", monthlyMorg)
  print("Your CLOSING COST is\t", closingCos)
  print()

main()