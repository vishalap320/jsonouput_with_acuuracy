import os
import json
from groq import Groq
from dotenv import load_dotenv

# Load .env file if it exists
load_dotenv()

# Fetch the Groq API Key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("Missing GROQ_API_KEY! Make sure it's set in the .env file or your environment.")

# Initialize the Groq client
client = Groq(api_key=GROQ_API_KEY)

def generate_structured_output(user_input):
    system_prompt = """
You are a precise assistant that transforms a stream-of-consciousness journal entry into a structured JSON format.

Instructions:
- Break the journal entry into individual events or concerns.
- For each, provide:
  - "title": a short, specific summary (include time if present, e.g., "Swimming class at 12 PM").
  - "description": a detailed sentence (not a list) summarizing everything related to the title.
- Ensure every entry has both a "title" and a "description" key.
- Output only valid, complete JSON in this format:

[
  {
    "entries": [
      {
        "entry": 1,
        "title": "Short, specific title",
        "description": "Clear and complete description."
      }
    ]
  }
]

Notes:
- Do not include empty or partial entries.
- Do not include categories or commentary.
- Output only valid JSON, nothing else.
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
