from flask import render_template_string
from app import app
import markdown
from app.ai import ask_ai
from app.wiki import get_random_wiki_title, get_detailed_wiki

@app.route("/")
def home():
    title = get_random_wiki_title()
    details = get_detailed_wiki(title)
    summary = ask_ai(details)

    md_text = f"""### AI summarized random Wiki article:

## {title}

{summary}
"""

    html = markdown.markdown(md_text)

    return render_template_string("""
        <html>
            <body>{{ html|safe }}</body>
        </html>
    """, html=html)
