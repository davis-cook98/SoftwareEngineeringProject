from marshmallow import Schema, fields

#Schemas, may be updated later
class ArticleSchema(Schema):
    id = fields.Int(required=True)
    Title = fields.Str()
    Description = fields.Str()
    Published = fields.Str()
    Url = fields.Str()
    InsertTime = fields.DateTime()

class UserSchema(Schema):
    id = fields.Int(required=True)
    Username = fields.Str()
    Password = fields.Str()
    Favorites = fields.List(fields.Str())
