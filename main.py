# Make Your Own Pizza - Price Calculator - www.101computing.net/build-your-own-pizza-price-calculator/

print("O-O-O-O-O-O-O-O-O-O-O-O")
print("|        BUILD        |")
print("O   YOUR OWN PIZZA    O")
print("|  PRICE CALCULATOR   |")
print("O-O-O-O-O-O-O-O-O-O-O-O")
print("")

# Initialise a variable used to store the price of our pizza
price = 0

print("Order a pizza in 5 easy steps:")

# Step 1 - Pick a size
print("""We have three sizes of pizza:
    - Small (£6)
    - Medium (£8)
    - Large (£10)""")

size = input("Enter the size of your pizza: S, M or L?").upper()
while size not in ["S", "M", "L"]:
   print("Invalid option, please try again!")
   size = input("Enter the size of your pizza: S, M or L?").upper()

if size=="S":
   price = price + 6
elif size=="M":
   price = price + 8
elif size=="L":
   price = price + 10

print("Pizza price so far: £" + str(price))

# Step 2 - Choose a base
print("Choose your base:")
print(" - Classic (+ £0)")
print(" - Thin (+ £1)")
print(" - Deep (+ £2)")

base = input("Enter base (Classic, Thin or deep):").capitalize()

if base == "Classic":
   price = price + 0
elif base == "Thin":
   price = price + 1
elif base == "Deep":
   price = price + 2

   print("Pizza price so far: £" + str(price))


# Step 3 - Decide how many toppings you would like
toppings = int(input("how many extra toppings do you want? (£1.50 each): "))
price = price + (toppings * 1.5)

print("Pizza price so far: £" + str(price))
# Step 4 - Eat in or Takeaway?
eat_in = input("do you want to eat in or takeaway? (Yes = eat in, No =takeaway): ").capitalize()
if eat_in == "Yes":
   price = price + 2
else:
   price = price + 0

print("Pizza price so far: £" + str(price))

# Step 5 - Enter Discount Code
discount = input("Enter the discount code if you have one (otherwise press enter): ")

if discount == "P1ZZ4":
   price = price * 0.8
   print("Discount applied! 20% off.")
elif discount == "Freepizza":

   price = price * 0.8
   print("Discount applied! 20% off.")
#Final Price
print("Total price for your pizza: £" + str(round(price, 2)))