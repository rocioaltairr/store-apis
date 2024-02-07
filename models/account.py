from db import db

class AccountModel(db.Model):
    __tablename__ = "accounts"

    id = db.Column(db.Integer, primary_key=True)
    actor = db.Column(db.String(80), unique=False, nullable=False)
    name = db.Column(db.String(80), unique=True, nullable=False)
    user_name = db.Column(db.String(80), unique=True, nullable=False)

    code = db.Column(db.String(80), unique=False, nullable=False)

    items = db.relationship("ItemModel", back_populates="account", lazy="dynamic")
