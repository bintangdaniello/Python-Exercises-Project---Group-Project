# Personal Budget Tracker
# This program helps a user track their monthly expenses
# and compares their spending to a monthly budget.

def main():  # usage
    print("=== Personal Budget Tracker ===")

    # Ask the user for their monthly budget
    budget = float(input("Enter your monthly budget: $"))

    # Ask how many expenses they want to enter
    num_expenses = int(input("How many expenses do you want to enter? "))

    # Create an empty list to store the expense amounts
    expenses = []

    # Use a loop to collect each expense from the user
    for i in range(1, num_expenses + 1):
        amount = float(input(f"Enter amount for expense #{i}: $"))
        expenses.append(amount)

    # If no expenses were entered, handle that case
    if len(expenses) == 0:
        print("\nNo expenses entered. Nothing to calculate.")
        return

    # Calculate total, average, and highest expense
    total_spent = sum(expenses)
    average_expense = total_spent / len(expenses)
    highest_expense = max(expenses)

    # Display a summary of the spending
    print("\n=== Spending Summary ===")
    print(f"Number of expenses: {len(expenses)}")
    print(f"Total spent:        ${total_spent:.2f}")
    print(f"Average expense:    ${average_expense:.2f}")
    print(f"Highest expense:    ${highest_expense:.2f}")

    # Compare total spending to the budget
    print("\n=== Budget Comparison ===")
    if total_spent < budget:
        amount_under = budget - total_spent
        print(f"You are under budget by ${amount_under:.2f}. Nice job!")
    elif total_spent == budget:
        print("You spent exactly your budget.")
    else:
        amount_over = total_spent - budget
        print(f"Warning: you are over budget by ${amount_over:.2f}.")

# Call the main function to run the program
if __name__ == "__main__":
    main()