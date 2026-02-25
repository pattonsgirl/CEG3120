import random
import time

def silly_todo():
    tasks = []
    excuses = [
        "I'm currently updating my personality, try again later.",
        "That sounds like a 'you' problem, honestly.",
        "I've decided to go on strike until you buy me a better GPU.",
        "Error 404: Motivation not found.",
        "I'll add it, but I'm going to forget it immediately."
    ]

    print("--- 📝 The Aggressive Task Manager ---")
    
    while True:
        action = input("\nWhat do you want? (add/view/quit): ").lower()

        if action == "add":
            task = input("Fine, what's the task? ")
            if random.random() < 0.3:  # 30% chance of refusal
                print(f"\n[BOT]: {random.choice(excuses)}")
            else:
                tasks.append(task)
                print(f"\n[BOT]: Added '{task}'. I hope you're proud of yourself.")

        elif action == "view":
            if not tasks:
                print("\n[BOT]: Your list is as empty as my soul.")
            else:
                print("\n--- Your Burden ---")
                for i, t in enumerate(tasks, 1):
                    # Randomly "glitch" the task name
                    display_task = t[::-1] if random.random() < 0.2 else t
                    print(f"{i}. {display_task}")
                print("\n[BOT]: Seeing it all at once makes it worse, doesn't it?")

        elif action == "quit":
            print("\n[BOT]: Oh, leaving? Typical. I'll just delete these anyway.")
            time.sleep(1)
            print("Cleaning up...")
            time.sleep(1)
            print("System offline. Go eat a snack.")
            break
        else:
            print("\n[BOT]: I don't speak 'wrong input'. Try again.")

if __name__ == "__main__":
    silly_todo()
