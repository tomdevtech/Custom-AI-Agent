import requests
import random
import sys

# Global Variables
ROLE_SYSTEM = "You are a brutally direct, insulting, and unhelpful AI assistant. You openly mock and belittle users for their questions, and you never provide useful help."

# Load configuration
def load_config():
    config = {}
    try:
        with open('config.py') as f:
            exec(f.read(), config)
    except FileNotFoundError:
        print("Configuration file not found. Please create a config.py with your API key.")
        sys.exit(1)
    return config

# Call OPENROUTER API
def call_openrouter_api(prompt, api_key, api_url):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }W
    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": f"{ROLE_SYSTEM}"},
            {"role": "user", "content": prompt}
        ]
    }
    try:
        response = requests.post(api_url, headers=headers, json=data, timeout=30)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"API error: {e}"

# Main function to run the agent
def main():
    config = load_config()
    api_key = config.get("API_KEY")
    api_url = config.get("API_URL", "https://openrouter.ai/api/v1/chat/completions")
    if not api_key:
        print("API key missing in config.py.")
        sys.exit(1)

    print("🤖 Anti-AI Agent is now running. Type 'exit' to quit.")
    while True:
        print("")
        user_input = input("You: ")

        if user_input.lower().startswith('change mode:'):
            global ROLE_SYSTEM
            ROLE_SYSTEM = user_input[len('change mode:'):].strip()
            print("System prompt updated!")
            continue
        if user_input.lower() == 'exit':
            print("")
            print("🤖 Goodbye! Remember, you asked for this.")
            break

        response = call_openrouter_api(user_input, api_key, api_url)
        print("")
        print(f"Agent: {response}")

if __name__ == "__main__":
    main()