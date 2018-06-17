# Journal

import time  # recording the date
import sqlite3  # table entries
import pandas as pd  # printing an attractive table
import tabulate as tab  # printing an attractive table
import sys # exit script
import os


# Print Journal entries
def print_journal_entries():

    conn = sqlite3.connect('Journal.db')
    c = conn.cursor()
    df = pd.read_sql("SELECT * FROM Journal", conn)
    print(tab.tabulate(df, headers=["Date", "Entry"],
                            tablefmt='grid',
                            showindex=False) )


# Write new Journal entry
def write_new_entry():
    os.system("clear")
    date = time.strftime("%b %d, %Y | %H:%M |")
    print("+-------------+-------+-------------------------------------------+")
    print("|" + date + "     This is part of a jounral entry...    |")
    print("+-------------+-------+-------------------------------------------+")
    entry = sys.stdin.read()
    addTime = time.strftime("%H:%M")

    # \n ^D to finish entry.

    if entry.replace("\n","").replace(" ", "") != "":
        store_new_entry(addTime + "\n\n" + entry)
    else:
        print("Empty entry not committed.")



# Store new Journal entry
def store_new_entry(entry):

    date = time.strftime("%b %d, %Y")

    # Table entry process:
    conn = sqlite3.connect('Journal.db')
    c = conn.cursor()


    # If table hasn't already been created, create one:
    c.execute("CREATE TABLE IF NOT EXISTS Journal (num INTEGER PRIMARY KEY, date, entry)")

    c.execute("INSERT INTO Journal VALUES (?,?,?)", (None, date, entry))


    # Save and exit:
    conn.commit()
    conn.close()


def delete_last_entry():
    conn = sqlite3.connect('Journal.db')
    c = conn.cursor()
    c.execute("DELETE FROM Journal WHERE num = (SELECT MAX(num) FROM Journal);");
    conn.commit()
    conn.close()


def main():
    start = True
    while True:

        if start == True:
            os.system("clear")

        print("+----------------+-------------------------+--------------------+----------+")
        print("| New Entry (e)  |  Print Old Entries (p)  |  Delete Last (del) | Quit (q) |")
        print("+----------------+-------------------------+--------------------+----------+\n")
        response = input()

        if response == 'e':
            write_new_entry()

        elif response == 'p':
            print_journal_entries()

        elif response == 'del':
            delete_last_entry()

        elif response == 'q':
            print("\nGoodbye! :)")
            sys.exit()

        else:
            os.system("clear")
            print("Not an option, try again.")

        start = False


if __name__ == "__main__":
    main()







