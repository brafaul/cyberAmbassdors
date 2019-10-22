import sqlite3

conn = sqlite3.connect('database.db')
print("Database connection successfull")
""" cursor = conn.execute("SELECT Password from home WHERE Name='Test'")
for i in cursor:
    print(i)
"""
userName = input("What is your username?")
passWord = input("What is your password?")
statement = "SELECT Secret from Home WHERE Name='" + userName + "' AND Password='" + passWord + "'"
print(statement);
cursor = conn.execute(statement)
for i in cursor:
    print(i[0])
