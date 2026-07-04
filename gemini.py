import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

# Load API Key
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

# Load Gemini Model
model = genai.GenerativeModel("gemini-1.5-flash")


def extract_tasks(user_input):
    """
    Accepts user text and returns:
    - Extracted tasks
    - Category
    - Priority
    - Status
    - Summary
    """

    prompt = f"""
You are an AI assistant for a Personal Productivity Tool.

The user will enter tasks or notes in natural language.

Your job is to:

1. Extract every individual task.
2. Categorize each task into ONLY:
   - Study
   - Work
   - Personal

3. Assign Priority:
   - High
   - Medium
   - Low

4. Every task should have:
   - title
   - category
   - priority
   - status = Pending

5. Generate a short summary.

IMPORTANT:
Return ONLY valid JSON.

Example format:

{{
    "tasks": [
        {{
            "title": "Complete AI Project",
            "category": "Study",
            "priority": "High",
            "status": "Pending"
        }},
        {{
            "title": "Buy Groceries",
            "category": "Personal",
            "priority": "Low",
            "status": "Pending"
        }}
    ],
    "summary": "Complete the AI project and buy groceries."
}}

User Input:

{user_input}
"""

    try:

        response = model.generate_content(prompt)

        text = response.text.strip()

        # Remove Markdown formatting if Gemini returns it
        if text.startswith("```json"):
            text = text.replace("```json", "").replace("```", "").strip()

        return json.loads(text)

    except Exception as e:

        return {
            "tasks": [],
            "summary": "",
            "error": str(e)
        }