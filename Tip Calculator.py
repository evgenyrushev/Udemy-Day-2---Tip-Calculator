#If the bill was $150.00, split between 5 people, with 12% tip.
print("Welcome to the tip calculator.")

total_bill = input("What was the total bill? $")
tip_given = input("What percentage tip would you like to give? ")
people_tip = input("How many people to split the bill? ")

final_bill = float(total_bill)
final_percentage_of_tip = int(tip_given)
people_tipping = int(people_tip)

amount_without_tip = round((final_bill / people_tipping), 2)

tipping_per_person = round((((final_bill * final_percentage_of_tip) / 100) / people_tipping), 2)

final = round((tipping_per_person + amount_without_tip), 2)
print(f"Each person should pay: ${final}")
