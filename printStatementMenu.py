# ******************************************************************************
# Author: Khanh Vu
# Lab: Lab 4
# Date: 02.02.2022, 02.03.2022 
# Module Description: This module has 2 functions that relate to the Mortgage loan statement
# Source: Murach texbook
# ******************************************************************************
import locale as lc

# Set locale on most systems
result = lc.setlocale(lc.LC_ALL, "")
if result == "C":
    lc.setlocale(lc.LC_ALL, "en_US")


def menu(mthlyMortgagePmt,principal, annualInterestRate, years, annualPropTax,closingCost):
  # Function: A menu that give user options to print out statements after completing the calculation.
  # Parameters:
  #  mthlyMortgagePmt: float - monthly mortgage payment. eg: 2500
  #  principal: float - loan amount. eg: 350000
  #  annualInterestRate: float - annual interest rate stated as %. eg: enter 5 if Annual interest rate is 5%
  #  years: int - loan term in years. eg: 5
  #  #  annualPropTax: float - monthly property tax. eg: 500
  # Output: no return value. This function either call the printMortgageStatement() or exit the menu
  while True:
    ans = input(
  
        "\nChoose the following options to print out your statement:\n1. Print Statement \n2. PrintStatement "
        "and Send email\n3. Exit\n")

    # Invalid input handling: if user doesn't enter 1, 2 or 3, the program print out warning
    if ans != "1" and ans != "2" and ans != "3":  # invalid input
      print("Invalid input! Please enter 1, 2 or 3 only! Try again. ")
      continue
    # If user enters valid input, the following if statements will print out the statement and/or send
    # the statement to email.
    elif ans == "1":
      printMortgageStatement(mthlyMortgagePmt,principal, annualInterestRate, years, annualPropTax, closingCost)
      continue

    elif ans == "2":
      emailAdd = input("Please enter your email address: ")
      #Assummsing there is a code that actually sends the statement to the input email address
      print("\nThe statement was sent to ", emailAdd)
      printMortgageStatement(mthlyMortgagePmt, principal, annualInterestRate, years, annualPropTax, closingCost)
      continue

    elif ans == "3":
      break


def printMortgageStatement(mthlyMortgagePmt,principal, annualInterestRate, years, annualPropTax,                                  closingCost):
  # Function: this function that output the Mortgage statement including monthly Mortgage payment, the loan amount
  # /principal, the annual interest rate, the monthly property tax, and closing cost
  # Parameters:
  #  mthlyMortgagePmt: float - monthly mortgage payment. eg: 2500
  #  principal: float - loan amount. eg: 350000
  #  annualInterestRate: float - annual interest rate stated as %. eg: enter 5 if Annual interest rate is 5%
  #  years: int - loan term in years. eg: 5
  #  annualPropTax: float - monthly property tax. eg: 500
  # Output: no return value, just print()

  print()
  print("MONTHLY MORTGAGE STATEMENT")
  print("Principal amount: ", lc.currency(principal, grouping=True))
  print("Interest Rate (%): ", round(annualInterestRate,2))
  print("Term (years):", years)
  print("Closing Cost: ", lc.currency(closingCost,grouping=True))
  print("Monthly Property tax:", lc.currency(annualPropTax, grouping=True))
  print("Monthly Mortgage Payment: ", lc.currency(mthlyMortgagePmt, grouping=True))