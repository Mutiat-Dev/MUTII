import json


def load_file():
    try:
        with open("expenses.json", "r") as file:
            exp = json.load(file)
            return exp
    except FileNotFoundError:
        return []

def update_file(expenses):
    with open("expenses.json", "w")as file:
        json.dump(expenses, file, indent=3)
    
# expenses = [
    # {
    #     "amount": 2900,
    #     "category": "Food",
    #     "description": "Breakfast"
    # },
    # # print(expenses["amount"])
    # {
    #     "amount": 3500,
    #     "category": "Food",
    #     "description": "Dinner"
    # },
    # {
    #     "amount": 7000,
    #     "category": "Transport",
    #     "description": "Taxi"
    # },
    # {
    #     "amount": 1200,
    #     "category": "Miscellaneous",
    #     "description": "Cake&Chips"
    # }

# ]


def add_expense(expenses):
    amount = int(input("Expense Amount: "))
    category = input("Expense Category: Housing | Food | Transport | Internet | Miscellaneous" "\n")
    description = input("Expense Description: ")

    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }
    expenses.append(expense)
    update_file(expenses)


# def view_expense(expenses):
#     for expense in expenses:
#         print(expense["category"], "|",  expense["description"], "|",  expense["amount"])

def view_expense(expenses):
    if not expenses:
        print("No expense yet")
        return

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}.{expense["category"]} | {expense["description"]} | {expense["amount"]}")



def calc_expenses(expenses):
    total_spending = 0

    for expense in expenses:
        total_spending = total_spending + expense["amount"]

    return total_spending



def spend_category(expenses):
    category_totals = {}

    for expense in expenses:
        if expense["category"] in category_totals:
            category_totals[expense["category"]] = category_totals[expense["category"]] + expense["amount"]
        else:
            category_totals[expense["category"]] = expense["amount"]

    return category_totals


def delete(expenses):
    view_expense(expenses)
    choice = int(input("which expense would you like to remove, pick a number: "))

    if 1 <= choice <= len(expenses):
        choice = choice - 1
        del expenses[choice]
    else:
        print("Invalid Input")

    # print(expenses)
    update_file(expenses)
expenses = load_file()

# print(expenses)


while True:
    print("========EXPENSE TRACKER========")
    print("1. Add an expense")
    print("2. View all expenses")
    print("3. Calculate total spending")
    print("4. Calculate spending by category")
    print("5. Delete an expense")
    print("6. Save and Exit")

    choice = input("Choose an option: ")
    if choice == "1":

            try:
                add_expense(expenses)
            except ValueError:
                print("Enter a valid option")
            print() 
    elif choice == "2":
        view_expense(expenses)
        print()
    elif choice == "3":
        total = calc_expenses(expenses)
        print(f"Total Expense:",total)
        print()
    elif choice == "4":
        print(spend_category(expenses))
        print()
    elif choice == "5":
        delete(expenses)
        print()
    elif choice == "6":
        update_file(expenses)
        break
    else:
        print("Choose a valid option")
        print()
