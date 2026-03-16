💰 Expense Tracker CLI (Python)

A simple Command Line Expense Tracker built using Python that helps users manage their income and expenses efficiently. The application allows users to record financial transactions, generate monthly summaries, export reports, and visualize expense distribution through charts.

This project demonstrates the use of Python for data handling, analysis, and visualization using libraries such as Pandas and Matplotlib.

📌 Features
- ➕ Add income or expense entries
- 📅 Track transactions with date, category, and amount
- 📊 View monthly financial summary
- 📁 Export reports in CSV and Excel formats
- 📈 Generate expense distribution charts
- 🖥 Simple and interactive Command Line Interface (CLI)

🛠 Technologies Used
- Python
- Pandas
- Matplotlib
- CSV Module
- Datetime Module

📂 Project Structure
Expense-Tracker-CLI/
│
├── expense_tracker.py
├── expenses.csv
├── README.md

⚙️ Installation

1️⃣ Clone the Repository
- git clone https://github.com/your-username/expense-tracker-cli.git

2️⃣ Navigate to the Project Folder
- cd expense-tracker-cli

3️⃣ Install Required Libraries
- pip install pandas matplotlib

▶️ How to Run the Project
*Run the following command in the terminal:
- python expense_tracker.py
- You will see the CLI menu:

===== Expense Tracker CLI =====
1. Add Entry
2. Monthly Summary
3. Export Monthly Report
4. Export Expense Chart
5. Exit

📊 Functionality

1️⃣ Add Entry
1. Allows users to add a new income or expense record including:
2. Date
3. Type (income/expense)
4. Category
5. Amount

2️⃣ Monthly Summary
Displays:
- Total Income
- Total Expense
- Savings for the selected month.

3️⃣ Export Monthly Report
- Exports the monthly data into:
1. CSV file
2. Excel file

*Example output files:
- 2026-03_report.csv
- 2026-03_report.xlsx

4️⃣ Export Expense Chart
- Generates a pie chart showing expense distribution by category and saves it as:

- 2026-03_expense_chart.png
📁 Data Storage

- All financial records are stored in a CSV file:
-- expenses.csv

- Example format:

- date	type	category	amount
- 2026-03-10	expense	Food	250
- 2026-03-11	income	Salary	50000

💡 Skills Demonstrated
1. This project demonstrates:
2. Python CLI application development
3. File handling using CSV
4. Data analysis using Pandas
5. Data visualization using Matplotlib
6. Error handling and input validation
7. Working with dates and financial data

🚀 Future Improvements
- Possible improvements for this project:
- Add SQLite database support
- Create a GUI version using Tkinter or Streamlit
- Add budget tracking
- Add yearly analytics dashboard
- Add category-wise expense reports

👨‍💻 Author : Vikram Singh Kushwaha - Aspiring Data Scientist | Python Developer
