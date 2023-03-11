import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": animal}],
            max_tokens=300,
            temperature=0.9,
        )
        print(response)
        return redirect(url_for("index", result=response.choices[0].message.content))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(animal):
    return """The following is a conversation with ChatGPT. ChatGPT is friendly and helpful.

Human: {}
ChatGPT:""".format(
        animal.capitalize()
    )
