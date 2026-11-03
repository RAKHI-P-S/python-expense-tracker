print("******* EXPENSE TRACKER *******")
expenses=[]

while True:
    name=input("Enter the expense name( or enter done): ").strip()
    
    if name.lower()=="done":
        break 

    try:
        amount=float(input(f"enter the amount : "))

        if amount<=0:
            print("Amount must be grater than 0")
            continue
    except ValueError:
        print("Please enter a valuable input =") 
        continue
    
    expenses.append({"name":name,"amount":amount})  
    print("expenses added.....!")

print("\n--- Expense Summary ---")
total=0

for expens in expenses:
    print(f"{expens['name']} :{expens['amount']:.2f}")
    total+=expens['amount']

print(f"Total spent: ₹{total:.2f}")
