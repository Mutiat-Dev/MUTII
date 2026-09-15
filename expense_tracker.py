expenses = [
    {
        "amount": 2900,
        "category": "Food",
        "description": "Breakfast"
    },
    # print(expenses["amount"])
    {
        "amount": 3500,
        "category": "Food",
        "description": "Dinner"
    },
    {
        "amount": 7000,
        "category": "Transport",
        "description": "Taxi"
    },
    {
        "amount": 1200,
        "category": "Miscellaneous",
        "description": "Cake&Chips"
    }

]

def calc_expenses(expenses):
    total_spending = 0
    for expense in expenses:
        total_spending = total_spending + expense["amount"]
    return total_spending

total = calc_expenses(expenses)
print(total)  
# print(expenses[0]["amount"])
# x = expenses[0]["amount"]
# y = expenses[1]["amount"]
# z = expenses[2]["amount"]

# total_spending = x + y + z

# print(expenses["amount"])
def spend_category(expenses):
    category_totals = {}

    for expense in expenses:
        if expense["category"] in category_totals:
         category_totals[expense["category"]] = category_totals[expense["category"]] + expense["amount"]
        else:
           category_totals[expense["category"]] = expense["amount"]
    return category_totals

print(spend_category(expenses))

# print(expenses)
def view_expense(expenses):
   for expense in expenses:
      print(expense["category"], expense["description"], expense["amount"])

view_expense(expenses)


def delete(expenses):
    # del expenses[2]
    print(expenses)
    choice = int(input("What do you want to remove? "))

    if len(expenses) > 0 <= 4 :
       del expenses[choice]
    else:
       print("Invalid Input")

    choice = choice - 1
    print(expenses)

delete(expenses)

# # with open("expenses.txt") as file:
#     ...
