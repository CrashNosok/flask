## План урока:
1. __проверка дз__
2.  __Работа с sqlite через sqlalchemy__
Для урока использовал видео:
https://www.youtube.com/watch?v=PAKJpfxeXjc
3. __Подготовка окружения__
SQLite: https://sqlitebrowser.org/dl/
установка sqlalchemy: ```pip install sqlalchemy```

4. __Создание базы:__
Импорты для урока (даём постепенно)
```
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
```
Подключение к базе и получение базового класса для создания класса моделей:
```
engine = create_engine('sqlite:///database.db', echo=False)
base = declarative_base()
```
создание модели:
```
class User(base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String) 
    def __repr__(self):
        return f'<User ({self.id} {self.name} {self.fullname})>'
```
отправляем модель в базу и получаем объект сессии для выполнения запросов в БД:
```
base.metadata.create_all(engine)
session = sessionmaker(bind=engine)()
```

4. __Запросы к БД:__

запросы к БД для внесения данных
```
# Создание объекта класса
user_ivan = User(name='Ivan', fullname='Ivanov')
print(user_ivan.name)

# id не доступен (так как объект ещё не в базе)
print(user_ivan.id)

# возвращает список объектов, которые уйдут в БД при коммите
print(session.new) 
# добавление объекта в сессию
session.add(user_ivan)
print(session.new) 
# отправляем объект в базу
session.commit()
# id теперь появился
print(user_ivan.id)

# добавление сразу нескольких объектов (списком)
# session.add_all([User(name='Bob', fullname='Bobovich'), User(name='John', fullname='Smith')])
# session.commit()
```

запросы к БД для получения данных
```
# обращения к базе не происходит (рассказываем что сессия у нас ленивая)
# в примере ниже показывается, что можно использовать несколько фильтров друг за другом
q = session.query(User).filter_by(name='Ivan').filter_by(fullname='Ivanov')

# обращение к базе только во время считывания 
# сколько объектов вернул запрос
print(q.count())
# получить первый объект
other_ivan = q.first()
# print(other_ivan)
# посметреть все объекты по-очереди (показываем, что циклом можно пробежаться по всем объектам сразу)
# for user in q:
#     print(user)

print(other_ivan)
# session.dirty - показывает список объектов из БД, которые были изменены (не новые
#   объекты, а измененные)
print(session.dirty)
other_ivan.fullname = 'Sidorov'
print(session.dirty)
# если хотим, чтобы изменения сохранились, не забываем коммитить сессию
```

Удаление объектов из БД
```
# 1 способ удаления
# удалит объект сразу (мы его даже посмотреть не сможем)
q = session.query(User).filter_by(name='Ivan').delete()
session.commit()

# 2 способ удаления
# получили нужные нам объекты
q = session.query(User).filter_by(name='Ivan2')
# достали только первый из них
user = q.first()
print(user)
# удаляем этот объект
session.delete(user)
session.commit()
```

P.S. Скорее всего весь этот материал не получится уместить в 1 урок. поэтому можно опустить некоторые детили (session.new, session.dirty... так же в файле sql_alch.py есть информация о выполнении прямых sql запросов к безе, откат сессии и методе get(). Это тоже можно опустить)

5. __Практика:__
1) создать базу данных users, где для каждого пользователя будут поля id, username, email
2) создать базу данных tasks
В базе данных должны быть поля user_id, text, priority
user_id - id пользователя, которому принадлежит таск 
priority - приоритет таска (от 0 до 2 будет)
3) добавить в БД с пользователями трёх любых пользователей, а в БД с тасками любые 15 задач (каждая задача привязана к конкретному пользователю)
4) вывести с помощью запросов к БД все задачи первого и последнего пользователя

ответ на практику можно найти в файле db.py
