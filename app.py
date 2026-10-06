from flask import Flask, render_template, request
from generator import generate_business_idea

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        category = request.form["category"]
        budget = request.form["budget"]
        skills = request.form["skills"]
        target = request.form["target"]
        location = request.form["location"]

        idea = generate_business_idea(
            category, budget, skills, target, location
        )

        return render_template("result.html", idea=idea)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)