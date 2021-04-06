from flask import Flask, request, render_template, url_for, redirect
import csv_functions

app = Flask(__name__)


@app.route('/')
@app.route('/about/')
def index():
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
    csv_functions.delete_task_by_id('db.csv', id)
    # redirect - перенаправить на страницу (параметр - путь до страницы)
    return redirect(url_for('tasks'))


@app.route('/tasks/create', methods=['POST'])
def create_task():
    # проверить метод запроса:
    if request.method == 'POST':
        # request.form - объект, который хранит в себе все ключи полученного запроса
        description = request.form['description']
        csv_functions.create_task('db.csv', description)
    return redirect(url_for('tasks'))


if __name__ == '__main__':
    app.run(debug=True)
