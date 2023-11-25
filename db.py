from sqlalchemy import create_engine, Column, Integer, String, BigInteger, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine('postgresql://postgres:111213@localhost/exam', echo=True)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    user_id = Column(BigInteger, unique=True)
    username = Column(String)
    created_at = Column(String)

    def __init__(self, first_name, last_name, user_id, username, created_at):
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.username = username
        self.created_at = created_at

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __repr__(self):
        return f'{self.user_id}: {self.full_name}\n{self.chat_name}'


class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey('users.id'))
    message = Column(Text)
    chat_id = Column(BigInteger)
    chat_name = Column(String)
    created_at = Column(String)

    def __init__(self, user_id, message, chat_id, chat_name, created_at):
        self.user_id = user_id
        self.message = message
        self.chat_id = chat_id
        self.chat_name = chat_name
        self.created_at = created_at


# Base.metadata.create_all(engine)
