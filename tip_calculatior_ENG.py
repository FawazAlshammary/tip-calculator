print("Welcome to the tip calculator! ")
bill = float(input("What was the total bill ? $ "))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
persons = int(input("How many people to split the bill? "))
Calc_tip = tip / 100
Total_Calc_tip = bill * Calc_tip
Calc_Bill_tip = (bill + Total_Calc_tip ) /  persons
final_Bill = round(Calc_Bill_tip, 2)
print(f"Each person should pay: ${final_Bill} ")


