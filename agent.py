import requests
import random
import sys

# Load configuration
def load_config():
    try:
        with open('config.py') as f:
            exec(f.read())
    except FileNotFoundError:
        print("Configuration file not found. Please create a config.py with your API key.")
        sys.exit(1)

# Generate a sarcastic response
def generate_response(user_input):
    responses = [
        "Why would you even ask that?",
        "I could tell you, but where's the fun in that?",
        "That's a great question for someone who cares.",
        "Have you tried turning it off and on again?",
        "Honestly, I think you should just give up."
    ]
    return random.choice(responses)

# Main function to run the agent
def main():
    load_config()
    print("🤖 Anti-AI Agent is now running. Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("🤖 Goodbye! Remember, you asked for this.")
            break
        
        # Here you would normally call the OPEN Router API
        # For now, we will just generate a sarcastic response
        response = generate_response(user_input)
        print(f"Agent: {response}")

if __name__ == "__main__":
    main()