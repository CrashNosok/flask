from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

engine = create_engine('sqlite:///database.db', echo=True)
base = declarative_base()
class User(base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String) 
    def __repr__(self):
        return f'<User ({self.name} {self.fullname})>'

base.metadata.create_all(engine)
session = sessionmaker(bind=engine)()

user_ivan = User(name='Ivan', fullname='Ivanov')

# print(user_ivan.name)

# print(user_ivan.id)
# session.add(user_ivan)
# print(session.new) 
# session.commit()
# print(user_ivan.id)

# обращения к базе не происходит 
q = session.query(User).filter_by(name='Ivan')

# обращение к базе только во время считывания 
print(q.count())
other_ivan = q.first()
print(other_ivan)

# session.add_all([User(name='Bob', fullname='Bobovich'), User(name='John', fullname='Smith')])
# session.commit()

# print(session.dirty)
# other_ivan.fullname = 'Sidoriv'
# print(session.dirty)

s = session.execute('SELECT * FROM USERS WHERE name="John"')
print(s.first())

# session.delete(other_ivan)
# session.commit()

user_alice = User(name='Alice', fullname='Linch')
session.add(user_alice)
print(session.new)
session.rollback()
print(session.new)

# a = session.query(User).get(1)
# print(a)
