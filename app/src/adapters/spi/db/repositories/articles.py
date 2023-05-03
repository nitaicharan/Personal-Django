from sqlmodel import Session, select
from app.src.adapters.spi.db.models.aticle import ArticleModel
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
            session.close()
