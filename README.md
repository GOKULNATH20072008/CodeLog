Code Log
#### Video Demo: https://www.youtube.com/watch](https://youtu.be/4M_zbwmULmg)
#### Description:

Hey everyone! This is my final project. I'm an 18-year-old student who just finished my Class 12 CBSE exams with Computer Science, and I also recently completed Harvard's CS50P (Introduction to Programming with Python) course online. In Class 12, they taught us all about relational databases, primary keys, and how to interface Python with SQL databases using basic SQL commands. At the same time, CS50P taught me how to write clean, modular Python code, use loops safely, handle exceptions using `try-except` blocks, and work with external pip packages like `fpdf`.

I noticed that a lot of seniors and older students online talk about grinding LeetCode, HackerRank, and Codeforces to prepare for tech interviews. They solve hundreds of problems, but keeping track of everything in a random Excel sheet or a notebook looked super messy. Since I wanted to practice my new programming skills, I decided to combine my Class 12 SQL knowledge with my CS50P Python knowledge to build a real, fully-working **Code Log**! 

It’s a command-line app where you can log every problem you solve. It stores the title, platform, topic, difficulty, and date. It also automatically counts how many total problems you've solved right on the main menu, lets you search by specific topics, and can even export your entire history into a clean PDF report!

---

### What Each File Does

#### `project.py`
This is the main Python script where all the magic happens. I used the procedural programming style I learned in CS50P to break everything down into clean, separate functions so it doesn't look like a giant spaghetti mess:
* `main()`: Runs a continuous `while True` loop that keeps the menu alive in the terminal until you choose option 5 to exit. It also prints out your total progress statistics dynamically every time the menu loops.
* `create_database()`: This runs right when you start the program. It uses SQL commands like `CREATE TABLE IF NOT EXISTS` (just like what we learned in the CBSE board syllabus) to set up our table with an autoincrementing ID, text fields, and constraints.
* `add_problem_menu()` & `add_problem()`: The menu function handles the `input()` from the user and makes sure everything looks good. Then it passes the data to `add_problem()`, which executes an `INSERT INTO` SQL query using `?` placeholders to safely save the data.
* `view_problems()` and `search_by_topic()`: These functions handle the data retrieval. `view_problems` fetches everything with `SELECT *`, while `search_by_topic` uses a `where lower(topic)=?` clause so that it doesn't matter if the user types "graphs" or "Graphs".
* `validate_difficulty()`: A simple helper function that checks if the input matches 'Easy', 'Medium', or 'Hard' so junk data doesn't corrupt the database.
* `export_pdf()`: This uses the `FPDF` library. It loops through all the rows from our SQL query and dynamically writes them into a nicely spaced, multi-line layout to generate a local PDF.

#### `tracker.db`
This is the actual SQLite database file. Instead of saving data to a normal text file that can get erased or messed up easily, this database file holds our structured table. It automatically creates itself the first time you run the script, so you don't have to configure anything manually.

#### `problem_report.pdf`
This file is generated on-demand whenever you type option `4` in the menu. It reads your latest database stats and turns them into an external, printable document. It’s perfect if you want a physical copy of your progress or want to show off your grind to a mentor.

---

### Design Decisions & Things I Debated

#### 1. Text Files vs. SQL Databases
When I first started thinking about this project, I considered just using a basic CSV or text file to save the data because it seemed easier at first glance. But from my Class 12 CS theory classes, I knew that flat files don't have built-in data integrity, can easily get corrupted if the program crashes mid-write, and making searches on them requires writing a bunch of extra Python logic. By using SQLite3, I got to use real SQL queries, secure inputs to prevent injection bugs, and proper data constraints. It made the storage system way faster and more secure.

#### 2. CLI Terminal vs. Graphic User Interface (GUI)
I spent some time considering whether to build a graphical desktop window using a library like `tkinter`. From a workflow perspective, a command-line interface (CLI) makes total sense: when software engineers are practicing coding problems on LeetCode, they are already completely locked into their code editors and terminal screens. A CLI is fast, completely distraction-free, and lets you log your solved problems in three seconds flat without taking your hands off the keyboard to hunt for a mouse. 

But if I am being 100% honest, there was another major factor: I also didn't know how to use `tkinter` properly yet! Between finishing up Class 12 and diving deep into backend logic with CS50P, learning a massive GUI framework on top of everything felt like trying to defeat a final boss with starting-level gear. So, I leaned into the CLI, optimized it to look as clean as possible, and saved the GUI learning curve for my next project!

#### 3. Date Validation Issues
At first, I was just going to let the user type whatever they wanted for the date. But I realized people might make typos, type "tomorrow", or mix up the day and month formats, which would completely break any future sorting features. I used David Malan’s advice from CS50P to use Python’s built-in `datetime` library. By wrapping `datetime.strptime(solved_date, "%Y-%m-%d")` in a strict `try-except` block inside a `while` loop, the program literally refuses to accept the input until it’s formatted exactly as a valid `yyyy-mm-dd` calendar date.
