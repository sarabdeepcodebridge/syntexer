from flask import Blueprint, render_template, jsonify, request
import json
import os

main = Blueprint("main", __name__)

def load_problems():
    path = os.path.join(os.path.dirname(__file__), 'problems', 'problems.json')
    with open(path, 'r') as f:
        return json.load(f)

def load_glossary():
    path = os.path.join(os.path.dirname(__file__), 'problems', 'glossary.json')
    with open(path, 'r') as f:
        return json.load(f)

@main.route("/")
def index():
    problems = load_problems()
    categories = {}
    for p in problems:
        t = p["topic"]
        if t not in categories:
            categories[t] = []
        categories[t].append(p)
    return render_template("index.html", categories=categories, problems_count=len(problems))

@main.route("/category/<topic>")
def category(topic):
    problems = load_problems()
    cat_problems = [p for p in problems if p["topic"] == topic]
    return render_template("category.html", topic=topic, problems=cat_problems)

@main.route("/problem/<int:id>")
def problem_detail(id):
    problems = load_problems()
    problem = next((p for p in problems if p["id"] == id), None)
    if not problem:
        return render_template("404.html"), 404
    total = len(problems)
    return render_template("problem.html", problem=problem, total=total)

@main.route("/glossary")
def glossary_page():
    glossary = load_glossary()
    return render_template("glossary.html", glossary=glossary)

@main.route("/search")
def search():
    problems = load_problems()
    query = request.args.get("q", "").lower()
    if not query:
        return render_template("search.html", results=[], query="")
    results = [p for p in problems if
               query in p["title"].lower() or
               query in p["topic"].lower() or
               query in p["difficulty"].lower()]
    return render_template("search.html", results=results, query=query)

@main.route("/api/problems")
def api_problems():
    return jsonify(load_problems())

@main.route("/api/problems/<int:id>")
def api_problem(id):
    problems = load_problems()
    problem = next((p for p in problems if p["id"] == id), None)
    if not problem:
        return jsonify({"error": "Not found"}), 404
    return jsonify(problem)

@main.route("/api/categories")
def api_categories():
    problems = load_problems()
    categories = {}
    for p in problems:
        t = p["topic"]
        if t not in categories:
            categories[t] = []
        categories[t].append(p["id"])
    return jsonify(categories)
