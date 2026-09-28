# Bill calculator

bill = float(input("How much was your bill? $"))
choice= input("How was your service? ") 
print(choice)
if choice == "1":
        tip_percent= 0.00
elif choice== "2":
   tip_percent= 0.10
elif choice== "3":
     tip_percent= 0.15
elif choice== "4":
    tip_percent= 0.20
else:
    tip_percent = 0.15
    print("Invalid choice. Defaulting to 15%.")
    tip_perfect= 0.15
print(f"Total: ${tip_percent:.2f}")
