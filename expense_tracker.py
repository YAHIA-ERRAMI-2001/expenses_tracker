
# Expense Tracker - my Level 1 project
import json

print("Welcome YAHIA to Expense Tracker!")
print("Expense Tracker v1!")
try:
    with open("expenses.json", "r") as file:
        expenses = json.load(file)
except FileNotFoundError:
    expenses = []

#Add Expense 

def add_expense(expenses):
    name = input("What did you buy? ")
    amount_str = input("How much did it cost? ")
    category = input("What category? ")
        
    try:
        amount = float(amount_str)
        expense = {"name": name, "amount": amount, "category": category}
        expenses.append(expense)
        print("Expense added successfully!")
            
    except ValueError:
        print("Error: Please enter a valid number for the cost.")


#Show All
def show_all(expenses):

        if len(expenses) == 0:
            print("No expenses to show.")
        else:
            total = 0
            print("\n--- All Expenses ---")
            for item in expenses:
                print(f"Name: {item['name']} | Cost: {item['amount']} | Category: {item['category']}")
                total += item['amount']
            print(f"Total Spent: {total}")

#Total by Category
def show_category_totals(expenses):
    if len(expenses) == 0:
            print("No expenses to show.")
    else:
        category_totals = {}
        print("\n--- Total by Category ---")
        for item in expenses:
            cat = item['category']
            if cat in category_totals:
                category_totals[cat] += item['amount']
            else:
                category_totals[cat] = item['amount']
            
        for cat, total in category_totals.items():
            print(f"Category: {cat} | Total: ${total}")            


#Delete Expense  

def delete_expense(expenses):
    if len(expenses) == 0:
        print("No expenses to delete.")
    else:
        while True:
            print("\n--- Select an Expense to Delete (or 'q' to cancel) ---")
            for i in range(len(expenses)):
                print(f"{i + 1}. Name: {expenses[i]['name']} - Cost: {expenses[i]['amount']}")
                
            user_input = input("Enter the number to delete or 'q' to quit: ")
                
            if user_input.lower() == 'q':
                print("Returning to main menu.")
                break
                    
            try:
                num_to_delete = int(user_input)
                index = num_to_delete - 1
                    
                if 0 <= index < len(expenses):
                    deleted_item = expenses.pop(index)
                    print(f"Deleted: {deleted_item['name']}")
                    break  # Exits the delete loop, goes back to main menu
                else:
                    print("Invalid number. That expense does not exist. Try again.")
            except ValueError:
                    print("Error: Please enter a valid number or 'q'.")

#Quit

def save_and_quit(expenses):
        with open("expenses.json", "w") as file:
            json.dump(expenses, file)
        print("Expenses saved. Goodbye!")
        

while True:
    print("1. Add Expense")
    print("2. Show All")
    print("3. Total by Category")
    print("4. Delete Expense")
    print("5. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense(expenses)
    elif choice == "2":          # Changed to elif
        show_all(expenses)
    elif choice == "3":          # Changed to elif
        show_category_totals(expenses)
    elif choice == "4":          # Changed to elif
        delete_expense(expenses)
    elif choice == "5":          # Changed to elif
        save_and_quit(expenses)
        break                    # The break goes here, in the main loop
    else:
        print("Invalid choice, please try again.")
