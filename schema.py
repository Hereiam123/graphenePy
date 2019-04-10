import graphene
import json
from datetime import datetime


class User(graphene.ObjectType):
    id = graphene.ID()
    username = graphene.String()
    created_at = graphene.DateTime()


class Query(graphene.ObjectType):
    hello = graphene.String()
    is_admin = graphene.Boolean()
    users = graphene.List(User, limit=graphene.Int())

    def resolve_hello(self, info):
        return "world"

    def resolve_is_admin(self, info):
        return True

    def resolve_users(self, info, limit):
        return[
            User(id="1", username="Fred", created_at=datetime.now()),
            User(id="2", username="Fred2", created_at=datetime.now()),
            User(id="3", username="Fred3", created_at=datetime.now())
        ][:limit]


schema = graphene.Schema(query=Query)

result = schema.execute(
    '''
    {
        users(limit: 1){
            id
            username
            createdAt
        }
    }
    '''
)

dictResult = dict(result.data.items())
print(json.dumps(dictResult, indent=2))
