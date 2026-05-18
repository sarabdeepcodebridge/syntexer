from flask import Blueprint, render_template
from app.problems import problems, glossary

main = Blueprint("main", __name__)

@main.route("/")
def index():
    categories = {}
    for problem in problems:
        topic = problem["topic"]
        if topic not in categories:
            categories[topic] = []
        categories[topic].append(problem)
    return render_template("index.html", categories=categories)

@main.route("/category/<topic>")
def category(topic):
    category_problems = [p for p in problems if p["topic"] == topic]
    return render_template("category.html", topic=topic, problems=category_problems)

@main.route("/problem/<int:id>")
def problem_detail(id):
    problem = next((p for p in problems if p["id"] == id), None)
    return render_template("problem.html", problem=problem)

@main.route("/glossary")
def glossary_page():
    return render_template("glossary.html", glossary=glossary)