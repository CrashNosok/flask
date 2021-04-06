## План урока:
1. __проверка дз__
обязательно должны быть написаны функции:
```
def get_task_index_by_id(file, id)
def delete_task_by_id(file, id)
```
2.  __делаем, чтобы функции были написаны правильно__
3. __рассказываем про redirect__
4. __делаем удаление при нажатии на крестик:__
html:
```
<a class="remove" href="/tasks/del/{{ task[0] }}">X</a>
```
py:
```
@app.route('/tasks/del/<int:id>')
def del_task(id):
    csv_functions.delete_task_by_id('db.csv', id)
    # redirect - перенаправить на страницу (параметр - путь до страницы)
    return redirect(url_for('tasks'))
```

4. __GET/POST запросы__
рассказываем что такое, как отличаются, где используются и зачем нужны
5. __рассказываем про form в html__
```
<!-- 
    action - куда отправить запрос
    method - тип запроса (обычно GET или POST)
-->
<form id="todo-add" action="{{ url_for('create_task') }}" method="POST">
    <!-- name - ключ для POST запроса -->
    <input name="description" type="text" id="new-todo-description" class="form-control"/>
    <button class="add" type="submit">+</button>
</form>
```
можно после этого попробовать отправить запрос. так как нет view, мы увидим POST запрос только в консоле.
6. __пишем view__
пишем дополнительные функции для сохранения task (как пару ```[id, description]```):
```
def get_last_id(file):
    tasks = read_rows_from_csv(file)
    return int(tasks[-1][0])


def create_task(file, description):
    id = get_last_id(file) + 1
    task = [id, description]
    tasks = read_rows_from_csv(file)
    # добавили свой task ко всем
    tasks.append(task)
    write_rows_to_csv(file, tasks)

```

добавляем доступный метод во view:
```@app.route('/tasks/create', methods=['POST'])```

рассказываем как определить метод запроса:
```if request.method == 'POST':```

рассказываем, что ключи из формы указываются в ```name``` и что они доступны в коде через ```request.form```

Пишем саму view
```
@app.route('/tasks/create', methods=['POST'])
def create_task():
    # проверить метод запроса:
    if request.method == 'POST':
        # request.form - объект, который хранит в себе все ключи полученного запроса
        description = request.form['description']
        csv_functions.create_task('db.csv', description)
    return redirect(url_for('tasks'))

```
