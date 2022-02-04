# ******************************************************************************
# Author: Khanh Vu
# Lab: Lab 4
# Date: 02.01.2022
# Module Description: This module has a function that calculate closing cost that charges to home buyers.  
# According to Quicken loan, Closing cost comprises of three main costs: Property-related cost, 
# Loan-origination-related cost, and Other insurance-related cost. Each will have a detailed list of cost components.  
# However, as a team, we decided to do a simple version of closing cost, which is 3%-6% of the home value. 
# I will not include all of these costs in the calculation for simplicity. 
# Sources: https://www.quickenloans.com/learn/closing-costs
#          Amanda: https://www.investopedia.com/mortgage/mortgage-guide/closing-costs/

# ******************************************************************************


def calculateClosingCost (p):
  # Function: Closing Cost Calculation. The function calculates the closing cost charges to home buyers.
  # Arguments: the loan amount(principal amount)
  # Outputs: float closingCost
  
  costAsPercentage = 0.03      # I assume the closing cost is 3% of the loan amount
  closingCost = round (p * costAsPercentage, 2)
  return closingCost 
  






