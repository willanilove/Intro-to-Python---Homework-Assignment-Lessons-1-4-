# Create a budget calculator using a function that tracks income and expenses.

def calculate_budget():

    income = float(input("Enter your monthly income: $"))
    rent = float(input("Enter rent expense: $"))
    food = float(input("Enter food expense: $"))
    entertainment = float(input("Enter entertainment expense: $"))

    total_expenses = rent + food + entertainment
    remaining_money = income - total_expenses

    if remaining_money < 0:
        advice = "You're overspending! Cut back on expenses."
    elif remaining_money < 100:
        advice = "Your budget is tight. Be careful with spending."
    else:
        advice = "Great job! You have money left over."

    print("\n=== BUDGET SUMMARY ===")
    print(f"Monthly Income: ${income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Remaining Money: ${remaining_money:.2f}")
    print(f"\nBudget Advice: {advice}")

calculate_budget()