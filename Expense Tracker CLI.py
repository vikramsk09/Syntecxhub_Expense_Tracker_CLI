import csv
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

FILE_NAME = "expenses.csv"


# Ensure CSV file exists
def initialize_file():
    try:
        with open(FILE_NAME, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["date", "type", "category", "amount"])
    except FileExistsError:
        pass


# Add income/expense entry
def add_entry():
    print("\n--- Add New Entry ---")

    entry_type = input("Type (income/expense): ").lower()

    if entry_type not in ["income", "expense"]:
        print("Invalid type!")
        return

    date = input("Enter date (YYYY-MM-DD): ")

    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format!")
        return

    category = input("Enter category: ")

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Amount must be a number!")
        return

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, entry_type, category, amount])

    print("Entry added successfully!")


# Monthly summary
def monthly_summary():
    print("\n--- Monthly Summary ---")

    month = input("Enter month (YYYY-MM): ")

    df = pd.read_csv(FILE_NAME)

    df["date"] = pd.to_datetime(df["date"])

    monthly_data = df[df["date"].dt.strftime("%Y-%m") == month]

    if monthly_data.empty:
        print("No data found for this month.")
        return

    income = monthly_data[monthly_data["type"] == "income"]["amount"].sum()
    expense = monthly_data[monthly_data["type"] == "expense"]["amount"].sum()

    print(f"Total Income : {income}")
    print(f"Total Expense: {expense}")
    print(f"Savings      : {income - expense}")


# Export monthly report
def export_report():
    print("\n--- Export Monthly Report ---")

    month = input("Enter month (YYYY-MM): ")

    df = pd.read_csv(FILE_NAME)
    df["date"] = pd.to_datetime(df["date"])

    monthly_data = df[df["date"].dt.strftime("%Y-%m") == month]

    if monthly_data.empty:
        print("No data found.")
        return

    csv_name = f"{month}_report.csv"
    excel_name = f"{month}_report.xlsx"

    monthly_data.to_csv(csv_name, index=False)
    monthly_data.to_excel(excel_name, index=False)

    print(f"Report exported to {csv_name} and {excel_name}")


# Export chart
def export_chart():
    print("\n--- Export Expense Chart ---")

    month = input("Enter month (YYYY-MM): ")

    df = pd.read_csv(FILE_NAME)
    df["date"] = pd.to_datetime(df["date"])

    monthly_data = df[df["date"].dt.strftime("%Y-%m") == month]

    expense_data = monthly_data[monthly_data["type"] == "expense"]

    if expense_data.empty:
        print("No expense data for this month.")
        return

    category_sum = expense_data.groupby("category")["amount"].sum()

    category_sum.plot(kind="pie", autopct="%1.1f%%")

    plt.title(f"Expenses by Category ({month})")

    chart_name = f"{month}_expense_chart.png"

    plt.savefig(chart_name)
    plt.close()

    print(f"Chart saved as {chart_name}")


# Main CLI menu
def main():
    initialize_file()

    while True:
        print("\n===== Expense Tracker CLI =====")
        print("1. Add Entry")
        print("2. Monthly Summary")
        print("3. Export Monthly Report")
        print("4. Export Expense Chart")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_entry()

        elif choice == "2":
            monthly_summary()

        elif choice == "3":
            export_report()

        elif choice == "4":
            export_chart()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
