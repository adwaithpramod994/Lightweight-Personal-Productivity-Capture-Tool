import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found. Please add it to your .env file.")

genai.configure(api_key=api_key)

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")


def extract_tasks(user_input):
    """
    Extracts tasks from natural language using Gemini AI.

    Returns:
    {
        "tasks": [...],
        "summary": "..."
    }
    """

    prompt = f"""
You are an AI assistant for a Personal Productivity Tool.

The user will enter tasks or notes in natural language.

Your responsibilities are:

1. Extract every individual task.
2. Categorize each task into ONLY one of:
   - Study
   - Work
   - Personal
3. Assign a priority:
   - High
   - Medium
   - Low
4. Every task must contain:
   - title
   - category
   - priority
   - status = Pending
5. Generate one short summary of the entire input.

Return ONLY valid JSON.

Example:

{{
    "tasks": [
        {{
            "title": "Complete AI project",
            "category": "Study",
            "priority": "High",
            "status": "Pending"
        }},
        {{
            "title": "Attend Java interview",
            "category": "Work",
            "priority": "High",
            "status": "Pending"
        }}
    ],
    "summary": "Complete the AI project and attend the Java interview."
}}

User Input:
{user_input}
"""

    try:

        response = model.generate_content(prompt)

        text = response.text.strip()

        # Remove markdown formatting if present
        text = text.replace("```json", "").replace("```", "").strip()

        # Extract only the JSON object
        start = text.find("{")
        end = text.rfind("}")

        if start == -1 or end == -1:
            raise ValueError("Gemini did not return valid JSON.")

        json_text = text[start:end + 1]

        result = json.loads(json_text)

        # Ensure required keys exist
        if "tasks" not in result:
            result["tasks"] = []

        if "summary" not in result:
            result["summary"] = ""

        # Ensure every task has required fields
        for task in result["tasks"]:

            task.setdefault("title", "Untitled Task")
            task.setdefault("category", "Personal")
            task.setdefault("priority", "Medium")
            task.setdefault("status", "Pending")

        return result

    except Exception as e:

        return {
            "tasks": [],
            "summary": "",
            "error": str(e)
        }