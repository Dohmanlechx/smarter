from flask import Flask, render_template_string
from ai import ask_ai
import markdown

app = Flask(__name__)

@app.route("/")
def home():
    ai_text = ask_ai()

    md_text = f"""{ai_text}"""
    html = markdown.markdown(md_text)

    return render_template_string("""
        <html>
            <body>{{ html|safe }}</body>
        </html>
    """, html=html)

if __name__ == "__main__":
    app.run(debug=True)
