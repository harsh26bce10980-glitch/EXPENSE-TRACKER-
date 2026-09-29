"""
Expense Tracker - Python Console Application
Submitted by: Harsh Godara (Reg. No. 26BCE10980)

A command-line application for recording, analyzing, and monitoring
personal expenses. Data is persisted locally in expense.txt using
'|' as the field delimiter (name|amount|category).
"""

import os

DATA_FILE = "expense.txt"
DELIMITER = "|"

expenses = []          # list of dicts: {"name": str, "amount": float, "category": str}
monthly_budget = None  # session-only, per report's stated limitation


# ---------------------------------------------------------------------
# File handling
# ---------------------------------------------------------------------
def load_expenses():
    """Load expenses from expense.txt into memory, if the file exists."""
    if not os.path.exists(DATA_FILE):
        return

    try:
        with open(DATA_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(DELIMITER)
                if len(parts) != 3:
                    continue  # skip malformed lines instead of crashing
                name, amount, category = parts
                try:
                    expenses.append({
                        "name": name,
                        "amount": float(amount),
                        "category": category
                    })
                except ValueError:
                    continue  # skip lines with a corrupted amount field
        print(f"Loaded {len(expenses)} expense(s) from {DATA_FILE}.")
    except OSError as e:
        print(f"Could not read {DATA_FILE}: {e}")


def save_expenses():
    """Write all in-memory expenses back to expense.txt."""
    try:
        with open(DATA_FILE, "w") as f:
            for exp in expenses:
                f.write(f"{exp['name']}{DELIMITER}{exp['amount']}{DELIMITER}{exp['category']}\n")
    except OSError as e:
        print(f"Could not save to {DATA_FILE}: {e}")


# ---------------------------------------------------------------------
# Core operations
# ---------------------------------------------------------------------
def add_expense():
    name = input("Enter expense name: ").strip()
    if not name:
        print("Expense name cannot be empty.")
        return

    try:
        amount = float(input("Enter amount: ").strip())
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return

    if amount <= 0:
        print("Amount must be greater than zero.")
        return

    category = input("Enter category: ").strip()
    if not category:
        print("Category cannot be empty.")
        return

    expenses.append({"name": name, "amount": amount, "category": category.upper()})
    save_expenses()
    print("Expense added successfully!")


def view_expenses():
    print("\n----------- ALL EXPENSES -----------")
    if not expenses:
        print("No expenses recorded yet.")
    else:
        for i, exp in enumerate(expenses, start=1):
            print(f"{i}. {exp['name']} | ₹{exp['amount']} | {exp['category']}")
    print("-------------------------------------")


def calculate_total():
    total = sum(exp["amount"] for exp in expenses)
    print(f"\nTotal Spending: ₹{total}")
    return total


def category_wise_spending():
    totals = {}
    for exp in expenses:
        totals[exp["category"]] = totals.get(exp["category"], 0) + exp["amount"]

    print("\n------ CATEGORY-WISE SPENDING ------")
    if not totals:
        print("No expenses recorded yet.")
    else:
        for category, amount in totals.items():
            print(f"{category} : ₹{amount}")
    print("-------------------------------------")


def highest_expense():
    print("\n---------- HIGHEST EXPENSE ----------")
    if not expenses:
        print("No expenses recorded yet.")
        return
    top = max(expenses, key=lambda e: e["amount"])
    print(f"Expense Name : {top['name']}")
    print(f"Amount       : ₹{top['amount']}")
    print(f"Category     : {top['category']}")
    print("--------------------------------------")


def set_monthly_budget():
    global monthly_budget
    try:
        monthly_budget = float(input("Enter your monthly budget: ").strip())
        if monthly_budget < 0:
            print("Budget cannot be negative.")
            monthly_budget = None
            return
        print("Monthly budget set successfully!")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")


def view_budget_status():
    print("\n----------- BUDGET STATUS -----------")
    if monthly_budget is None:
        print("Please set your budget first.")
        return
    total_spending = sum(exp["amount"] for exp in expenses)
    remaining = monthly_budget - total_spending
    print(f"Monthly Budget   : {monthly_budget}")
    print(f"Total Spending   : {total_spending}")
    print(f"Remaining amount : ₹{remaining}")
    print("--------------------------------------")


# ---------------------------------------------------------------------
# Menu / main loop
# ---------------------------------------------------------------------
MENU = """
========== EXPENSE TRACKER ==========
1. Add Expense
2. View All Expenses
3. View Total Spending
4. View Category-wise Spending
5. View Highest Expense
6. Set Monthly Budget
7. View Budget Status
8. Exit
======================================"""


def main():
    load_expenses()

    while True:
        print(MENU)
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            calculate_total()
        elif choice == "4":
            category_wise_spending()
        elif choice == "5":
            highest_expense()
        elif choice == "6":
            set_monthly_budget()
        elif choice == "7":
            view_budget_status()
        elif choice == "8":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")


if __name__ == "__main__":
    main()
