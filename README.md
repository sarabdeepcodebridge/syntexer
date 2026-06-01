# Syntaxer — Python to Java Interview Companion

A web platform helping developers perform confidently in Java interviews without learning Java from scratch.

## What's inside
- 60 problems across 5 categories (Arrays, Strings, Loops, Math, Sorting)
- Side-by-side Python and Java solutions with syntax highlighting
- Key differences, pseudocode, and plain English explanations
- Python → Java glossary (35 terms)
- Search functionality
- Progress tracking (localStorage)
- REST API endpoints
- Premium dark UI

## Data structure
Problems stored in `app/problems/problems.json` — easy to edit, no database needed.
To add a problem: open the JSON file, add a new object, save, push.

## Running locally
```bash
pip install -r requirements.txt
python run.py
```
Visit `http://127.0.0.1:5000`

## API
- `GET /api/problems` — all problems
- `GET /api/problems/<id>` — single problem
- `GET /api/categories` — categories with problem ids

## Deployment
Render.com — connect GitHub repo, auto-deploys on push.

## Company
17719019 Canada Inc. 🍁
