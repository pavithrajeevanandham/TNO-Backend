import newsdata.schema
import authapp.schema
import graphene
import newsdata.mutations
import authapp.mutations


class Query(newsdata.schema.Query, authapp.schema.Query, graphene.ObjectType):
    pass


class Mutation(newsdata.mutations.Mutation, authapp.mutations.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
