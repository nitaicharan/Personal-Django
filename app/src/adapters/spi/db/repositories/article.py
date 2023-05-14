from sqlmodel import Session, select
from app.src.adapters.spi.db.models.article import ArticleModel
from app.src.application.persistences.article import ArticlePersistency
from app.src.entities.article import ArticleEntity
from .schema import engine


class ArticleRepository(ArticlePersistency):
    async def list(self):
        with Session(engine) as session:
            statement = select(ArticleModel)
            results = session.exec(statement)
            articles = results.all()
            session.close()
            return articles

    async def add(self, entity: ArticleEntity):
        with Session(engine) as session:
            model = ArticleModel.from_entity(entity)
            session.add(model)
            session.commit()
            entity = model.to_entity()
            session.close()
            return entity

    async def find(self, id: int):
        with Session(engine) as session:
            statement = select(ArticleModel).where(ArticleModel.id == id)
            entity = session.exec(statement).one()
            session.close()
            return entity
