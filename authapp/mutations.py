# myapp/mutations.py
import graphene
from .types import *
from .models import *


class CreateUser(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        author = graphene.String(required=True)
        published_date = graphene.String(required=True)

    user = graphene.Field(UserType)

    def mutate(self, info, title, author, published_date):
        user = CustomUser(title=title, author=author, published_date=published_date)
        user.save()
        return CreateUser(user=user)


class UpdateUser(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        title = graphene.String()
        author = graphene.String()
        published_date = graphene.String()

    article = graphene.Field(UserType)

    def mutate(self, info, id, title=None, author=None, published_date=None):
        user = CustomUser.objects.get(pk=id)
        if title:
            user.title = title
        if author:
            user.author = author
        if published_date:
            user.published_date = published_date
        user.save()
        return UpdateUser(user=user)


# Add mutations to the schema
class Mutation(graphene.ObjectType):
    create_article = CreateUser.Field()
    update_article = UpdateUser.Field()


# schema = graphene.Schema(query=Query, mutation=Mutation)
