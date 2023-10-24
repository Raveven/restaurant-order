import random
import string
from datetime import datetime
import pytz
import os
import time

#Input Lessee Info
name = input('Please input your name: ')
while True:
  phone = input('Please input your phone numer: ')
  if len(phone) == 10:
    break
  else:
    print('Invalid input, phone numbers must be 10 digits.')
os.system("clear")

#Menu
print("\033[1mMenu\033[0m")
print("Angie Burger $10.00\nDeluxe Cheese Burger $9.00\nBYOB $9.00\n\033[1mDrink Menu\033[0m\nPepsi, Diet Pepsi, Sierra Mist\nSmall $1.00\nMedium $1.50\nLarg e$2.00")
#Car Choice Input
burgerchoice = input('Hello, ' + name + ', Would you like the Angie Burger(1), Deluxe Cheese Burger(2), BYOB(3): ')
if '1' in burgerchoice:
  burgerprice = 10
if '2' in burgerchoice:
  burgerprice = 9
if '3' in burgerchoice:
  burgerprice = 9
  byob1 = input('American Cheese(1), Cheddar Cheese (2), Provel Cheese(3), Mushroom(4), Jalapenos(5), or Spinach(6): ')
  byob2 = input('American Cheese(1), Cheddar Cheese (2), Provel Cheese(3), Mushroom(4), Jalapenos(5), or Spinach(6): ')
  byob3 = input('American Cheese(1), Cheddar Cheese (2), Provel Cheese(3), Mushroom(4), Jalapenos(5), or Spinach(6): ')

drinksize = input("What size drink would you like small(1), medium(2), large(3), none(4): ")
if '1' in drinksize:
  drinkprice = 1
  drinkchoice = ("Would you like Pepsi(1), Diet Pepsi(2), or Sierra Mist(3): ")
if '2' in drinksize:
  drinkprice = 1.5
  drinkchoice = ("Would you like Pepsi(1), Diet Pepsi(2), or Sierra Mist(3): ")
if '3' in drinksize:
  drinkprice = 2
  drinkchoice = ("Would you like Pepsi(1), Diet Pepsi(2), or Sierra Mist(3): ")
if '4' in drinksize:
  drinkprice = 0
  drinkchoice = ("Would you like Pepsi(1), Diet Pepsi(2), or Sierra Mist(3): ")

tip = input("How much would you like to add as a tip: ")

#Car Rental Payment
while True:
  ccn = input('Please input your credit card number: ')
  if len(ccn) == 16:
    break
  else:
    print('Invalid input, credit card numbers must be 16 digits.')
while True:
  cvv = input('Please input your CVV: ')
  if len(cvv) == 3:
    break
  else:
    print('Invalid input, CVV must be 3 digits: ')
    
#Car Rental Receipt Title
print('Printing Receipt...')
time.sleep(3)
os.system("clear")
print('\033[1m' + '          ' + 'Burger Reciept\033[0m')
 
#local time
tz_US = pytz.timezone('US/central') 
datetime_US = datetime.now(tz_US)
print("Current Date:", datetime_US.strftime("%m/%d/%Y, %H:%M:%S"))

#Generates Receipt ID
N = 12
res = ''.join(random.choices(string.digits, k=N))
print("Receipt ID: " + str(res))

#Rental Company Info
print('\n\033[1mCompany Info\033[0m')
print("Company: Angie's Burger Truck\nRepresentative: Jacob Hock\nLocation: St. Louis, Missouri\nZIP: 63128\nPhone: 314-347-6077\n")

#Lessee Info
print('\033[1mCustomer Info\033[0m')
print('Lessee Name: ', name)
print('Lessee Phone Number: ', phone)

#Payment Info
print('\n\033[1mPayment Info\033[0m')
print((burgerprice + drinkprice) * 0.043 + burgerprice + drinkprice + tip)
print('\n\033[1mOrder Info\033[0m')
if '1' in burgerchoice:
  print("Burger Choice: Angie Burger")
if '2' in burgerchoice:
  print("Burger Choice: Deluxe Cheese Burger")
if '3' in burgerchoice:
  print("Burger Choice: BYOB")
if '1' in drinkchoice:
  print("Drink Choice: Pepsi")
if '1' in drinkchoice:
  print("Drink Choice: Diet Pepsi")
if '1' in drinkchoice:
  print("Drink Choice: Sierra Mist")

#Thanks and credits
print('\n\033[1mThank you for the order! Please stop by the location to pick up the burger!\r033[1m')
print('Created by Jacob Hock')
    