def suggest_changes(total_expenses, waste_expenses, target, monthly_income):
    savings_needed = target - (monthly_income * 12 - total_expenses)
    print(f"Savings needed to achieve target: {savings_needed}")
    print(f"Reduce waste expenses by: {waste_expenses}")

suggest_changes(total_expenses, waste_expenses, 400000, 70000)
