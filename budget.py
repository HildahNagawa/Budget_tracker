def get_valid_category(): # Ensure only alphabetical input for categories.
    while True:                      # Keep prompting until valid input
        category = input("Add Category: ")
        if category.isalpha(): #check if input contains only alphabetical characters.
            return category 
        else:
            print("Invalid input! Please enter letters only") 

def only_valid_amount(): # Ensure that only positive amount is input
    while True:
        try:
            amount = float(input("Add Amount: "))
            if amount >= 0: #check if the input is greater than or equal to zero
                return amount
            else:
                print("Invalid Amount! Please enter a valid amount greater than 0")
        except ValueError: # Handles non numeric inputs 
            print("Invalid Input! Please enter a valid number")     


def add_income(Balance): #Function to append income amounts
    income_category = get_valid_category()
    income_amount = only_valid_amount()
    income_entries.append({"Category": income_category, "Amount":income_amount})
    Balance += income_amount
    print(f"Income added! Updated Balance:{Balance}")
    return Balance

def add_expense(Balance): #Function to append expense amounts
    expense_category = get_valid_category()
    expense_amount = only_valid_amount()
    expense_entries.append({"Category": expense_category, "Amount": expense_amount})
    Balance -= expense_amount
    print(f"Expense Added! Updated Balance: {Balance}")
    return Balance

def view_summary():
    print(f"\n{"."*5}\nYour Incomes\n{"."*5}")
    for entry in income_entries:
        print(f"Category: {entry['Category']}, Incomes: {entry['Amount']} ")
    print(f"\n{"."*5}\nYour Expenses\n{"."*5}")
    for entry in expense_entries:
        print(f"Category:{entry['Category']}, Amount: {entry['Amount']}")
    print(f"Net Balance: {Balance}")

import json

def save_data():
    with open("budget_data.json", "w") as file:
        json.dump({"Balance": Balance, 
                   "Incomes":income_entries,
                  "Expenses": expense_entries} , file)


def load_data():
    global Balance, income_entries, expense_entries
    
    try:
        with open("budget_data.json", "r") as file:
            data = json.load(file)
            Balance = data["Balance"]
            income_entries = data["Incomes"]
            expense_entries = data["Expenses"]
            print("Data Loaded Successfully")
    except FileNotFoundError:
        print("Error: The file budget.json does not exist! Refreshing")


    
Balance = 0  #initialise balance to zero
income_entries = []
expense_entries = []
load_data()

print("""Welcome To Budget Tracker!
      Enter your Income and Expenses""")
print()
#keep the menu popping with infinite loop.
while True:
    print("Please select an option: ")
    print("1: Add Income")
    print("2: Add Expense")
    print("3: View Summary")
    print("4: Exit")

    choice = input("Enter your option")

    if choice == "1":
        print("Adding Income.....")
        Balance = add_income(Balance)
    elif choice == "2":
        print("Adding Expense....")
        Balance = add_expense(Balance)
    elif choice == "3":
        print("Making your summary")
        view_summary()
    elif choice == "4":
        confirm_exit = input("Are you sure you want to exit? : (y/n)")
        if confirm_exit.lower() == "y":
            print(f"\nExiting\n{"."*5}\nThank you for using Budget Tracker")
            save_data()
            break
    else:
        print("""Error!
          Invalid option, Please Try Again""") 

