from flask import Flask, render_template
import pandas as pd

app = Flask("__name__")

stations = pd.read_csv("data_small/stations.txt", header=0, skiprows=17)
stations = stations[["STAID", "STANAME                                 "]][0:100]
stations = stations.to_html()

# important to store all .html files inside "templates" folder and images inside "static" folder
# @ indicates that the following line is a declarator, and it declares the .route() method to the home() function.


@app.route("/")
def home():
    return render_template("home.html", data=stations, )


@app.route("/api/v1/<station>/<year>")
def year_data(station, year):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    station_df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    station_df['YEAR'] = station_df['    DATE'].dt.year
    station_df = station_df.loc[station_df['YEAR'] == int(year)]
    result = station_df.to_dict(orient="records")
    # OR
    # result = station_df.loc[station_df['    DATE'].dt.year == int(year)].to_dict(orient="records")
    return result


@app.route("/api/v1/<station>/<date>")
def data(station, date):
    print(date)
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df["    DATE"] == date]["   TG"].squeeze() / 10
    return {'station': station,
            'date': date,
            'temperature': temperature}


@app.route("/api/v1/<station>")
def station_data(station):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    station_df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    result = station_df.to_dict(orient="records")
    return result


if __name__ == "__main__":
    app.run(debug=True, port=5000)