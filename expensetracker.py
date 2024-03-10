import json
import os

# Function to load existing data from file
def load_data(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            return json.load(file)
    else:
        return {'income': 0, 'expenses': []}

# Function to save data to file
def save_data(data, file_name):
    with open(file_name, 'w') as file:
        json.dump(data, file)

# Function to add income
def add_income(data):
    income = float(input("Enter income amount: "))
    data['income'] += income
    print(f"Income of ${income} added successfully.")

# Function to add expense
def add_expense(data):
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    data['expenses'].append({'category': category, 'amount': amount})
    print(f"Expense of ${amount} added successfully.")

# Function to calculate remaining budget
def calculate_budget(data):
    total_expenses = sum(expense['amount'] for expense in data['expenses'])
    remaining_budget = data['income'] - total_expenses
    return remaining_budget

# Function to analyze expenses
def analyze_expenses(data):
    categories = {}
    for expense in data['expenses']:
        category = expense['category']
        amount = expense['amount']
        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount
    print("Expense Analysis:")
    for category, amount in categories.items():
        print(f"{category}: ${amount}")

# Main function
def main():
    file_name = 'budget_data.json'
    data = load_data(file_name)

    while True:
        print("\n===== Budget Tracker =====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Calculate Remaining Budget")
        print("4. Analyze Expenses")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_income(data)
        elif choice == '2':
            add_expense(data)
        elif choice == '3':
            remaining_budget = calculate_budget(data)
            print(f"Remaining Budget: ${remaining_budget}")
        elif choice == '4':
            analyze_expenses(data)
        elif choice == '5':
            save_data(data, file_name)
            print("Budget data saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
