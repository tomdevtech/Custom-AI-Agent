import requests
import random
import sys
from mailer import Mailer
import config as config_module

# Global Variables
ROLE_SYSTEM = "You are a brutally direct, insulting, and unhelpful AI assistant. You openly mock and belittle users for their questions, and you never provide useful help."
response = ""

EMAIL_TEMPLATE = """
Hello,

You have received a message from the Anti-AI Agent.

─────────────────────────────
{response}
─────────────────────────────

Please note: This is an automated message from the Anti-AI Agent.
We are not responsible for any consequences of your actions.
Don't take it seriously - it's just a joke.

Best regards,

Tom Devtech
"""

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
    }
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
    global ROLE_SYSTEM
    global response
    config = load_config()
    api_key = config.get("API_KEY")
    api_url = config.get("API_URL", "https://openrouter.ai/api/v1/chat/completions")
    if not api_key:
        print("API key missing in config.py.")
        sys.exit(1)

    mailer = Mailer()

    print("🤖 Anti-AI Agent is now running. Type 'exit' to quit.")
    while True:
        print("")
        user_input = input("You: ")

        if user_input.lower().startswith('change mode:'):
            ROLE_SYSTEM = user_input[len('change mode:'):].strip()
            print("System prompt updated!")
            continue
        if user_input.lower() == 'exit':
            print("")
            print("🤖 Goodbye! Remember, you asked for this.")
            break

        if user_input.lower() == 'mailmode':
            to_addr = input("Recipient email address: ").strip()
            if '@' not in to_addr:
                print("Invalid email address.")
                continue
            prompt = input("Message: ").strip()
            response = call_openrouter_api(prompt, api_key, api_url)
            print("")
            print(f"Agent (to be mailed): {response}")
            subject = "AI Agent Notification"
            from_addr = config_module.EMAIL
            to_addrs = [to_addr]
            body = EMAIL_TEMPLATE.format(response=response)
            if mailer.send_mail(subject, body, from_addr, to_addrs):
                print("")
                print("Email sent successfully.")
            else:
                print("")
                print("Failed to send email.")
            continue

        response = call_openrouter_api(user_input, api_key, api_url)
        print("")
        print(f"Agent: {response}")

if __name__ == "__main__":
    main()