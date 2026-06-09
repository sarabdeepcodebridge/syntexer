from flask import Blueprint, render_template, request, jsonify, abort
import json, os

main = Blueprint('main', __name__)

def load_problems():
    path = os.path.join(os.path.dirname(__file__), 'problems', 'problems.json')
    with open(path) as f:
        return json.load(f)

@main.route('/')
def index():
    problems = load_problems()
    return render_template('index.html', problems=problems)

@main.route('/category/<topic>')
def category(topic):
    problems = load_problems()
    diff_filter = request.args.get('difficulty', 'all')
    cat_problems = [p for p in problems if p['topic'] == topic]
    if diff_filter != 'all':
        cat_problems = [p for p in cat_problems if p['difficulty'].lower() == diff_filter]
    return render_template('category.html', problems=cat_problems, topic=topic, diff_filter=diff_filter)

@main.route('/problem/<int:problem_id>')
def problem(problem_id):
    problems = load_problems()
    prob = next((p for p in problems if p['id'] == problem_id), None)
    if not prob:
        abort(404)
    cat_problems = [p for p in problems if p['topic'] == prob['topic']]
    ids = [p['id'] for p in cat_problems]
    idx = ids.index(problem_id)
    prev_id = ids[idx-1] if idx > 0 else None
    next_id = ids[idx+1] if idx < len(ids)-1 else None
    return render_template('problem.html', problem=prob, prev_id=prev_id, next_id=next_id)

@main.route('/search')
def search():
    q = request.args.get('q', '').lower()
    problems = load_problems()
    results = []
    if q:
        for p in problems:
            if q in p['title'].lower() or q in p['topic'].lower() or q in p['difficulty'].lower():
                results.append(p)
    return render_template('search.html', results=results, query=q)

@main.route('/glossary')
def glossary():
    return render_template('glossary.html')

@main.route('/api/problems')
def api_problems():
    return jsonify(load_problems())

@main.route('/api/problems/<int:pid>')
def api_problem(pid):
    problems = load_problems()
    p = next((p for p in problems if p['id'] == pid), None)
    if not p: abort(404)
    return jsonify(p)

@main.route('/api/categories')
def api_categories():
    problems = load_problems()
    cats = {}
    for p in problems:
        if p['topic'] not in cats:
            cats[p['topic']] = []
        cats[p['topic']].append(p['id'])
    return jsonify(cats)

@main.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404
