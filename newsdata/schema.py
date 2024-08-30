import graphene
from .types import *
from .models import *


class Query(graphene.ObjectType):
    articles = graphene.List(ArticleConnection, article_id=graphene.Int())

    def resolve_articles(self, info):
        queryset = Article.objects.all()

        return ArticleConnection(data=queryset)


schema = graphene.Schema(query=Query)
