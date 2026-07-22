from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chickens")
@app.route("/chiikawa")
def chickens():
    return render_template("chickens.html")

@app.route("/pandas")
def pandas():
    return render_template("pandas.html")

@app.route("/butterflies")
@app.route("/izna")
def butterflies():
    return render_template("butterflies.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5678)
