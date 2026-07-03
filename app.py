from flask import Flask, render_template, request
app = Flask(__name__)



# Sample Data


tasks = [
    {
        "title": "Complete AI Project",
        "category": "Work",
        "priority": "High",
        "status": "Pending"
    },
    {
        "title": "Prepare Java Interview",
        "category": "Study",
        "priority": "Medium",
        "status": "Completed"
    },
    {
        "title": "Revise DBMS",
        "category": "Study",
        "priority": "Medium",
        "status": "Pending"
    },
    {
        "title": "Buy Groceries",
        "category": "Personal",
        "priority": "Low",
        "status": "Completed"
    },
    {
        "title": "Read Research Paper",
        "category": "Work",
        "priority": "High",
        "status": "Pending"
    }
]


@app.route("/")
def dashboard():
    total = len(tasks)
    completed = len([t for t in tasks if t["status"] == "Completed"])
    pending = total - completed
    progress = int((completed / total) * 100)

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


@app.route("/tasks")
def task_page():
    return render_template(
        "tasks.html",
        tasks=tasks
    )


@app.route("/analytics")
def analytics():

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
    app.run(debug=True)