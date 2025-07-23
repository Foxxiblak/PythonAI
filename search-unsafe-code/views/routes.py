from flask import Blueprint, render_template, request
from models.owasp_parser import get_title, about, get_donate_link, get_contact
from models.db import Vulnerability
from sqlalchemy.future import select
from db import SessionLocal
from models.api import get_response

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')


@main.route('/search', methods=['GET', 'POST'])
def search():
    with SessionLocal() as session:
        result = session.execute(select(Vulnerability))
        vulnerabilities = result.scalars().all()

    if(request.method == 'POST'):
        type_vul = request.form['vulnerabilities']
        results = get_response(int(type_vul))
        return render_template('search.html', results=results, selected_value=type_vul, vulnerabilities=vulnerabilities)
    else:
        return render_template('search.html', vulnerabilities=vulnerabilities)

@main.route('/contacts', methods=['GET'])
def contacts():
    return render_template('contacts.html', contacts={'title': get_title(), 'about': about(), 'donate': get_donate_link(), 'contacts': get_contact()})