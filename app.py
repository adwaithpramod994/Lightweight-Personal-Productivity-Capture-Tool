from flask import Flask, render_template, request, redirect

app = Flask(__name__)

from gemini import extract_tasks

from database import (
    create_database,
    add_task,
    get_tasks,
    complete_task,
    delete_task
)






@app.route("/")
def dashboard():

    tasks = get_tasks()

    total = len(tasks)
    completed = len([t for t in tasks if t["status"] == "Completed"])
    pending = total - completed
    progress = int((completed / total) * 100) if total > 0 else 0

    return render_template(
        "dashboard.html",
        tasks=tasks,
        total=total,
        completed=completed,
        pending=pending,
        progress=progress
    )


@app.route("/capture")
def capture():
    return render_template("capture.html")


@app.route("/process", methods=["POST"])
def process():

    # Get text entered by the user
    user_input = request.form["user_input"]

    # Send text to Gemini AI
    result = extract_tasks(user_input)

    # Save each extracted task into SQLite
    for task in result["tasks"]:

        add_task(
            task["title"],
            task["category"],
            task["priority"],
            task["status"]
        )

    # Go back to dashboard
    return redirect("/")

@app.route("/tasks")
def task_page():

    tasks = get_tasks()

    return render_template(
        "tasks.html",
        tasks=tasks
    )


@app.route("/analytics")
def analytics():

    tasks = get_tasks()

    categories = {}

    for task in tasks:
        cat = task["category"]
        categories[cat] = categories.get(cat, 0) + 1

    return render_template(
        "analytics.html",
        tasks=tasks,
        categories=categories
    )

if __name__ == "__main__":
    create_database()   # Creates task.db and tasks table
    app.run(debug=True)