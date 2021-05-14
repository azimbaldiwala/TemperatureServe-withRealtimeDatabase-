from flask import Flask, render_template, request, send_file
from scraper import get_values
import pandas as pd
import database
import os

app = Flask(__name__)



@app.route('/')
def index():
    t, h = get_values()
    if t == "Error" or h == "Error":
        return render_template('home_alert.html')
    return render_template('home.html', t=t, h=h)


@app.route('/download_data')
def download():
    return render_template('downloads.html')


@app.route('/download_data_send', methods=["POST"])
def download_send():
    try:
        is_jan = request.form['inlineCheckbox1']
    except:
        is_jan = 'null'

    try:
        is_feb = request.form['inlineCheckbox2']
    except:
        is_feb = 'null'

    try:
        is_mar = request.form['inlineCheckbox3']
    except:
        is_mar = 'null'

    try:
        is_apr = request.form['inlineCheckbox4']
    except:
        is_apr = 'null'

    try:
        is_may = request.form['inlineCheckbox5']
    except:
        is_may = 'null'

    try:
        is_jun = request.form['inlineCheckbox6']
    except:
        is_jun = 'null'

    try:
        is_july = request.form['inlineCheckbox7']
    except:
        is_july = 'null'

    try:
        is_aug = request.form['inlineCheckbox8']
    except:
        is_aug = 'null'

    try:
        is_sept = request.form['inlineCheckbox9']
    except:
        is_sept = 'null'

    try:
        is_oct = request.form['inlineCheckbox10']

    except:
        is_oct = 'null'

    try:
        is_nov = request.form['inlineCheckbox11']
    except:
        is_nov = 'null'

    try:
        is_dec = request.form['inlineCheckbox12']
    except:
        is_dec = 'null'

    months = [is_jan, is_feb, is_mar, is_apr, is_may, is_jun, is_july, is_aug, is_sept, is_oct, is_nov, is_dec]
    year = request.form['year']
    all_data = []
    for month in months:
        if month != 'null':
            data = database.get_data_by_month(month, year)
            all_data.append(data)

    # Access tuple with all_data[0][0]
    df = pd.DataFrame(all_data[0], columns=['temperature', 'Humidity', 'Time', 'Date', 'Month', 'Year'])
    df = df.set_index('temperature')
    #df.to_csv('data.csv')
    df.to_excel('data.xlsx')
    return send_file('data.csv', attachment_filename='data.csv', as_attachment=True )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
