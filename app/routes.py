from flask import Blueprint, render_template, send_file, Response, make_response, request
from .functions import generate_data
from io import BytesIO
import pandas as pd

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    return render_template('index.html')


@main.route('/datasets')
def datasets():
    return render_template('datasets.html')


@main.route('/download_excel', methods=['POST'])
def download_excel():
    rows = request.form['rows']
    # print(number_of_rows)
    df = generate_data(int(rows))
    # print(df)
    df.to_excel('app/static/generated_data/cardiac_patients/data.xlsx', index=False)
    response = make_response(open('app/static/generated_data/cardiac_patients/data.xlsx', 'rb').read())
    response.headers.set('Content-Type', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response.headers.set('Content-Disposition', 'attachment', filename='fake_cardiac_patients.xlsx')
    return response
