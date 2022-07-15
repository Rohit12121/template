import csv
from lib2to3.pgen2.token import NEWLINE
from flask import Flask, redirect, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def wbIntro():
    renderingHtml = render_template(
        'index.html')
    return renderingHtml


@app.route('/<string:page_name>')
def htmlpage(page_name):
    return render_template(page_name)


def storingInformation(data):
    with open('database.csv', mode='a', newline='') as mydatabasefile:
        email = data['email']
        counting = data['counting']
        checkbox = data['checkbox']
        message = data['message']
        allDictKeys = ['email', 'counting', 'checkbox', 'message']
        writer = csv.DictWriter(mydatabasefile, fieldnames=allDictKeys)
        writer.writerow({'email': email, 'counting': counting,
                        'checkbox': checkbox, 'message': message})


@app.route('/submit_form', methods=['POST', 'GET'])
def formSubmmiting():
    if request.method == 'POST':
        data = request.form.to_dict()
        storingInformation(data)
        print(data)
        return redirect('/thank_you.html')
    else:
        return 'something went wrong'
