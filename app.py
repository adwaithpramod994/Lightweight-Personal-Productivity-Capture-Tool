from flask import Flask, render_template, request, redirect

from gemini import extract_tasks

from database import (
    create_database,
    add_task,
    get_tasks,
    complete_task,
    delete_task
)

app = Flask(__name__)


@app.route("/")
def dashboard():

    tasks = get_tasks()

    total = len(tasks)
    completed = len([task for task in tasks if task["status"] == "Completed"])
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

    user_input = request.form.get("user_input", "").strip()

    if not user_input:
        return redirect("/capture")

    print("\n========== USER INPUT ==========")
    print(user_input)

    result = extract_tasks(user_input)

    print("\n========== GEMINI RESULT ==========")
    print(result)
    print("===================================\n")

    tasks = result.get("tasks", [])

    if tasks:

        for task in tasks:

            print("Adding task:", task)

            add_task(
                task.get("title", "Untitled Task"),
                task.get("category", "Personal"),
                task.get("priority", "Medium"),
                task.get("status", "Pending")
            )

    else:
        print("No tasks extracted!")
        print("Error:", result.get("error"))

    return redirect("/")


@app.route("/tasks")
def task_page():

    tasks = get_tasks()

    return render_template(
        "tasks.html",
        tasks=tasks
    )


@app.route("/complete/<int:task_id>")
def complete(task_id):

    complete_task(task_id)

    return redirect("/tasks")


@app.route("/delete/<int:task_id>")
def delete(task_id):

    delete_task(task_id)

    return redirect("/tasks")


@app.route("/analytics")
def analytics():

    tasks = get_tasks()

    categories = {}

    for task in tasks:

        category = task["category"]

        categories[category] = categories.get(category, 0) + 1

    return render_template(
        "analytics.html",
        tasks=tasks,
        categories=categories
    )


if __name__ == "__main__":

    create_database()

    app.run(debug=True)