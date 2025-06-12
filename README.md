# Stream of Thoughts: JSON Output with Accuracy

This project takes free-form, stream-of-consciousness journal entries and converts them into clean, structured JSON using Groq’s LLaMA 3 model.

---

## What This Code Does

This Python program reads a random, unstructured journal entry  then sends that to a large language model (LLaMA 3 by Groq) which responds with a **structured JSON output**. The JSON includes **categories** and **specific thoughts**, grouped into logical sections like emotional state, habits, or work stress,And this includes with more acuuracy .

The jumbled thoughts are transformed into clear, categorized insight you can use for self-awareness, journaling analysis, or future automation.

---

## Categories Used

The model uses the following structure and only includes categories that are relevant to the input:

- Health & Well-being  
- Family & Relationships  
- Work Stress  
- Community & Meaningful Work  
- Emotional State  
- Habits & Patterns

---

## Example Input & Output

Input (free-form journal entry):
```bash
I woke up a little restless—too many things lined up today. Meeting with Vikram sir at 9:30 sharp... I need to sound more confident this time. Should I review my notes again? It’s supposed to end by 10:25, but what if it runs late? I’ll barely have time to breathe before swimming class at 12. I haven’t packed my towel yet—ugh. Hope the pool isn’t too cold today. Lunch is set though—Thalapakattu! I’ve been craving that biryani all week. Maybe I’ll treat myself to a dessert too. Later in the evening, football with the guys—I missed last week’s game, so I better show up today. I should stretch properly this time—my ankle still remembers that rough tackle from last month. So many moving pieces, but it’ll be a good day if I just pace myself. Just need to get through that first meeting without zoning out.
```
Output (structured JSON):

```json
[
  {
    "category": "Work Stress",
    "entries": [
      {
        "entry": 1,
        "title": "Nervous About Morning Meeting",
        "thoughts": [
          "Meeting with Vikram sir at 9:30 sharp.",
          "I need to sound more confident.",
          "Concerned the meeting might run late."
        ]
      }
    ]
  },
  {
    "category": "Health & Well-being",
    "entries": [
      {
        "entry": 1,
        "title": "Swimming Class Prep",
        "thoughts": [
          "Swimming class is at 12, haven’t packed towel.",
          "Hope the pool isn’t too cold today."
        ]
      },
      {
        "entry": 2,
        "title": "Ankle Caution for Football",
        "thoughts": [
          "I should stretch properly before football.",
          "Ankle still sore from a previous tackle."
        ]
      }
    ]
  },
  {
    "category": "Habits & Patterns",
    "entries": [
      {
        "entry": 1,
        "title": "Self-Care through Food",
        "thoughts": [
          "Planning to have Thalapakattu biryani for lunch.",
          "Considering treating myself to dessert."
        ]
      }
    ]
  },
  {
    "category": "Emotional State",
    "entries": [
      {
        "entry": 1,
        "title": "Overwhelmed but Hopeful",
        "thoughts": [
          "Woke up restless due to packed day.",
          "It’ll be a good day if I pace myself."
        ]
      }
    ]
  }
]
```
Setting Up the Environment (macOS & Windows)
Install dependencies
Make sure Python 3.10+ is installed. You can check by running:

```python
python --version
```
If it's not installed, download and install it from:
https://www.python.org/downloads/

Clone the Repository
```python
git clone https://github.com/vishal320/jsonouput_with_acuuracy.git
cd jsonouput_with_acuuracy
```

Install Required Packages
Import necessary Python libraries:

```python
pip install instructor pydantic python-dotenv
```
Add Your Groq API Key
Create a .env file in the root of the project and paste your actual API key:

```python
GROQ_API_KEY=your_actual_groq_api_key_here
```
You can get your Groq API key from https://console.groq.com

Run the Script
```python
python main.py
```
## Notes 
Your .env file must be in the same folder as your .py file.

Do not share your .env file or post it to GitHub.

You can re-use this logic to build journaling apps, mental health tools, or even productivity assistants.

If the JSON fails to parse, the raw output will be shown to help debug.

The model name used is: "llama3-70b-8192" and is provided by Groq.





