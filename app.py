from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/form", methods=["POST", "GET"])
def form():
    # display specific information about the stock element
    # if request.method == 'POST':
    #     return
    return render_template("form.html")


if __name__ == "__main__":
    app.run(debug=True)
