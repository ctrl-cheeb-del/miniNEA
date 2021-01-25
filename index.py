from datetime import date
from time import time
print(" ")
print(" ")
f = open('dragon.txt', 'r')
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

print("Adult tickets:")
print(" ")

def validate():
    not_validated = True
    while not_validated:
        try:
            print("How many tickets are required:")
            print(" ")
            required_adult = int(input())
            not_validated = False
        except ValueError:
            print(" ")
            print("You must enter a number:")
            print(" ")

validate() 

print(" ")
print("Child tickets:")
print(" ")

validate()

