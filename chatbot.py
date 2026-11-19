
import random
from datetime import datetime

def greet_user():
    print("================================")
    print("       SMART ASSISTANT BOT      ")
    print("================================")

    name = input("Enter your name: ").strip()

    while not name:
        print("Please enter your name.")
        name = input("Enter your name: ").strip()

    print(f"\nHello, {name}!")
    print("I'm your Smart Assistant.")
    print("Type 'help' to see what I can do.")
    print("Type 'bye' to exit.")

    return name


def show_help():
    print("\n===== AVAILABLE COMMANDS =====")
    print("hello       - Greet the chatbot")
    print("time        - Show current time")
    print("date        - Show today's date")
    print("joke        - Tell a programming joke")
    print("calculate   - Perform calculations")
    print("python      - Learn about Python")
    print("technology  - Explore technology topics")
    print("help        - Show available commands")
    print("bye         - Exit chatbot")


def show_time():
    current_time = datetime.now().strftime("%I:%M:%S %p")
    print("Bot: Current time is", current_time)


def show_date():
    current_date = datetime.now().strftime("%d-%m-%Y")
    print("Bot: Today's date is", current_date)


def tell_joke():
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why was the computer cold? Because it left its Windows open!",
        "Why do Python programmers wear glasses? Because they cannot C!",
        "What is a programmer's favourite place? The Foo Bar!"
    ]

    print("Bot:", random.choice(jokes))


def calculator():
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            result = num1 + num2

        elif operator == "-":
            result = num1 - num2

        elif operator == "*":
            result = num1 * num2

        elif operator == "/":
            if num2 == 0:
                print("Bot: Cannot divide by zero!")
                return

            result = num1 / num2

        else:
            print("Bot: Invalid operator!")
            return

        print("Bot: Result =", result)

    except ValueError:
        print("Bot: Please enter valid numbers!")


def technology_info():
    question = input("What would you like to know? ").lower().strip()

    topics = {
        "python": "Python is a popular programming language used in AI, automation and web development.",

        "artificial intelligence": "AI enables machines to perform tasks that normally require human intelligence.",

        "machine learning": "Machine Learning allows computers to learn patterns from data and improve their performance.",

        "deep learning": "Deep Learning is a branch of Machine Learning that uses neural networks.",

        "cybersecurity": "Cybersecurity protects computers, networks and data from digital attacks.",

        "blockchain": "Blockchain is a distributed digital ledger that stores information securely.",

        "cloud computing": "Cloud Computing provides computing services such as storage and servers over the internet.",

        "internet of things": "IoT connects physical devices to the internet so they can collect and exchange data."
    }

    if question in topics:
        print("Bot:", topics[question])

    else:
        print("Bot: Sorry, I don't have information about that topic yet.")


def chat(name):
    while True:

        command = input("\nYou: ").lower().strip()

        if command == "hello":
            print(f"Bot: Hello, {name}! How can I help you?")

        elif command == "time":
            show_time()

        elif command == "date":
            show_date()

        elif command == "joke":
            tell_joke()

        elif command == "calculate":
            calculator()

        elif command == "python":
            print("Bot: Python is a popular, beginner-friendly programming language.")

        elif command == "technology":
            technology_info()

        elif command == "help":
            show_help()

        elif command == "bye":
            print(f"Bot: Goodbye, {name}! Have a nice day.")
            break

        else:
            print("Bot: Sorry, I don't understand that command. Type 'help' for options.")

user_name = greet_user()
chat(user_name)
