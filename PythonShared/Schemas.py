from marshmallow import Schema, fields

class ArticleSchema(Schema):
    id = fields.int(required=True)
    title = fields.Str()
    description = fields.Str()

class UserSchema(Schema):
    id = fields.int(required=True)
    FirstName = fields.Str()
    LastName = fields.Str()
    Username = fields.Str()
    Password = fields.Str()
    LastLogin = fields.DateTime()

