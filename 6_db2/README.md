## План урока:
1. __проверка дз__
2.  __Рассказываем то, что не рассказали в предыдущем уроке__
3. __Отношения в БД:__

рассказываем какие бывают отношения в БД:
1 к 1
1 ко многим
многие ко многим

4. __Импорт классов__

В файле db.py оставляем только определение классов и нужные импорты. после этого импортируем их в index.py
```
from db import User, Task
```

Добавляем библиотеки для работы с БД в index.py
```
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
```

5. __Практика__

В файле index.py поменять всю логику таким образом, чтобы вместо csv БД использовалась sqlite + sqlalchemy

так же, сделаем небольшой костыль: так как у нас нет логина пользователей. 
объявим переменную ID и будем использовать её как id залогиненного пользователя
```
ID = 1
```
то есть сейчас, чтобы получить пользователя, нужно прописать:
```
user = session.query(User).get(ID)
```

пример с функцией для удаления таксов:
было:
```
@app.route('/tasks/del/<int:id>')
def del_task(id):
    csv_functions.delete_task_by_id('db.csv', id)
    return redirect(url_for('tasks'))
```
стало:
```
@app.route('/tasks/del/<int:id>')
def del_task(id):
    task = session.query(Task).get(id)
    session.delete(task)
    session.commit()
    return redirect(url_for('tasks'))
```
ребята могут сказать, что такой код позволяет удалять такси любого пользователя (а это небезопасно) в таком случае можно этот код заменить:
```
@app.route('/tasks/del/<int:id>')
def del_task(id):
    task = session.query(Task).filter_by(user_id=ID).get(id)
    # тут можно добавить проверку, if task is not None
    session.delete(task)
    session.commit()
    return redirect(url_for('tasks'))
```

по такому принципу нужно поменять все функции
6. __Отправка сообщений на почту (SMTP сервер)__
Рассказываем, если осталось время

документация: https://pythonhosted.org/Flask-Mail/

импорты:
```
from flask_mail import Mail, Message
```

объект для отправки писем
```
app = Flask(__name__)
mail = Mail(app)
```

настройки для работы с почтой
```
app.config['MAIL_SERVER'] = 'smtp.mail.ru'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'ваш_емейл@mail.ru'
app.config['MAIL_PASSWORD'] = 'ваш_пароль_от_почты'
app.config['MAIL_DEFAULT_SENDER'] = 'ваш_емейл@mail.ru'
```

пример отправки сообщения:
```
@app.route('/')
def index():
    mail.init_app(app)
    msg = Message("Hello",
                  sender="ваш_емейл@mail.ru",
                  recipients=["емейл_получателя@mail.ru"])
    # 1 параметр - тема сообщения
    # sender - указать отправителя
    # recipients - список emal'ов, на которые уйдут письма
    
    msg.body = "тело письма (то, что будет написано внутри письма) лалала!!"

    # отправить сообщение
    mail.send(msg)
    return 'Сообщение было отправлено!!'
```
