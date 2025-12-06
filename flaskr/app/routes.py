from flask import render_template
from app.ai import ask_ai
import wiki
import markdown

def init_routes(app):
    @app.route("/")
    def home():
        return render_template("home.html")

    @app.route("/article")
    def article():
        title = wiki.get_random_wiki_title()
        details = wiki.get_detailed_wiki(title)
        images = wiki.get_image_urls(title)
        summary = ask_ai(details)
        summary_html = markdown.markdown(summary)

        return render_template(
            "article.html",
            title=title,
            summary=summary_html,
            images=images,
            page_url=f"https://en.wikipedia.org/wiki/{title}"
        )
