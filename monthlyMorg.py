#***********************************************************************
#Amanda Stein
#Lab 4, 133y  
#Date: 01.31.2022, 02.1.2022, 02.03.2022
#Inputs:principal(p), Inerest rate(r),years of loan (n), and tax.
#output: No output, returns the value
#Scource:https://www.businessinsider.com
#Bug testing all.
#***********************************************************************
#Defining the input statements
def monthlyInput():
  while True: 
    try: 
      p=float(input('Enter your principal: '))
      r=float(input('Enter your interest rate as a percent: '))
      n=int(input('Enter how many years your loan is: '))
      tax=float(input('Enter your yearly county property tax: '))
      return p, r, n, tax
    except ValueError:
        print("Please Enter valid input: ")
    
def monthlyPayment():
#pass the values to monthlyPayment 
  p,r, n, tax= monthlyInput()
  rate=r/100  
  rate= rate / 12
  numOfMonths=n*12
  tax= round(tax / 12) 
  # calculating the monthly payment and including tax.
  homeValue=(rate*p*((1+rate)**numOfMonths))/(((1+rate)**numOfMonths)-1) 
  homeValue=round (homeValue + tax, 2)
  #print(monthly) Unhashed during first run to check.
  # return the value for imports to other fucntions.
  return homeValue,p,r,n,tax
