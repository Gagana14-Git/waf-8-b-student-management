
from flask import Flask, request, render_template_string

app = Flask(__name__)
students = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"].strip()
        department = request.form["department"].strip()

        if name and department:
            students.append({
                "name": name,
                "department": department
            })

    return render_template_string("""
    <h2>Student Information Management System - Updated</h2>

    <form method="POST">
        Student Name: <input name="name" required><br><br>
        Department: <input name="department" required><br><br>
        <button type="submit">Add Student</button>
    </form>

    <h3>Student Records</h3>
    {% for s in students %}
        <p>{{ s.name }} - {{ s.department }}</p>
    {% endfor %}
    """, students=students)

if __name__ == "__main__":
    app.run(debug=True)
