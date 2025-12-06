from flask import render_template
from .ai import ask_ai
from .wiki import get_random_wiki_title, get_detailed_wiki, get_image_urls
import markdown

def init_routes(app):
    @app.route("/")
    def home():
        return render_template("home.html")

    @app.route("/article")
    def article():
        try:
            title = get_random_wiki_title()
            details = get_detailed_wiki(title)
            images = get_image_urls(title)
            summary = ask_ai(details)
            summary_html = markdown.markdown(summary)

            return render_template(
                "article.html",
                title=title,
                summary=summary_html,
                images=images,
                page_url=f"https://en.wikipedia.org/wiki/{title}"
            )
        except Exception as e:
            return render_template("error.html", message=str(e))