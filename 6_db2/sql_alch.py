from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

engine = create_engine('sqlite:///database.db', echo=False)
base = declarative_base()

class User(base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String) 
    def __repr__(self):
        return f'<User ({self.id} {self.name} {self.fullname})>'

base.metadata.create_all(engine)
session = sessionmaker(bind=engine)()

# запросы к БД для внесения данных
'''
# user_ivan = User(name='Ivan', fullname='Ivanov')

# print(user_ivan.name)

# print(user_ivan.id)
# возвращает список объектов, которые уйдут в БД при коммите
# print(session.new) 
# session.add(user_ivan)
# print(session.new) 
# session.commit()
# print(user_ivan.id)
'''

# запросы к БД для получения данных
'''
# обращения к базе не происходит 
q = session.query(User).filter_by(name='Ivan').filter_by(fullname='Ivanov')

# обращение к базе только во время считывания 
# print(q.count())
other_ivan = q.first()
# print(other_ivan)
# посметреть все объекты по-очереди
# for user in q:
#     print(user)

# session.add_all([User(name='Bob', fullname='Bobovich'), User(name='John', fullname='Smith')])
# session.commit()

print(other_ivan)
# session.dirty - показывает список объектов из БД, которые были изменены (не новые
#   объекты, а измененные)
print(session.dirty)
other_ivan.fullname = 'Sidorov'
print(session.dirty)
'''

# Прямые SQL запросы в БД
'''
# * читайте ПДО (защита от SQL инъекций) *
# s = session.execute('SELECT * FROM USERS WHERE name="John"')
# print(s.first())
'''


# удаление из БД
'''
# удаляет объект из таблицы
# 1 способ удаления
# q = session.query(User).filter_by(name='Ivan').delete()
# session.commit()

# 2 способ удаления
# q = session.query(User).filter_by(name='Ivan2')
# user = q.first()
# print(user)
# session.delete(user)
# session.commit()
'''


# откат сессии
'''
user_alice = User(name='Alice', fullname='Linch')
session.add(user_alice)
print(session.new)
# можно откатить сессию назад (убрать из неё последнее добавление)
session.rollback()
print(session.new)
'''

# возвращает 1 объект. параметром get является id в БД
a = session.query(User).get(6)
print(a)
