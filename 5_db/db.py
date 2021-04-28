from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm.session import sessionmaker

# engine = create_engine('sqlite:///database.db', echo=False)
base = declarative_base()

class User(base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    def __repr__(self):
        return f'<User ({self.id} {self.username} {self.email})>'

class Task(base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    text = Column(String)
    priority = Column(Integer)
    def __repr__(self):
        return f'<Task ({self.user_id} {self.text} {self.priority})>'

# base.metadata.create_all(engine)
# session = sessionmaker(bind=engine)()

# session.add_all([
#     User(username='Bob', email='lalala@mail.ru'), 
#     User(username='John', email='Smith@gmail.com'),
#     User(username='Ivan', email='ivan@mail.ru'),
# ])

# session.add_all([
#     Task(user_id=1, text='помыть пол', priority=0),
#     Task(user_id=1, text='сделать уроки', priority=0),
#     Task(user_id=1, text='пропылесосить квартиру', priority=0),
#     Task(user_id=2, text='прочитать книгу', priority=0),
#     Task(user_id=2, text='позвонить в школу', priority=0),
#     Task(user_id=2, text='поспать', priority=0),
#     Task(user_id=3, text='поесть', priority=0),
#     Task(user_id=3, text='покормить кота', priority=0),
#     Task(user_id=3, text='сделать ужин', priority=0),
#     Task(user_id=3, text='помыться', priority=0),
# ])
# session.commit()

# name = input('введите Ваше имя: ')
# user = session.query(User).filter_by(username=name).first()
# if user is not None:
#     tasks = session.query(Task).filter_by(user_id=user.id)
#     for task in tasks:
#         print(task)
