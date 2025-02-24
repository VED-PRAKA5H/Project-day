#if the bill was $150.00 ,split between 5 people ,with 12% tip each pearson should pay, round upto two decimal places

print("Welcome to the tip calculator!")
bill= flaot(input("what was the bill?\n$"))
tip=int(input("How much percentage tip would you like to give? 10 ,12, 15 or 20\n"))
people=int(input("how many people to split the bill?\n"))
total_bill= bill + bill*tip/100

final_amount=round(total_bill/people,2)

#round() function can not round 1.2 to 1.20 or 1.200
#so we use format specifier function , format() using "{:.2f}"
final_amount + "{:.2f}".format(total_amount/people)

print(f"each person should pay :${final_amount}")
