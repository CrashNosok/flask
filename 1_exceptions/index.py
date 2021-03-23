from flask import Flask, request, render_template, url_for

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
    tasks = [
        'сделать 1',
        'сделать 2',
        'сделать 3',
        'сделать 4',
        'сделать 5',
    ]

    return render_template('index.html', tasks=tasks)


if __name__ == '__main__':
    app.run(debug=True)
