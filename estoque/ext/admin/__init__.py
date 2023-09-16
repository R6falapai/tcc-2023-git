from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from estoque.ext.db import db
from estoque.ext.db.models import Category, Brands, Items

admin = Admin()


def init_app(app):
    admin.name = app.config.get("APPNAME", "Estoque Online")
    admin.template_mode = app.config.get("ADMIN_TEMPLATE_MODE", "bootstrap2")
    admin.init_app(app)


    admin.add_view(ModelView(Category, db.session))
    admin.add_view(ModelView(Brands, db.session))
    admin.add_view(ModelView(Items, db.session))

