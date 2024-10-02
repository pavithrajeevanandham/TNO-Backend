# myapp/mutations.py
import graphene
from .types import *
from .models import *


class CreateArticle(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        author = graphene.Int(required=True)
        summary = graphene.String(required=True)
        image = graphene.String(required=True)
        keywords = graphene.String(required=True)
        status = graphene.Int(required=True)
        sub_title = graphene.String()
        published_date = graphene.String(required=True)
        
    article = graphene.Field(ArticleType)

    def mutate(self, info, title, author, published_date):
        article = Article(title=title, author=author, published_date=published_date)
        article.save()
        return CreateArticle(article=article)


class UpdateArticle(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        title = graphene.String()
        author = graphene.String()
        published_date = graphene.String()

    article = graphene.Field(ArticleType)

    def mutate(self, info, id, title=None, author=None, published_date=None):
        article = Article.objects.get(pk=id)
        if title:
            article.title = title
        if author:
            article.author = author
        if published_date:
            article.published_date = published_date
        article.save()
        return UpdateArticle(article=article)


# Add mutations to the schema
class Mutation(graphene.ObjectType):
    create_article = CreateArticle.Field()
    update_article = UpdateArticle.Field()


# schema = graphene.Schema(query=Query, mutation=Mutation)
