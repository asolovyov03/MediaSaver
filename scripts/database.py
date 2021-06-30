from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///database.db', echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String)

    def __repr__(self) -> str:
        return f"<User(name = {self.first_name}, last_name = {self.last_name}, username = {self.username}, telegram_id = {self.telegram_id}>"


class File(Base):
    __tablename__ = 'files'

    id = Column(Integer, primary_key=True)
    file_id = Column(String)  # file_id from Telegram API
    description = Column(String)
    file_extension = Column(String)
    file_name = Column(String)
    file_type = Column(String)

    def __repr__(self) -> str:
        return f'<File(id = {self.id}, name = {self.file_name}, file_type = {self.file_type}'


Base.metadata.create_all(engine)
