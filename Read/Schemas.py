from marshmallow import Schema, fields

#Schemas, may be updated later
class ArticleSchema(Schema):
    id = fields.Int(required=True)
    title = fields.Str()
    description = fields.Str()
    published = fields.DateTime()
    InsertTime = fields.DateTime()

class UserSchema(Schema):
    id = fields.Int(required=True)
    FirstName = fields.Str()
    LastName = fields.Str()
    Username = fields.Str()
    Password = fields.Str()
    LastLogin = fields.DateTime()

