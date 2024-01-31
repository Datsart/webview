import time
import webview
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
template_folder = os.path.join(current_dir, 'templates')

app = Flask(__name__, template_folder=template_folder)
absolute_path = '/Users/artemdatsenko/PycharmProjects/webview/database.db'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{absolute_path}'
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
        else:
            message = "Ошибка: логин и пароль обязательны для заполнения"
    return render_template('form_1.html', message=message)


if __name__ == '__main__':
    import create_db

    with app.app_context():
        db.create_all()
    webview.create_window('Login', app)
    webview.start()
