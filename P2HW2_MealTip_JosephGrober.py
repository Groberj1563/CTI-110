#Tip Calculator
#FEB 15 2019
#CTI-110 P2HW2- Meal Tip Calculator
#Joseph Grober
#






#This program is a Meal Tip Calculator for tip values of 15%, 18% and 20%
Total_Price = float(input(' Enter value of meal for 15% tip: '))

Tip = Total_Price * 0.15

Total_Price = Tip + Total_Price

print( 'The tip ammount is $', format(Tip, ',.2f'))

print( 'The total price including tip is $', format( Total_Price, ',.2f'))
print(" ")


Total_Price = float(input(' Enter value of meal for 18% tip: '))

Tip = Total_Price * 0.18

Total_Price = Tip + Total_Price

print( 'The tip ammount is $', format(Tip, ',.2f'))

print( 'The total price including tip is $', format( Total_Price, ',.2f'))

print(" ")








Total_Price = float(input(' Enter value of meal for 20% tip: '))

Tip = Total_Price * 0.20

Total_Price = Tip + Total_Price

print( 'The tip ammount is $', format(Tip, ',.2f'))

print( 'The total price including tip is $', format( Total_Price, ',.2f'))
print(" ")




print( "Thank you")
