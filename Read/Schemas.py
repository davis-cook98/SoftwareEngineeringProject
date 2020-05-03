from marshmallow import Schema, fields

#Schemas, may be updated later
class ArticleSchema(Schema):
    id = fields.Int(required=True)
    Title = fields.Str()
    Description = fields.Str()
    Published = fields.Str()
    InsertTime = fields.Date()
    favorited = fields.Str()

class UserSchema(Schema):
    id = fields.Int(required=True)
    FirstName = fields.Str()
    LastName = fields.Str()
    Username = fields.Str()
    Password = fields.Str()
    LastLogin = fields.Date()

