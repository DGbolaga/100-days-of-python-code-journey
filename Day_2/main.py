############# Topic: Understanding data types and how to manipulate strings ########
# Day 2 project: Tip Calculator

print("Welcome to the tip calculator!\n") 

total_bill = float(input("What was the total bill? $"))
tip_percent = input("How much tip would you like to give (percentage)? 10, 12, or 15? ")
num_of_people = input("How many people to split the bill? ")


tip_amount = (tip_percent / 100) * total_bill
total_amount = tip_amount + total_bill
amount_per_person = round((total_amount / num_of_people), 2)

print(f"Each person should pay: ${amount_per_person}")

