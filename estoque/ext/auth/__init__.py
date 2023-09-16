
from estoque.ext.auth import models  # noqa
from estoque.ext.auth.commands import list_users, add_user

from estoque.ext.db import db
from estoque.ext.auth.admin import UserAdmin
from estoque.ext.admin import admin
from estoque.ext.auth.models import User


def init_app(app):
    """TODO: inicializar flask simple login + JWT"""
    app.cli.command()(list_users)
    app.cli.command()(add_user)

    admin.add_view(UserAdmin(User, db.session))
