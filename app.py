from flask import Flask, render_template

app = Flask(__name__)

name = "Elba Zurita"

@app.route("/")
def hello_world():
    return render_template('index.html', person=name)

if __name__ == "__main__":
    app.run(debug=True)