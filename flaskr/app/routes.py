from flask import render_template, jsonify
from app import app
from app.wiki import get_random_wiki_title, get_detailed_wiki
from app.ai import ask_ai
import markdown

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/article")
def article():
    title = get_random_wiki_title()
    details = get_detailed_wiki(title)
    summary = ask_ai(details)
    summary_html = markdown.markdown(summary)
    return render_template("article.html", title=title, summary=summary_html)
