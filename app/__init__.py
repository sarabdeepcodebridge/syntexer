from flask import Flask
import json, os

def create_app():
    app = Flask(__name__)

    @app.context_processor
    def inject_globals():
        problems_path = os.path.join(app.root_path, 'problems', 'problems.json')
        with open(problems_path) as f:
            problems = json.load(f)
        categories = {}
        for p in problems:
            t = p['topic']
            if t not in categories:
                categories[t] = {'easy':0,'medium':0,'hard':0,'total':0,'problems':[]}
            categories[t][p['difficulty'].lower()] += 1
            categories[t]['total'] += 1
            categories[t]['problems'].append(p['id'])
        return dict(categories=categories, total_problems=len(problems))

    from .routes import main
    app.register_blueprint(main)
    return app
