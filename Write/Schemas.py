from marshmallow import Schema, fields

#Schemas for our database collections
class ArticleSchema(Schema):
    _id = fields.Str()
    Title = fields.Str()
    Description = fields.Str()
    Published = fields.Str()
    Url = fields.Str()
    InsertTime = fields.DateTime()

class UserSchema(Schema):
    _id = fields.Str()
    Username = fields.Str()
    Password = fields.Str()
    Favorites = fields.List(fields.Str())
    Pushed = fields.List(fields.Str())
