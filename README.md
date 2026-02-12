# 💰 Expense Tracker (Python + Pandas)

A simple Command-Line Expense Tracker built using Python and Pandas.
This project stores expense data in a CSV file and allows users to manage and analyze their daily expenses.

---

## 🚀 Features

- ✅ Add Expense
- 📄 View All Expenses
- 🔍 Filter by Category
- 💸 Calculate Total Expense
- 📅 Monthly Expense Summary
- 📂 Automatically creates CSV file if not exists

---

## 🛠 Technologies Used

- Python
- Pandas
- datetime module
- os module

---



## ▶️ How to Run

1. Install Python (3.x)
2. Install pandas:

```
pip install pandas
```

3. Run the program:

```
Expense-Tracker.py
```

---

## 📌 How It Works

- Expenses are stored in a CSV file (`expenses.csv`)
- Data is handled using Pandas DataFrame
- Monthly summary is calculated using:
  
```
df.groupby("Month")["Amount"].sum()
```

- Date is converted using:

```
pd.to_datetime()
```

---

## 📷 Sample Menu

```
========Expense Tracker==============
1. Add Expense
2. View Expenses
3. Category Wise Filter
4. Total Expense
5. Monthly Summary
6. Exit
```

---

## 🎯 Learning Concepts Used

- File Handling
- Pandas DataFrame
- groupby()
- datetime formatting
- CSV operations
- Functions in Python
- CLI menu using while loop

---

## 📈 Future Improvements

- Add graphical dashboard
- Add edit/delete expense option
- Add budget tracking
- Export monthly report as PDF

---

## 👩‍💻 Author


Tanvi  
BCA (AI & Data Science) Student  
Learning Python, AI, ML & Data Science

---

⭐ If you like this project, give it a star!

