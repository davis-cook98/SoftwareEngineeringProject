from ..Read.ReadMongo import ReadConnect
from ..Write.WriteMongo import WriteConnect
from .Schemas import ArticleSchema, UserSchema

class Service(object):
    def __init__(self, user_id, repo_client=ReadConnect(adapter=WriteConnect))
