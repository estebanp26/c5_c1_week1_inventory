#Primero se pide la informacion del usuario
person_name = input ("Insert name: ")
product = input ("Insert product: ")
unit_price = float(input ("Insert unit price: "))
quantity = int(input ("Insert quantity: "))


if unit_price <=0:
    print("Invalid value, the price cannot be negative, please try again.")
else:
    print("Purchase completed successfully.")
#Then the total amount to pay is calculated.
total_price = unit_price * quantity
#Finally we print the total price to the user
print("The total price to pay is: ", total_price)
