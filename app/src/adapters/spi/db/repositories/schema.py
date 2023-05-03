from sqlmodel import SQLModel, create_engine

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(
    url=SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    echo=True,
)

SQLModel.metadata.create_all(engine)
