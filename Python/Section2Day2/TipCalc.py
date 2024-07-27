## Tip Calculator
total = int(input("How much was your bill?"))
#print(type(total))
tip_percent = int(input("How much tip would you like to give? 10, 12, 15"))

number_of_people = int(input("How many people to split the bill"))


#pay = int(((total * tip_percent) + total) / number_of_people)
#multiply the total buy the tip% add 
#pay = ((total * (tip_percent / 100)) + total) / number_of_people
tip_amount = total * (tip_percent / 100)
total_with_tip = total + tip_amount
pay = total_with_tip / number_of_people

print(pay)

