import os
import json
from groq import Groq

# Set your Groq API key here directly or via environment variable
GROQ_API_KEY = os.getenv("GROQ_API_KEY") or "your-groq-api-key-here"

client = Groq(api_key=GROQ_API_KEY)

def generate_structured_output(user_input):
    system_prompt = """
You are a highly precise assistant that transforms a stream-of-consciousness journal entry into a clean, structured JSON format. Categorize each relevant idea under these sections:
- Health & Well-being
- Family & Relationships
- Work Stress
- Community & Meaningful Work
- Emotional State
- Habits & Patterns

Guidelines:
- Extract **specific, clear thoughts** and **avoid generalizations**.
- Capture **intentions, concerns, emotions, or physical states** accurately.
- Create a **short title** for each grouped thought.
- Use multiple entries per category if needed.
- Only include **categories mentioned or implied** in the journal entry.
- Ensure JSON is **valid, well-formatted, and clean**.

Your response must follow **this exact format** (replace placeholders with real content):

[
  {
    "category": "Health & Well-being",
    "entries": [
      {
        "entry": 1,
        "title": "Example Title",
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

    return response.choices[0].message.content

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
