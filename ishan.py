import time
import os 
from datetime import datetime

def close():
	os.system('cls' if os.name=='nt' else 'clear')
	print("Sorry, our booking times are over")

def close2():
	time.sleep(4)
	os.system('cls' if os.name=='nt' else 'clear')
	welcome()

def catch_error_yn():
	unvalid = True
	while unvalid:
		try:
			response = input()
			if response not in ['Yes', 'No'] :
				raise ValueError()
			return response
		except ValueError:
			print("please only enter 'Yes' or 'No' with capitals on Y or N:")
	
def catch_error_str():
    unvalid = True
    while unvalid:
      try:            
        string = str(input())
        if not string.isalpha():
            raise ValueError
        unvalid = False
        return string
      except ValueError:
        print("You must only enter letters")

def catch_error_int():
	unvalid = True
	while unvalid:
		try:
			number = int(input())
			unvalid = False
			return number
		except ValueError:
			print("You must enter a number:")

def ticket():
	collect_money()
	last_name = surname()
	print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
	print("  Ticket for the lead booker", last_name)
	print("  This ticket allows entry to:")
	print("","",   child_total, "children")
	print("","",   adult_total, "adults")   
	print("","",   senior_total, "seniors")  
	print("")
	print("","",   wristband, "wristbands have been purchased"    )
	print("","", "The current time is", datetime.now().strftime('%H:%M'))
	print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")	
	carpark()

def collect_money(): 
	payment = total_prices()	
	print("\nYour entrance fee will cost a total of £", payment)
	print("We only accept £10 and £20 notes")	
	payed = 0
	while payed<payment:
		print("\nYou have currently paid a total of £" , payed)
		print("How many £10 notes would you like to spend?")
		ten_pounds = catch_error_int()*10
		print("How many £20 notes would you like to spend?")
		twenty_pounds = catch_error_int()*20
		payed = payed + twenty_pounds + ten_pounds

	print ("your change is £", payed - payment)
				
def print_car_park():
	print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
	print("  Parking ticket for one car")
	print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
	bye()
	time.sleep(5)

def entrance():
	print("\nhow many child tickets do you want?")
	global child_total
	child_total = catch_error_int()
	print("\nhow many adult tickets do you want?")
	global adult_total
	adult_total = catch_error_int()
	print("\nhow many senior tickets do you want?")
	global senior_total
	senior_total = catch_error_int()
	total_ticket_price = (child_total*12) + (adult_total*20) + (senior_total*11)
	return total_ticket_price

def total_prices():
	ticket_price = entrance()
	wrist_band_price = wristbands()*20
	total_price = ticket_price + wrist_band_price
	return total_price

def wristbands():
	print("\nHow many wristbands would you like, each one is £20.")
	global wristband 
	wristband = catch_error_int()
	return wristband

def surname ():
	print("\nWhat is the surname of the lead booker ")
	last_name = catch_error_str()
	return last_name

def carpark():
	print("Do you want a free parking space, please answer 'Yes' or 'No' with capital letters on Y or N")
	response = catch_error_yn()
	if response == "Yes":
		print_car_park()
	else:
		print("Ok")
		bye()

def welcome():
	print("Welcome to Copington Adventure Theme Park's automated ticket system\nplease press any button to see the ticket prices.")
	enter = input()
	print("\nAdult tickets are £20 each \nChild tickets are £12 each \nSenior citizen tickets are £11 each")
	ticket()

def bye():
	print("\nThank you for coming to Copington Adventure Park")
	print("We hope you enjoy your stay")
	bye_for_today()


def bye_for_today():
	if time.localtime().tm_hour >= 20:
		time.sleep(4)
		close()
				
	else:
		close2()
		

welcome()
