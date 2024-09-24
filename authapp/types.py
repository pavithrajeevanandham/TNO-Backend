import graphene
from graphene_django.types import DjangoObjectType
from .models import *


class PaginatedType(graphene.ObjectType):
    page = graphene.Int()
    pages = graphene.Int()
    has_next = graphene.Boolean()
    has_prev = graphene.Boolean()


class UserType(DjangoObjectType):
    class Meta:
        model = CustomUser


class UserConnection(graphene.ObjectType):
    data = graphene.List(UserType)
    page = graphene.Field(PaginatedType)
