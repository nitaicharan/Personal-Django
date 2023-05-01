from app.src.adapters.spi.db.repositories.schema import SessionLocal
from app.src.adapters.spi.db.tables.aticle import ArticleTable
from app.src.application.persistences.article_persistency import ArticlePersistency

class ArticleRepository(ArticlePersistency):
    async def list(self):
        db = SessionLocal()
        return db.query(ArticleTable).all()
