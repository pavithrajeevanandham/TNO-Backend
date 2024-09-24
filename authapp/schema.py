import graphene
from .types import *
from .models import *


class Query(graphene.ObjectType):
    users = graphene.List(UserConnection, user_id=graphene.Int())

    def resolve_users(self, info):
        queryset = CustomUser.objects.all()

        return UserConnection(data=queryset)


schema = graphene.Schema(query=Query)

