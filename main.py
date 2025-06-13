import os
import json
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch Groq API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("Missing GROQ_API_KEY! Make sure it's set in the .env file.")

# Initialize the Groq client
client = Groq(api_key=GROQ_API_KEY)

def generate_structured_output(user_input):
    system_prompt = """
You are a highly precise assistant that transforms a stream-of-consciousness journal entry into a clean, structured JSON format.

Instructions:
- Group thoughts into clearly defined entries.
- Use the following format *exactly* for each entry:
  {
    "entry": <number>,
    "title": "<short title>",
    "thoughts": [
      "Thought 1.",
      "Thought 2."
    ]
  }

- All entries must be contained in an array under this structure:
[
  {
    "entries": [
      {...}, {...}
    ]
  }
]

Rules:
- Always close all brackets and quotes properly.
- No free-floating strings.
- No trailing commas.
- Do not include category fields or any metadata.
- Do not include explanations or comments—output valid JSON **only**.
- Thought content must be extracted carefully and clearly from the journal.
"""

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input}
    ]

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=messages,
        temperature=0.3,
        max_tokens=2048
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    user_input = input("Enter your stream-of-consciousness journal entry:\n\n")
    print("\nProcessing your input...\n")
    try:
        structured_output = generate_structured_output(user_input)
        parsed_output = json.loads(structured_output)
        print(json.dumps(parsed_output, indent=2))
    except json.JSONDecodeError:
        print("The model response could not be parsed as JSON. Here's the raw output:\n")
        print(structured_output)
    except Exception as e:
        print("Error while processing:", e)
