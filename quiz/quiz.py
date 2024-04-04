import sqlite3
import matplotlib.pyplot as plt
import time

def create_database():
    # Connect to the database (or create if not exists)
    conn = sqlite3.connect('quiz_questions.db')
    c = conn.cursor()

    # Check if the quiz_questions table already exists
    c.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='quiz_questions' ''')
    if c.fetchone()[0] == 1:
        print("Database already exists. Skipping creation.")
        return

    # Create a table to store quiz questions
    c.execute('''CREATE TABLE quiz_questions
                 (id INTEGER PRIMARY KEY, 
                  question TEXT, 
                  option1 TEXT, 
                  option2 TEXT, 
                  option3 TEXT, 
                  option4 TEXT, 
                  correct_option TEXT)''')

    # Sample data: questions and options
    questions = [
        ("What is the value of π (pi)?", "3.14", "2.71", "1.618", "4.56", "A"),
        ("Who was the first President of the United States?", "Abraham Lincoln", "George Washington", "Thomas Jefferson", "John Adams", "B"),
        ("What is the chemical symbol for water?", "H", "O", "W", "H2O", "D"),
        ("Who wrote the play 'Romeo and Juliet'?", "William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain", "A"),
        ("Which continent is known as the 'Land of the Rising Sun'?", "Asia", "Europe", "Australia", "Africa", "A"),
        ("What is the main purpose of HTML?", "To define the structure of web pages", "To style web pages", "To create dynamic web applications", "To store data", "A"),
        ("What is the powerhouse of the cell?", "Nucleus", "Mitochondria", "Ribosome", "Chloroplast", "B"),
        ("Who painted the Mona Lisa?", "Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Michelangelo", "B"),
        ("What is the highest female singing voice?", "Alto", "Soprano", "Tenor", "Baritone", "B"),
        ("Which sport is associated with Wimbledon?", "Tennis", "Soccer", "Golf", "Cricket", "A")
    ]

    # Insert questions into the database
    c.executemany('INSERT INTO quiz_questions (question, option1, option2, option3, option4, correct_option) VALUES (?, ?, ?, ?, ?, ?)', questions)

    # Commit changes and close connection
    conn.commit()
    conn.close()

# Create the database if it doesn't exist
create_database()

# Connect to the database
conn = sqlite3.connect('quiz_questions.db')
c = conn.cursor()

def take_quiz():
    start_time = time.time()  # Start timer

    # Retrieve questions from the database
    c.execute("SELECT * FROM quiz_questions")
    questions = c.fetchall()

    correct_answers = 0
    incorrect_answers = 0

    print("Welcome to the Quiz!\n")
    for question in questions:
        print(question[1])  # Print the question
        print("A)", question[2])  # Print option A
        print("B)", question[3])  # Print option B
        print("C)", question[4])  # Print option C
        print("D)", question[5])  # Print option D

        user_answer = input("Your answer (A/B/C/D): ").upper()

        if user_answer == question[6]:
            print("Correct!")
            correct_answers += 1
        else:
            print("Incorrect!")
            incorrect_answers += 1

    end_time = time.time()  # End timer
    total_time = end_time - start_time  # Calculate total time

    print("\nQuiz completed in {:.2f} seconds!".format(total_time))
    print("Number of correct answers:", correct_answers)
    print("Number of incorrect answers:", incorrect_answers)

    # Plotting the graph
    labels = ['Correct', 'Incorrect', 'Total Time']
    counts = [correct_answers, incorrect_answers, total_time]

    plt.bar(labels, counts, color=['green', 'red', 'blue'])
    plt.xlabel('Answer')
    plt.ylabel('Number of Questions / Time (seconds)')
    plt.title('Quiz Results')
    plt.show()

# Call the function to start the quiz
take_quiz()

# Close the database connection
conn.close()
