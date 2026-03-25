from flask import Blueprint, render_template, request, redirect, url_for
from .models import House
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    houses = House.query.all()
    return render_template('index.html', houses=houses)

@main.route('/add', methods=['GET', 'POST'])
def add_house():
    if request.method == 'POST':
        title = request.form['title']
        location = request.form['location']
        price = request.form['price']
        description = request.form['description']

        new_house = House(
            title=title,
            location=location,
            price=price,
            description=description
        )

        db.session.add(new_house)
        db.session.commit()

        return redirect(url_for('main.index'))

    return render_template('add_house.html')

@main.route('/contact')
def contact():
    return render_template('contact.html')
