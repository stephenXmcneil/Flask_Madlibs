from flask import Flask, render_template, request

from stories import story


app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

@app.route("/")
def create_input():
    """Generate and show form to ask words."""

    prompts = story.prompts
  
    return render_template("questions.html", prompts=prompts)


@app.route("/form")
def show_story():
    """Show story result."""
   
    text = story.generate(request.args)


    return render_template("form.html", text=text)