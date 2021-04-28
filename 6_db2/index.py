from flask import Flask, request, render_template, url_for, redirect
import csv_functions
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from db import User, Task
# отправка писем:
from flask_mail import Mail, Message


app = Flask(__name__)
# объект для отправки писем
mail = Mail(app)

# настройки для работы с почтой
app.config['MAIL_SERVER'] = 'smtp.mail.ru'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'riocrash3@mail.ru'
app.config['MAIL_PASSWORD'] = 'OurTestPassword'
app.config['MAIL_DEFAULT_SENDER'] = 'riocrash3@mail.ru'


ID = 1
engine = create_engine('sqlite:///database.db', echo=False)
session = sessionmaker(bind=engine)()


@app.route('/')
@app.route('/about/')
def index():
    mail.init_app(app)
    msg = Message("Hello",
                  sender="riocrash3@mail.ru",
                  recipients=["riocrash@mail.ru"])
    # 1 параметр - тема сообщения
    # sender - указать отправителя
    # recipients - список emal'ов, на которые уйдут письма
    msg.body = "тело письма (то, что будет написано внутри письма) лалала!!"
    # отправить сообщение
    mail.send(msg)
    return 'Hello world'
    

# параметры строки:
# синтаксис:
# <тип_данных:название_переменной>
# название_переменной - должно быть в параметрах функции
@app.route('/user/<string:name>/<int:age>/')
def user_info(name, age):
    return f'имя: {name}; возраст: {age}'


'''
по пути /taks/
должен открываться файл index.html
со стилями style.css
'''
@app.route('/tasks/')
def tasks():
    tasks = csv_functions.read_rows_from_csv('db.csv')
    return render_template('index.html', tasks=tasks)


@app.route('/tasks/del/<int:id>')
def del_task(id):
    # csv_functions.delete_task_by_id('db.csv', id)
    # redirect - перенаправить на страницу (параметр - путь до страницы)
    task = session.query(Task).get(id)
    session.delete(task)
    session.commit()
    return redirect(url_for('tasks'))


@app.route('/tasks/create', methods=['POST'])
def create_task():
    # проверить метод запроса:
    if request.method == 'POST':
        # request.form - объект, который хранит в себе все ключи полученного запроса
        description = request.form['description']
        csv_functions.create_task('db.csv', description)
    return redirect(url_for('tasks'))


@app.route('/tasks/edit/<int:id>', methods=['GET', 'POST'])
def edit_task(id):
    task = csv_functions.get_task_index_by_id('db.csv', id)
    if request.method == 'POST':
        rows = csv_functions.read_rows_from_csv('db.csv')
        for row in rows:
            if int(row[0]) == id:
                row[1] = request.form['description']
                break
        csv_functions.write_rows_to_csv('db.csv', rows)
        return redirect(url_for('tasks'))
    else:
        return render_template('edit_task.html', task=task)


if __name__ == '__main__':
    app.run(debug=True)
