from flask import Flask, render_template

app = Flask(__name__)
app.debug = True
app.env = "development"


@app.route("/", strict_slashes=False)
def index():
    return 'Hello World'

if __name__ == "__main__":
    app.run()
