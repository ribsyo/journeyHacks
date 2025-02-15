from flask import Flask, render_template, request

import ai_api
from data_models import Location

app = Flask(__name__)
sfu_burnaby_location = Location(longitude=-122.9199, latitude=49.2781)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recommend", methods=["GET", "POST"])
def recommend():
    results = None  # Default is no results

    if request.method == "POST":
        query = request.form.get("query")

        # query is the response, use to get the value from the user input
        if query:
            results = [{"name": f"Best {query} Restaurant"}]

    return render_template("index.html", results=results)


if __name__ == "__main__":
    app.run(debug=True)
