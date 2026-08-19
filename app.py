from flask import Flask, render_template

app = Flask(__name__)

name = "Cansona"

@app.route("/")
def hello_world():
    return render_template('index.html', person=name)

@app.route("/actividad")
def actividad():
    return render_template( 'ejercicioClase.html')


if __name__ == "__main__":
    app.run(debug=True)