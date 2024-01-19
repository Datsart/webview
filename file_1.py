import webview
import sys
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.serving import run_simple

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users_info_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class DB(db.Model):
    __tablename__ = 'users_info_table'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)


@app.route('/', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username and password:
            log_info = DB(username=username, password=password)
            db.session.add(log_info)
            db.session.commit()
            message = "Данные успешно сохранены в БД"
            return redirect(url_for('login'))

        else:
            message = "Ошибка: логин и пароль обязательны для заполнения"

    return render_template('form_1.html', message=message)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    # app.run(host='localhost', port=5050, debug=True)
    webview.create_window('Login', app)
    webview.start()