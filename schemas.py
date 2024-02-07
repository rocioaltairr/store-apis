from marshmallow import Schema, fields

class PlainItemSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    stock = fields.Int(required=True)

class PlainAccountSchema(Schema):
    id = fields.Int(dump_only=True)
    actor = fields.Str()
    name = fields.Str()
    user_name = fields.Str()
    code = fields.Str()

class ItemSchema(PlainItemSchema):
    account_id = fields.Int(required=True, load_only=True)
    account = fields.Nested(PlainAccountSchema(), dump_only=True)

class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()
    stock = fields.Int()

class AccountSchema(PlainAccountSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)



#########

class PlainSaleItemSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    stock = fields.Int(required=True)

class PlainStoreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()

class SaleItemSchema(PlainSaleItemSchema):
    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)

class SaleItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()
    stock = fields.Int()

class StoreSchema(PlainStoreSchema):
    saleitems = fields.List(fields.Nested(PlainSaleItemSchema()), dump_only=True)