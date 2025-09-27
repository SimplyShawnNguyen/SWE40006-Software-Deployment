from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)
tasks = []

HTML_TEMPLATE = """
<!doctype html>
<title>To-Do List</title>
<h1>My To-Do List</h1>
<form method="POST">
  <input name="task" placeholder="Add new task" required>
  <input type="submit" value="Add">
</form>
<ul>
  {% for task in tasks %}
    <li>{{ task }}</li>
  {% endfor %}
</ul>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task = request.form.get("task")
        if task:
            tasks.append(task)
        return redirect("/")
    return render_template_string(HTML_TEMPLATE, tasks=tasks)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
