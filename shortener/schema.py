import graphene
from graphene_django import DjangoObjectType

from .models import URL


class URLType(DjangoObjectType):
    """A URL type linking the URL model"""

    class Meta:
        model = URL


class Query(graphene.ObjectType):
    """Query class containing list of URLTypes"""

    urls = graphene.List(URLType)

    def resolve_urls(self, info, **kwargs):
        return URL.objects.all()
