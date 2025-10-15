"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Get incomes over a given number of number_of_months."""
    incomes = []
    number_of_months = int(input("How many numbers_of_months? "))

    for month in range(1, number_of_months + 1):
        income = float(input("Enter income for month " + str(month) + ": "))
        incomes.append(income)

    calculate_income(incomes, number_of_months)

def calculate_income(incomes, number_of_months):
    """Display report"""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, number_of_months + 1):
        income = incomes[month - 1]
        total += income
        print_report(income, month, total)

def print_report(income, month, total):
    print(f"Month {month:2} - Income: ${income:10.2f}       Total: ${total:10.2f}")

main()
