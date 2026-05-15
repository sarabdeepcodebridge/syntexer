from flask import Blueprint, render_template
from app.problems import problems

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html", problems=problems)

@main.route("/problem/<int:id>")
def problem_detail(id):
    problem = next((p for p in problems if p["id"] == id), None)
    return render_template("problem.html", problem=problem)