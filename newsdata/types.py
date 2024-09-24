import graphene
from graphene_django.types import DjangoObjectType
from .models import *
from authapp.models import *


class PaginatedType(graphene.ObjectType):
    page = graphene.Int()
    pages = graphene.Int()
    has_next = graphene.Boolean()
    has_prev = graphene.Boolean()


class ArticleType(DjangoObjectType):
    class Meta:
        model = Article


class ArticleConnection(graphene.ObjectType):
    data = graphene.Field(ArticleType)
    page = graphene.Field(PaginatedType)


class ArticleStatusType(DjangoObjectType):
    class Meta:
        model = ArticleStatus


class ArticleStatusConnection(graphene.ObjectType):
    data = graphene.Field(ArticleStatusType)


class UserType(DjangoObjectType):
    class Meta:
        model = CustomUser


class UserConnection(graphene.ObjectType):
    data = graphene.Field(UserType)
    page = graphene.Field(PaginatedType)
