import pandas as pd
from datetime import datetime
import os
# Pandas = to manage table data(CSV as DataFrame)
# datetime to get today's date automatically
# os is a built-in Standard library module in python 
# THe os module provides functions to interact with the operating system like files,folders,path,system commands

FILE = "expenses.csv"

#--------Create file if not exists ----------


# os.path.exists(filename) is a function of the os module
#df = pd.DataFrame(columns=["Date","Category","Description","Amount"]) it creates an empty DataFrame with only columns names 
if not os.path.exists(FILE):
    df = pd.DataFrame(columns=["Date","Category","Description","Amount"])
    df.to_csv(FILE, index=False)
    # to_csv() is a pandas function it is used to save a DataFrame into a CSV file
    # Convert table (DataFrame) → into permanent CSV file

#------- ADD EXPENSE---------


# date = datetime.now().strftime("%Y-%m-%d") === datetime.now() it returns the current data time from ur computer and strftime =string format time it converts the date time object into a string in  the format 
# %Y is 4 digit year, %m is month 02 ,%d means day 
# Why double brackets [[ ]] ?
#Outer [ ] → represents list of rows
#Inner [ ] → one single row
# new = pd.DataFrame([[date, category, desc, amount]],
                       #columns=["Date", "Category","Description","Amount"])
    # ➡ Convert user input values into a one-row DataFrame
#   ➡ So it can be added to existing expense table.

# df = pd.concat([df,new],ignore_index=True) ignore_index is a argument of pd.concat() function  
#  pd.concat() function is  used to add the new expense row into the existing dataframe and create one updated dataframe
# ignore_index=True ---creates fresh index numbers means it will add new row 
#The argument ignore_index=True ...resets the index so that the resulting DataFrame has a fresh sequential index after adding the new record




def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter Category (Food/Travel/Shopping/etc):")
    desc = input("Enter Description: ")
    amount = float(input("Enter Amount:"))

    df = pd.read_csv(FILE)
    
    new = pd.DataFrame([[date, category, desc, amount]],
                       columns=["Date", "Category","Description","Amount"])
    df = pd.concat([df,new],ignore_index=True)
    df.to_csv(FILE, index=False)

    print("✅ Expense Added Successfully!!\n")

#----------View All Expenses-----------
#def view_expense runs when user chooses option 2 from menu
#df.empty is a pandas attribute returns true if no rowss and false if  data exists

def view_expense():
    df = pd.read_csv(FILE)

    if df.empty:
        print("No expenses found!\n") #user friendly message instead of blank output
    else:
        print("\n-------All expenses------")
        print(df, "\n")
    # else =means when df is not empty 
    #\n is for new line 

#-------Filter by category------
#to show expenses of one particular category 
# pd.read_csv(FILE)==loads all expense data from expenses.csv into DataFrame df
#df["Category"]==selects the category column 
#.str.lower()==convertS all the category values to lowercase
#category enter from user stored in cat and cat.lower() user input also converted to lowercase
# == compare both

def category_wise():
    

    cat = input("Enter Category to filter: ")

    result = df[df["Category"].strlower() == cat.lower()]

    if result.empty:
        print("No record for this category!\n")
    else:
        print(result, "\n")

#-------Total Expense---------
#df["Amount"].sum() ==selects the amount column adds all values using .sum() and stores result in variable total

def total_expense():
    df = pd.read_csv(FILE)

    total = df["Amount"].sum()

    print(f"\n 💸Total Expense = {total}\n")

#--------------Monthly Summary----------
# the goal of this function is to add expenses month-wise for e.g january total=200+150=350

# to_datetime() is a pandas function-----> it converts the text/string date into real date format

# .dt.to_period("M") it is part of pandas datetime accessor----- .dt is pandas datetime accessor and .to_period("M") is a pandas method it converts full date ----> only month-Year-period

# groupby is pandas function 
# groupby("column name")["Another column"].function()
#===== group data by---> "column name"
# === "another_column"---> "another column"
# =====apply function() like sum,count,mean etc


#df["Date"] = pd.to_datetime(df["Date"]) as i know that my date column is originally text "2024-01-05" a string this line converts it into real date  so python can understand month and  year
#df["Month"] = df["Date"].dt.to_period("M")==creates a new colum called month take date ---> keep only Year + Month
#summary = df.groupby("Month")["Amount"].sum()====group rows by month then add their Amount group 2024-01--> 200+150=350

#this function tellls us how much money u spent in each month
def monthly_summary():
    df = pd.read_csv(FILE)

    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.to_period("M")

    summary = df.groupby("Month")["Amount"].sum()

    print("\n 📅 Monthly Expense Summary")
    print(summary,"\n")


#------------Menu-----------------
while True:
    print("========Expense Tracker==============")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Category Wise Filter")
    print("4. Total Expense")
    print("5. Monthly Summary")
    print("6. Exit")

    ch = input("Enter Choice: ")

    if ch == "1":
        add_expense()

    elif ch == "2":
        view_expense()

    elif ch == "3":
        category_wise()

    elif ch == "4":
        total_expense()
        
    elif ch == "5":
        monthly_summary()

    elif ch =="6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!\n")
    

    





