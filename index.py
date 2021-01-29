from datetime import date
from time import time
print(" ")
print(" ")
f = open('swag_dragon.txt', 'r')
content = f.read()
print(content)
f.close()


today = date.today()
print(" ")
print("yo my slimedems welcome to the ticket booth at copington advent park")
print(" ")
print(" ")

def Entrance():
    class Prices:
        adult_ticket = 20
        child_ticket = 12
        senior_ticket = 11
        wristband_all = 20
        carpass = 0

    print("Adult ticket costs: ", Prices.adult_ticket)
    print("Child ticket costs: ", Prices.child_ticket)
    print("Senior ticket costs: ", Prices.senior_ticket)
    print("Wristband costs: ", Prices.wristband_all)
    print("Carpass costs: ", Prices.carpass)
    print(" ")

Entrance()

def validate_str():
    not_validated = True
    while not_validated:
        try:
            print("")
            print(" ")
            answer= str(input())
            not_validated = False
            return answer
        except ValueError:
            print("You must enter a number:")
            print(" ")

def validate_yes():
	not_validated = True
	while not_validated:
		try:
			response = input()
			if response not in ['yes', 'no'] :
				raise ValueError()
			return response
		except ValueError:
			print("please only enter either yes or no")

def validate_num():
    not_validated = True
    while not_validated:
        try:
            print("")
            print(" ")
            answer = int(input())
            not_validated = False
            return answer
        except ValueError:
            print("You must enter a number:")
            print(" ")

def required():
    print("how many child tickets are needed: ")
    global child_required
    child_required = validate_num()
    print("how many adult tickets are needed: ")
    global adult_required
    adult_required = validate_num()
    print("how many senior tickets are needed: ")
    global senior_required
    senior_required = validate_num()
    print("how many wristbands are needed: ")
    global wristband_required
    wristband_required = validate_num()
    total_cost = (child_required*12) + (adult_required*20) + (senior_required*11) + (wristband_required*20)
    return total_cost

def car_park():
    print("would you like a car pass?")
    reply = validate_yes()

def surname():
    print("what is the surname of the person booking?")
    booker_surname = validate_str()
    return booker_surname


def payment():
    cost = required()
    print("DISCLAIMER : we only accept 10 & 20 £ notes")
    print(" ")
    print("the required amount is", cost)
    accepted = 0
    while accepted <= cost:
        print("youve payed" , accepted, "so far")
        print("how many £10 notes will you use?")
        ten_submitted = validate_num()*10
        print("how many £20 notes will you use?")
        twenty_submitted = validate_num()*20
        accepted = accepted + twenty_submitted + ten_submitted
        change = accepted - cost
    print("you have", change, "change")

def final():
    booker_surname = surname()
    print("thank you ", booker_surname, "for booking with us on the", today, "hope to see you again soon!")

payment()
car_park()
final()

