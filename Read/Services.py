from .ReadMongo import ReadConnect
from .Schemas import ArticleSchema, UserSchema

class Service(object):
    def __init__(self, user_id, repo_client=ReadConnect):
        self.repo_client = repo_client
        self.user_id = user_id

        if not user_id:
            raise Exception("user id not provided")

    def find_all_kudos(self):
        kudos = self.repo_client.find_all({'user_id': self.user_id})
        return [self.dump(kudo) for kudo in kudos]

    def find_kudo(self, repo_id):
        kudo = self.repo_client.find({'user_id': self.user_id, 'repo_id': repo_id})
        return self.dump(kudo)

    def create_kudo_for(self, ReadConnect):
        self.repo_client.create(self.prepare_kudo(ReadConnect))
        return self.dump(ReadConnect.data)

    def update_kudo_with(self, repo_id, ReadConnect):
        records_affected = self.repo_client.update({'user_id': self.user_id, 'repo_id': repo_id}, self.prepare_kudo(ReadConnect))
        return records_affected > 0

    def delete_kudo_for(self, repo_id):
        records_affected = self.repo_client.delete({'user_id': self.user_id, 'repo_id': repo_id})
        return records_affected > 0

    def dump(self, data):
        return ArticleSchema(exclude=['_id']).dump(data).data

    def prepare_kudo(self, ReadConnect):
        data = ReadConnect.data
        data['user_id'] = self.user_id
        return data
