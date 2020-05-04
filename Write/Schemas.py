from marshmallow import Schema, fields

#Schemas, may be updated later
class ArticleSchema(Schema):
    id = fields.Str(required=True)
    title = fields.Str()
    description = fields.Str()
    published = fields.DateTime()
    InsertTime = fields.DateTime()
    favorited = fields.Str()

class UserSchema(Schema):
    id = fields.Str(required=True)
    Username = fields.Str()
    Password = fields.Str()
    Favorites = fields.List(fields.Str())
