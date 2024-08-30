# myapp/mutations.py
import graphene
from .types import BookType
from .models import Book

class CreateBook(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        author = graphene.String(required=True)
        published_date = graphene.String(required=True)

    book = graphene.Field(BookType)

    def mutate(self, info, title, author, published_date):
        book = Book(title=title, author=author, published_date=published_date)
        book.save()
        return CreateBook(book=book)

class UpdateBook(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        title = graphene.String()
        author = graphene.String()
        published_date = graphene.String()

    book = graphene.Field(BookType)

    def mutate(self, info, id, title=None, author=None, published_date=None):
        book = Book.objects.get(pk=id)
        if title:
            book.title = title
        if author:
            book.author = author
        if published_date:
            book.published_date = published_date
        book.save()
        return UpdateBook(book=book)


# Add mutations to the schema
class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()
    update_book = UpdateBook.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
