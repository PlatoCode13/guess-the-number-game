from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        try:
            guess = int(request.form["guess"])
            secret = random.randint(1, 10)
            if guess == secret:
                message = f"🎉 Correct! The number was {secret}."
            else:
                message = f"❌ Wrong! You guessed {guess}, but it was {secret}."
        except ValueError:
            message = "Please enter a valid number."

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
