from tortoise.models import Model
from tortoise import fields

class Todo(Model):
    id = fields.IntField(pk=True)
    title = fields.TextField()
    description  = fields.TextField()
    
    