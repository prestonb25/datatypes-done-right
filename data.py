# Bill calculator

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
print(f"Your total is: ${total:.2f}")


""" 
def spaces (n,y,t):
    occupied = 0 
    for i in range(len(y)) 
    if y[i]== "C" and t[i]=="C":
        occupied=occupied +1


    spaces(5,"CC..C",".CC..") """