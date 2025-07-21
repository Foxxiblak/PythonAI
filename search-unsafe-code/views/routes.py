from flask import Blueprint, render_template, request
from models.api import get_response
from static.scripts.classifier import vulnerabilities

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/search', methods=['GET', 'POST'])
def search():
    if(request.method == 'POST'):
        type_vul = request.form['vulnerabilities']
        results = get_response(int(type_vul))
        return render_template('search.html', results=results, selected_value=type_vul, vulnerabilities=vulnerabilities)
    else:
        return render_template('search.html', vulnerabilities=vulnerabilities)

@main.route('/contacts')
def contacts():
    return render_template('contacts.html')