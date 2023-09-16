import click
from estoque.ext.db import db
from estoque.ext.db import models  # noqa


def init_app(app):

    @app.cli.command()
    def create_db():
        """Este comando inicializa o DB"""
        db.create_all()

    @app.cli.command()
    def listar_pedidos():
        click.echo("lista de pedidos")
