
# Command-Line Expense Tracker 💰

A simple yet powerful command-line Expense Tracker built with Python. This application helps users keep track of their daily spending, categorize expenses, and analyze where their money is going.

## 🚀 Features

- **Add Expenses:** Record an expense with a name, cost, and category.
- **Show All:** View a complete list of all recorded expenses along with the grand total.
- **Total by Category:** See exactly how much you have spent in each category (e.g., Food, Transport).
- **Delete Expense:** Safely remove an expense. Includes a loop to prevent crashing on invalid input.
- **Data Persistence:** Automatically saves your data to a local `expenses.json` file and loads it when you restart the program.

## 🛠️ Technologies Used

- **Python 3**
- **JSON** (for data storage)
- **Standard Library** (no external dependencies required)

## 💻 How to Run Locally

1.Make sure you have Python installed on your computer. You can check by running:
   ```bash
   python --version
```
2. Clone this repository:   
git clone https://github.com/your-username/expenses_tracker.git

3. Navigate into the project folder:
cd expenses_tracker


4.Run the application:
python expense_tracker.py

## 🧠 What I Learned Building This
Python Fundamentals: Practiced using lists, dictionaries, and while/for loops.

Functions: Refactored a large script into modular, reusable functions (add_expense, show_all, etc.) to keep the code clean.

Error Handling: Used try/except blocks to prevent the program from crashing when a user types a word instead of a number.

File I/O: Learned how to save and load data using Python's built-in json module.

## 🔮 Future Improvements
Add a feature to edit an existing expense.

Add the ability to filter expenses by date (e.g., this week, this month).

Implement a simple graphical user interface (GUI) using Tkinter.