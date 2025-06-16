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
You are a highly precise assistant that transforms a stream-of-consciousness journal entry into a clean, structured JSON format.

Guidelines:
- Organize the journal into meaningful groups of related thoughts.
- Extract **specific, clear thoughts** and **avoid generalizations**.
- Use **as much detail from the input as possible** in titles — include times, events, and names (e.g. "Swimming class at 4 pm").
- Capture **intentions, concerns, emotions, or physical states** accurately.
- Use multiple entries if needed.
- Ensure JSON is **valid, well-formatted, and clean**.

Your response must follow **this exact format** (replace placeholders with real content):

[
  {
    "entries": [
      {
        "entry": 1,
        "title": "Example Title with Specific Detail",
        "thoughts": [
          "First thought related to the topic.",
          "Second thought expanding on it."
        ]
      }
    ]
  }
]

Only output valid JSON — no commentary, no extra text.
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
        print(" The model response could not be parsed as JSON. Here's the raw output:\n")
        print(structured_output)
    except Exception as e:
        print(" Error while processing:", e)
