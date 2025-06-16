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
- Create a short title for each entry, using **detailed language** from the input (include times, names, places, or events when mentioned — e.g., "Swimming class at 4 pm").
- Extract **exact thoughts** as stated — retain proper names, times, events, and emotions. Do not generalize.
- Be faithful to the input wording and tone.
- Group related thoughts under the same entry.
- Use multiple entries if needed.
- Ensure the JSON is **valid, clean, and contains no extra explanation or text**.

Use the format below exactly:

[
  {
    "entries": [
      {
        "entry": 1,
        "title": "Detailed Title Here",
        "thoughts": [
          "Specific thought with full context and detail.",
          "Another detailed thought directly from the original input."
        ]
      }
    ]
  }
]
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
