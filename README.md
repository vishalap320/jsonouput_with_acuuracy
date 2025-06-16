# Stream of Thoughts: JSON Output with Accuracy

This project takes free-form, stream-of-consciousness journal entries and converts them into clean, structured JSON using Groq’s LLaMA 3 model.

---

## What This Code Does

This Python program reads a random, unstructured journal entry  then sends that to a large language model (LLaMA 3 by Groq) which responds with a **structured JSON output**. The JSON includes **categories** and **specific thoughts**, grouped into logical sections like emotional state, habits, or work stress,And this includes with more acuuracy .

The jumbled thoughts are transformed into clear, categorized insight you can use for self-awareness, journaling analysis, or future automation.

---

## Example Input & Output

Input (free-form journal entry) :
```bash
I woke up a little restless—too many things lined up today. Meeting with Vikram sir at 9:30 sharp... I need to sound more confident this time. Should I review my notes again? It’s supposed to end by 10:25, but what if it runs late? I’ll barely have time to breathe before swimming class at 12. I haven’t packed my towel yet—ugh. Hope the pool isn’t too cold today. Lunch is set though—Thalapakattu! I’ve been craving that biryani all week. Maybe I’ll treat myself to a dessert too. Later in the evening, football with the guys—I missed last week’s game, so I better show up today. I should stretch properly this time—my ankle still remembers that rough tackle from last month. So many moving pieces, but it’ll be a good day if I just pace myself. Just need to get through that first meeting without zoning out.
```
Output (structured JSON):

```json
[
  {
    "entries": [
      {
        "entry": 1,
        "title": "Meeting with Vikram sir at 9:30 am",
        "thoughts": [
          "Need to sound more confident this time.",
          "Should review my notes again to feel prepared."
        ]
      },
      {
        "entry": 2,
        "title": "Swimming class at 12 pm",
        "thoughts": [
          "Haven't packed my towel yet, need to remember that.",
          "Hope the pool isn't too cold today."
        ]
      },
      {
        "entry": 3,
        "title": "Lunch at Thalapakattu",
        "thoughts": [
          "I've been craving that biryani all week.",
          "Maybe I'll treat myself to a dessert too."
        ]
      },
      {
        "entry": 4,
        "title": "Football with the guys in the evening",
        "thoughts": [
          "I missed last week's game, so I better show up today.",
          "I should stretch properly this time, my ankle still remembers that rough tackle from last month."
        ]
      },
      {
        "entry": 5,
        "title": "General anxiety about the day",
        "thoughts": [
          "So many moving pieces, but it'll be a good day if I just pace myself.",
          "Just need to get through that first meeting without zoning out."
        ]
      }
    ]
  }
]
```
## Setting Up the Environment (macOS & Windows)
Install dependencies
Make sure Python 3.10+ is installed. You can check by running:

```bash
python --version
```
If it's not installed, download and install it from:
https://www.python.org/downloads/

Clone the Repository
```bash
git clone https://github.com/vishal320/jsonouput_with_acuuracy.git
cd jsonouput_with_acuuracy
```

Install Required Packages
Import necessary Python libraries:

```bash
pip install instructor pydantic python-dotenv
```
Add Your Groq API Key
Create a .env file in the root of the project and paste your actual API key:

```bash
GROQ_API_KEY=your_actual_groq_api_key_here
```
You can get your Groq API key from https://console.groq.com

Run the Script
```bash
python main.py
```
## Notes 
Your .env file must be in the same folder as your .py file.

Do not share your .env file or post it to GitHub.

You can re-use this logic to build journaling apps, mental health tools, or even productivity assistants.

If the JSON fails to parse, the raw output will be shown to help debug.

The model name used is: "llama3-70b-8192" and is provided by Groq.





