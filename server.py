from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)


@app.route('/')
def route():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data: dict):
    with open("database.txt", "a") as database_file:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        database_file.writelines(f'\n{email}, {subject}, {message}')


def write_to_csv(data: dict):
    with open("database.csv", mode="a", newline='') as database_csv:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(
            database_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


def write_to_csv_dict(data: dict):
    with open("database.csv", mode="a", newline='') as database_csv:
        field_names = ['email', 'subject', 'message']
        csv_writer = csv.DictWriter(
            database_csv, fieldnames=field_names, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(data)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
        # write_to_file(data)
            write_to_csv(data)
        # write_to_csv_dict(data)
        return redirect('/thank_you.html')
        except:
            'Did not save to database'
    else:
        return 'something went wrong'
