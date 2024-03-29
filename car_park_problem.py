from datetime import datetime, timedelta
import math
import re

currency = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 5, 10, 20]

def getUserInput(str1): 
  regexPattern = r"^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$"  #regex pattern for 24 Hour time

  while True:
    if not re.fullmatch(regexPattern, str1):  #Checking the user input to ensure the enter the right time format
      str1 = input('That is not the correct 24hr Format please re enter: ')
    else:    
      break
  return str1
      
arrTime = getUserInput(input('Please enter an arrival time: '))
depTime = getUserInput(input('Please enter a departure time: '))


def totalTime(arr, dep):
        time1 = datetime.strptime(arr, '%H:%M')
        time2 = datetime.strptime(dep, '%H:%M') #converting the string inputs to datetime objects
        
        if time2 > time1:
          diff = time2 - time1
          return (diff.total_seconds()/60)  #Calculate the difference between arrival and departure time
        else:
          time2 = time2 + timedelta(days=1) 
          diff = time2 - time1
          return (diff.total_seconds() /60) #Calculate total seconds inbetween arrival and departure and convert to minutes by dividing by 60

duration = totalTime(arrTime, depTime)

def calculateCost(duration):
  if (duration <= 60):
    return 3
  else:
    return float(((duration - 60) + 300) / 100)

totalCost = calculateCost(duration)

print(f'The total cost of your stay was £{totalCost:.2f}')


def paymentIn():
  payment = 0
  while payment < totalCost:
    inp = input('Please make a payment: ' )
    
    if '£' in inp: 
      counter = float(inp[1:]) #Slicing the string and converting the numerical value of the string to float
      if counter in currency: 
        payment += counter
      else:
        print('That is not a correct denomination please try again')
  
    elif 'p' in inp.lower() :
      counter = float(inp[:-1]) / 100 
      if counter in currency:
        payment += counter
      else:
        print('That is not a correct denomination please try again')

    else:
     print('That is not a correct denomination please try again')

    if (payment == totalCost):
      print('Thank you for your stay, have a safe onward journey')

  global change
  change = payment - totalCost

  if change > 0 :
    print(f'Thank you for your payment you are due £{change:.2f} in change')

paymentIn()

def convertCurrency(arr):
  for i in range(len(arr)): 
    arr[i] = arr[i] * 100 
      
convertCurrency(currency)

def changeGiven(change):
  temp = []
  currency.reverse()

  change *= 100 
  change = int(math.ceil(change))  

  for coin in currency:
    while change >= 0:
        if change >= coin: #compare amount of change, with currency in list
            temp.append(coin) 
            change -= coin 
        else:
            break

  for i in range(len(temp)):
    temp[i] = temp[i] / 100  
    if temp[i] >= 1:
      temp[i] = '£' + str(int(temp[i])) #Formatting temp list for neater output
    else:
      temp[i] = str((int(temp[i]* 100))) + 'p'
    
  return  'The output change is ' + ', '.join(temp)

print(changeGiven(change))
