# from fastapi import Depends
# from ..shemas.aticle import ArticleShema
from .....application.persistences.article_persistency import ArticlePersistency
# from sqlalchemy.orm import Session


class ArticleRepository(ArticlePersistency):
    # def __init__(self, session: Session = Depends()):
    #     self.session = session

    def list(self) -> str:
        return "test"
        # self.session.query(ArticleShema).all()
