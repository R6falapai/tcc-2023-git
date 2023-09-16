from flask_admin.contrib.sqla import ModelView
from flask_admin.actions import action
from flask_admin.contrib.sqla import filters
from estoque.ext.auth.models import User
from estoque.ext.db import db
from flask import flash, Markup


def format_user(self, request, user, *args):
    user.email = user.email.partition("@")[0]
    return user.email


# def format_user_passwd(self, request, user, *args):
#     user.passwd = user.passwd = '*'
#     return user.passwd


class UserAdmin(ModelView):
    """Interface admin de user"""

    # column_formatters = {"email": format_user,
    #                      #  "passwd": format_user_passwd
    #                      }

    column_formatters = {
        "email": lambda s, r, u, *a: Markup(f'<b>{u.email.split("@")[0]}</b>')
    }
    column_list = ["email", "admin"]

    column_searchable_list = ["email"]

    column_filters = [
        "email",
        "admin",
        filters.FilterLike(
            User.email,
            "dominio",
            options=(("gmail", "Gmail"), ("uol", "UOL"))
        )
    ]

    can_edit = False
    can_create = True
    can_delete = True

    @action(
        'toggle_admin',
        'Toggle Admin status',
        'Are you sure?'
    )
    def toggle_admin_status(self, ids):
        users = User.query.filter(User.id.in_(ids)).all()
        for user in users:
            user.admin = not user.admin
        db.session.commit()
        flash(f"{len(users)}Usuarios alterados com sucesso!!", "success")

    @action(
        'send_email',
        'Send email to all users',
        'Are you sure?'
    )
    def send_email(self, ids):
        users = User.query.filter(User.id.in_(ids)).all()
        # 1) redirect para m form para escrever a mensagem do email
        # 2) enviar email
        flash(f"{len(users)}emails enviados com sucesso!!", "success")
