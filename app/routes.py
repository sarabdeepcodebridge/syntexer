from flask import Blueprint, render_template, jsonify, request
from app.problems import all_problems
from app.problems.glossary import glossary

main = Blueprint("main", __name__)

@main.route("/")
def index():
    categories = {}
    for problem in all_problems:
        topic = problem["topic"]
        if topic not in categories:
            categories[topic] = []
        categories[topic].append(problem)
    return render_template("index.html", categories=categories, problems_count=len(all_problems))

@main.route("/category/<topic>")
def category(topic):
    category_problems = [p for p in all_problems if p["topic"] == topic]
    return render_template("category.html", topic=topic, problems=category_problems)

@main.route("/problem/<int:id>")
def problem_detail(id):
    problem = next((p for p in all_problems if p["id"] == id), None)
    if not problem:
        return render_template("404.html"), 404
    return render_template("problem.html", problem=problem)

@main.route("/glossary")
def glossary_page():
    return render_template("glossary.html", glossary=glossary)

@main.route("/search")
def search():
    query = request.args.get("q", "").lower()
    if not query:
        return render_template("search.html", results=[], query="")
    results = [p for p in all_problems if
               query in p["title"].lower() or
               query in p["topic"].lower() or
               query in p["difficulty"].lower()]
    return render_template("search.html", results=results, query=query)

# API endpoints
@main.route("/api/problems")
def api_problems():
    return jsonify(all_problems)

@main.route("/api/problems/<int:id>")
def api_problem(id):
    problem = next((p for p in all_problems if p["id"] == id), None)
    if not problem:
        return jsonify({"error": "Not found"}), 404
    return jsonify(problem)

@main.route("/api/categories")
def api_categories():
    categories = {}
    for problem in all_problems:
        topic = problem["topic"]
        if topic not in categories:
            categories[topic] = []
        categories[topic].append(problem["id"])
    return jsonify(categories)
