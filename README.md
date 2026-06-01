# Syntaxer — Python to Java Interview Companion

A web platform that helps developers who know Python perform confidently in Java technical interviews — without learning Java from scratch.

## Features
- 50 interview problems across 5 categories
- Side-by-side Python and Java solutions
- Syntax highlighting with Prism.js
- Key differences explained in plain English
- Pseudocode for every problem
- Python → Java glossary (30 terms)
- Search functionality
- Progress tracking
- REST API endpoints
- Premium dark UI

## Categories
- Arrays (10 problems)
- Strings (10 problems)
- Loops (10 problems)
- Math (10 problems)
- Sorting (10 problems)

## Tech Stack
- Python 3.x
- Flask
- Jinja2 Templates
- Bootstrap 5
- Prism.js

## Running Locally
```bash
pip install -r requirements.txt
python run.py
```

Visit `http://127.0.0.1:5000`

## API Endpoints
- `GET /api/problems` — all problems
- `GET /api/problems/<id>` — single problem
- `GET /api/categories` — all categories

## Deployment
Deployed on Render. Live at [syntaxer.live](https://syntaxer.live)

## Company
17719019 Canada Inc. — Built in Canada 🍁
