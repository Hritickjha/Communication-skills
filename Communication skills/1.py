import time

def introduce_yourself():
    print("Hello! I am your friendly Python communication script.")
    time.sleep(1)
    print("Let's have a conversation.")

def ask_question():
    user_question = input("You: ")
    return user_question

def respond_to_question(question):
    print(f"Bot: I'm just a simple script, but I'll do my best to answer. You asked: '{question}'")

def main():
    introduce_yourself()
    while True:
        user_question = ask_question()
        if user_question.lower() == 'exit':
            print("Bot: Thanks for the conversation. Goodbye!")
            break
        respond_to_question(user_question)

if __name__ == "__main__":
    main()