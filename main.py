from flask import Flask, render_template_string
import logging
import markdown
from ai import ask_ai
from wiki import random_wiki_title, detailed_wiki

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    # Get random Wikipedia title
    title = random_wiki_title()
    logging.info(f"Random title: {title}")

    # Get detailed Wiki content
    detailed = detailed_wiki(title)

    # Ask AI to summarize
    final = ask_ai(detailed)

    # Combine into a single Markdown string
    md_text = f"""
### AI summarized random Wiki article:

## {title}

{final}
"""

    # Convert Markdown to HTML
    html = markdown.markdown(md_text)

    # Render HTML in Flask
    return render_template_string("""
        <html>
            <body>{{ html|safe }}</body>
        </html>
    """, html=html)

if __name__ == "__main__":
    app.run(debug=True)
