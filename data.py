""" # Bill calculator

bill = float(input("How much was your bill? $"))
choice = input("How was your service? 1, 2, 3, or 4") 
print(choice)
if choice == "1":
    total = bill * 0.00
elif choice== "2":
    total = bill * 0.10
elif choice== "3":
    total = bill * 0.15
elif choice== "4":
    total = bill * 0.25
else:
    total = bill * 1.15
    print("Invalid choice. Defaulting to 15%.")
    tip_perfect= 0.15
print(f"Your total is: ${total:.2f}") """





#Even or Odd Calculator
def check_odd_even (number):
    if % 2==0:
    return "Even"
else:
Return "Odd"
print(check_odd_even(4))
print(check_odd_even(7))
