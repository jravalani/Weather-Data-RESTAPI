from flask import Flask, render_template

app = Flask("__name__")

# important to store all .html files inside "templates" folder and images inside "static" folder
# @ indicates that the following line is a declarator, and it declares the .route() method to the home() function.


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def data(station, date):
    temperature = 23
    return {'station': station,
            'date': date,
            'temperature': temperature}


if __name__ == "__main__":
    app.run(debug=True)