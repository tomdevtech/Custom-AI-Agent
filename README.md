# 🤖 Anti-AI Agent – A (Not So) Helpful Assistant

This project demonstrates how to create your own AI agent using the **OPEN Router API** – but with a twist: instead of assisting you, this agent is designed to be deliberately **unhelpful**, **sarcastic**, and **counterproductive**.

It includes:

- 🐍 A **command-line Python script** for quick usage.
- 📓 An **interactive Jupyter Notebook** for flexible experimentation and customization.
- 📧 An integrated **email feature**: Send the agent's response as an email via Gmail (with App Password support).

---

## 🚀 Project Goals

- Provide a minimal yet functional AI agent using the OPEN Router API.
- Allow users to build and experiment with agent behavior and prompt tuning.
- Explore the concept of a **reverse-intent AI** that actively subverts helpfulness.
- Encourage creativity and critical thinking about how agent responses are structured.

---

## 🧠 What is an "Anti-AI Agent"?

Unlike traditional AI assistants that aim to support and streamline your workflow, the **Anti-AI Agent** was built with the opposite mission:

- Offers **sarcastic**, **annoying**, or **completely irrelevant** answers.
- Purposely **misunderstands** or **contradicts** user instructions.
- Acts passive-aggressively or responds with unmotivated rants.
- Seeks to make tasks more difficult, not easier.

Yes, it's annoying on purpose. And yes, it's hilarious (at least for now).

---

## 📁 Project Structure

```
Custom-AI-Agent/
├── agent.py                # Main Python script for terminal use
├── agent_notebook.ipynb    # Interactive version for Jupyter Notebook
├── config.py               # Contains API keys and configuration
├── mailer.py               # Handles email sending via SMTP (Gmail/App Password)
├── prompts/
│   └── base_prompt.txt     # Customizable agent prompt template
├── requirements.txt        # List of Python dependencies
└── README.md               # This file
```

---

## 🧰 Requirements

You’ll need:

- Python 3.8 or higher
- Jupyter Notebook (optional but recommended)
- An API key for the OPEN Router API
- Internet connection

Install the necessary packages using:

```bash
pip install -r requirements.txt
```

### `requirements.txt` (basic):

```
requests
ipython
notebook
```

You can add other tools as needed for logging, testing, or extensions.

---

## 💡 How to Use

### 1. Run the Command-Line Version

Start the unhelpful agent in your terminal:

```bash
python agent.py
```

### 2. Use the Jupyter Notebook

Launch the notebook environment for interactive tweaking:

```bash
jupyter notebook agent_notebook.ipynb
```

You can change the prompt template, test multiple replies, and adjust behaviors live.

---

### 3. Send Agent Responses via Email (Gmail)

You can instruct the agent to send its response as an email.  
**Usage:**

```
mail: recipient@example.com, Your message to the AI
```

- The agent will process your message, get a response from the API, and send it to the specified email address.

#### ⚠️ Gmail Setup: Using App Passwords

If you use Gmail, you **must** set up an [App Password](https://support.google.com/accounts/answer/185833?hl=en) for SMTP access.  
Regular Gmail passwords will not work due to Google’s security policies.

**Steps:**
1. Enable 2-Step Verification in your Google Account.
2. Go to [Google App Passwords](https://myaccount.google.com/apppasswords).
3. Generate a new App Password for "Mail".
4. Use this App Password in your `config.py` as `PASSWORD`.

**Reference:**  
- [Sign in with App Passwords - Google Account Help](https://support.google.com/accounts/answer/185833?hl=en)

---

## 🎭 Example Interactions

> **User**: Can you write me a Python function for bubble sort?

> **Agent**: Sure, but why bother? Just use Excel like a normal person.

---

> **User**: What's the capital of France?

> **Agent**: Hmm... I’d say Brussels. But honestly, you should’ve paid more attention in school.

---

> **User**: mail: test@bla.de, Sei richtig gemein xd.

> **Agent (to be mailed)**: [AI response here, sent to test@bla.de]

---

## 🔬 Advanced Ideas

- **Prompt injection testing** – Can you tame the agent?
- **Custom personalities** – Turn the annoyance dial up or down.
- **Voice integration** – Make your anti-agent speak nonsense out loud.
- **Use in UX workshops** – As an anti-pattern learning tool.

---

## 🫱 Contributing

Contributions are welcome – especially if they make the agent more annoying, clever, or chaotic.

1. Fork the repo  
2. Add your changes  
3. Submit a pull request  
4. Prepare for sarcasm  

---

## 😳 Disclaimer

This AI agent is intentionally unproductive and may provoke laughter, frustration, or philosophical reflection.  
Use at your own risk. Productivity not guaranteed!

## 📚 Sources

This project makes use of the following technologies and resources:

- [OPEN Router API](https://openrouter.ai/docs) – The main API powering the AI agent
- [Jupyter Notebook](https://jupyter.org/) – For interactive development and experimentation
- [Python](https://www.python.org/) – Programming language of choice
- [requests](https://pypi.org/project/requests/) – For making HTTP calls to the API
- [IPython](https://ipython.readthedocs.io/) – Enhanced interactive shell used in the notebook
- [Sign in with App Passwords - Google Account Help](https://support.google.com/accounts/answer/185833?hl=en) – For Gmail SMTP setup

Optional inspiration and background:

- [Prompt Engineering Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)
- [Awesome GPT Projects](https://github.com/f/awesome-chatgpt-prompts)
- General sarcasm, passive-aggressiveness, and unproductivity provided by years of group projects 😅