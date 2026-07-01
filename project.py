import sqlite3
from datetime import datetime #datetime module
from fpdf import FPDF


def main():
    create_database()
    while True:
        print("\n===CodeLog===")
        print(f"Total Problems Solved: {len(view_problems())}")
        print("-----------------------------------")
        print("1. Add Problem")
        print("2. View Problems")
        print("3. Search Problems")
        print("4. Export PDF")
        print("5. Exit")
        choice=input("Enter your choice: ").strip()
        if choice=="1":
            add_problem_menu()

        elif choice=="2":
            problems=view_problems()
            for problem in problems:
                print(problem)

        elif choice=="3":
            topic=input("Enter topic: ").strip()
            search_by_topic(topic)

        elif choice == "4":
            export_pdf()

        elif choice == "5":
            break


def create_database():
    mycon=sqlite3.connect("tracker.db")
    cur=mycon.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS problems (
                   id INTEGER primary key AUTOINCREMENT,
                   title VARCHAR NOT NULL,
                   platform VARCHAR NOT NULL,
                   topic VARCHAR NOT NULL,
                   difficulty VARCHAR NOT NULL,
                   solved_date TEXT
                   )                
    """
    )
#doctring :)
    mycon.commit()
    mycon.close()

def add_problem(title,topic,platform,difficulty,solved_date):
    mycon=sqlite3.connect("tracker.db")
    cur=mycon.cursor()
    cur.execute("""
                INSERT INTO problems(title,topic,platform,difficulty,solved_date)
                VALUES(?,?,?,?,?)
                """,(title,topic,platform,difficulty,solved_date))
    #docstring :)

    mycon.commit()
    mycon.close()

def view_problems():
    mycon=sqlite3.connect("tracker.db")
    cur=mycon.cursor()
    cur.execute("SELECT * FROM problems")
    rows=cur.fetchall()
    mycon.close()
    return rows


def add_problem_menu():
    title=input("Title: ")
    platform=input("Platform: ")
    topic=input("Topic: ")
    while True:
        difficulty=input("Difficulty: ")
        if validate_difficulty(difficulty.capitalize()):
            break
        print("Invaild Difficulty")
    while True:
        solved_date=input("Solved date (yyyy-mm-dd)").strip()
        try:
            datetime.strptime(solved_date,"%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format! Please use YYYY-MM-DD.")

    add_problem(title,topic,platform,difficulty.capitalize(),solved_date)
    print("Problem successfully addedd!")

def search_by_topic(topic):
    mycon=sqlite3.connect("tracker.db")
    cur=mycon.cursor()
    cur.execute(f"select * from problems where lower(topic)=?",(topic.lower(),))
    rows=cur.fetchall()
    mycon.close()
    if not rows:
        print("No problems found")

    else:
        for row in rows:
            print(row)
    return rows

def format_problem_string(row):
    
    return f"[{row[4]}] {row[1]} on {row[2]} ({row[3]}) - Solved: {row[5]}"

def validate_difficulty(difficulty):
    valid=['Easy','Medium','Hard']
    return difficulty in valid #boolean return 

def export_pdf():
    mycon = sqlite3.connect("tracker.db")
    cur = mycon.cursor()

    cur.execute("SELECT * FROM problems")
    rows = cur.fetchall()

    mycon.close()

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Code_Log Report", ln=True)

    pdf.ln(5)

    pdf.set_font("Arial", size=12)

    for row in rows:
        pdf.multi_cell(
            0,
            8,
            f"ID: {row[0]}\n"
            f"Title: {row[1]}\n"
            f"Platform: {row[2]}\n"
            f"Topic: {row[3]}\n"
            f"Difficulty: {row[4]}\n"
            f"Solved Date: {row[5]}\n"
        )
        pdf.ln(2)

    pdf.output("problem_report.pdf")

    print("PDF exported successfully!")

if __name__=="__main__":
    main()