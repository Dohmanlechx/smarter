from flask import render_template, request, jsonify
from .ai import ask_ai
from .wiki import get_random_wiki_title, get_detailed_wiki, get_image_urls
import markdown
import time

request_times = {}
LIMIT = 10      # max requests
WINDOW = 30     # seconds

def init_routes(app):
    @app.route("/")
    def home():
        return render_template("home.html")

    @app.route("/article")
    def article():
        user_ip = request.remote_addr
        now = time.time()
        timestamps = request_times.get(user_ip, [])
        timestamps = [t for t in timestamps if now - t < WINDOW]

        if len(timestamps) >= LIMIT:
            retry_after = WINDOW - (now - timestamps[0])
            return render_template("limiter.html", retry_after=int(retry_after))

        timestamps.append(now)
        request_times[user_ip] = timestamps

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
