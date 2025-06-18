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
I started my day at 5:25 AM and went to the gym around 6:00 AM. I did a workout and returned home by 7:15 AM. After completing my necessary morning routine, I attended a morning meeting at 7:47 AM. The meeting included a presentation on acids and bases, covering their role in everyday life along with some experiments and classifications.I'm also volunteering at a workshop called Beshma Hunt for children in grades 1 to 6. This workshop helps enhance their brain function through simple questions like puzzles, math problems, etc.Due to the morning meeting, I had a late breakfast. I also attended my daily stand-up meeting with Vikram Sir at 9:30 AM. My task for the day is to complete the Transcriber program, which converts an audio file (e.g., an MP3) into text in JSON format. As per my instructions, once completed, I need to upload the project to GitHub and share the repository link in Basecamp by 4:30 PM.After that, I’ll head back to the dormitory by 5:00 PM, and at 5:30 PM, I’ll go to the ground since I’m the mentor for my football team. I plan to return around 7:15 PM, take some rest, have dinner, and then work until 10:30 PM before going to bed to wake up early again the next morning.

```
Output (structured JSON):

```json
[
  {
    "entry": 1,
    "title": "Woke up at 5:25 AM",
    "description": "Started the day by waking up at 5:25 AM."
  },
  {
    "entry": 2,
    "title": "Gym at 6:00 AM",
    "description": "Went to the gym at 6:00 AM and completed a workout, returning home by 7:15 AM."
  },
  {
    "entry": 3,
    "title": "Morning meeting at 7:47 AM",
    "description": "Attended a morning meeting at 7:47 AM, which included a presentation on acids and bases, covering their role in everyday life along with some experiments and classifications."
  },
  {
    "entry": 4,
    "title": "Volunteering at Beshma Hunt",
    "description": "Volunteering at a workshop called Beshma Hunt, which helps enhance the brain function of children in grades 1 to 6 through simple questions like puzzles, math problems, etc."
  },
  {
    "entry": 5,
    "title": "Late breakfast",
    "description": "Had a late breakfast due to the morning meeting."
  },
  {
    "entry": 6,
    "title": "Daily stand-up meeting with Vikram Sir at 9:30 AM",
    "description": "Attended a daily stand-up meeting with Vikram Sir at 9:30 AM."
  },
  {
    "entry": 7,
    "title": "Task: Complete Transcriber program",
    "description": "The task for the day is to complete the Transcriber program, which converts an audio file into text in JSON format."
  },
  {
    "entry": 8,
    "title": "Upload project to GitHub by 4:30 PM",
    "description": "Once the Transcriber program is completed, need to upload the project to GitHub and share the repository link in Basecamp by 4:30 PM."
  },
  {
    "entry": 9,
    "title": "Return to dormitory at 5:00 PM",
    "description": "Will head back to the dormitory after completing the task."
  },
  {
    "entry": 10,
    "title": "Football team mentor at 5:30 PM",
    "description": "Will go to the ground at 5:30 PM as the mentor for the football team."
  },
  {
    "entry": 11,
    "title": "Return from football at 7:15 PM",
    "description": "Plan to return from football around 7:15 PM, take some rest, have dinner, and then work until 10:30 PM before going to bed to wake up early again the next morning."
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





