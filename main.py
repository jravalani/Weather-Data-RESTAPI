from flask import Flask, render_template
import pandas as pd

app = Flask("__name__")

# important to store all .html files inside "templates" folder and images inside "static" folder
# @ indicates that the following line is a declarator, and it declares the .route() method to the home() function.


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def data(station, date):
    print(date)
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df["    DATE"] == date]["   TG"].squeeze() / 10
    return {'station': station,
            'date': date,
            'temperature': temperature}


if __name__ == "__main__":
    app.run(debug=True, port=5000)