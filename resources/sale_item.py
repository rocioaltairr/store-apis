from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import StoreModel
from models import SaleItemModel
from schemas import SaleItemSchema, SaleItemUpdateSchema

blp = Blueprint("SaleItems", "SaleItems", description="Operations on sale items")


@blp.route("/saleitem/<string:store_id>")
class Item(MethodView):
    @blp.response(200, SaleItemSchema)
    def get(self, store_id):
        saleitem = SaleItemModel.query.get_or_404(store_id)
        return saleitem

    def delete(self, store_id):
        saleitem = SaleItemModel.query.get_or_404(store_id)
        db.session.delete(saleitem)
        db.session.commit()
        return {"message": "Sale Item deleted."}

    @blp.arguments(SaleItemUpdateSchema)
    @blp.response(200, SaleItemSchema)
    def put(self, item_data, store_id):
        saleitem = SaleItemModel.query.get(store_id)
        if not saleitem:
            return {"message": "Sale Item not found."}, 404
        # Update the sale item fields
        saleitem.price = item_data.get("price", saleitem.price)
        saleitem.name = item_data.get("name", saleitem.name)
        saleitem.stock = item_data.get("stock", saleitem.stock)

        # Commit changes to the database
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {"message": "Failed to update Sale Item.", "error": str(e)}, 500

        return saleitem
    
@blp.route("/saleitem/<string:store_id>/<string:item_id>")
class Item(MethodView):

    @blp.arguments(SaleItemUpdateSchema)
    @blp.response(200, SaleItemSchema)
    def put(self, item_data, store_id, item_id):
        saleitem = SaleItemModel.query.filter(SaleItemModel.id == item_id, SaleItemModel.store_id == store_id).first()
        if not saleitem:
            return {"message": "Sale Item not found."}, 404
        # Update the sale item fields
        saleitem.price = item_data.get("price", saleitem.price)
        saleitem.name = item_data.get("name", saleitem.name)
        saleitem.stock = item_data.get("stock", saleitem.stock)

        # Commit changes to the database
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {"message": "Failed to update Sale Item.", "error": str(e)}, 500

        return saleitem


@blp.route("/saleitem")
class ItemList(MethodView):
    @blp.response(200, SaleItemSchema(many=True))
    def get(self):
        return SaleItemModel.query.all()

    @blp.arguments(SaleItemSchema)
    @blp.response(201, SaleItemSchema)
    def post(self, item_data):
        item = SaleItemModel(**item_data)

        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the item.")

        return item
