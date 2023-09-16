import click
from estoque.ext.db import db
from estoque.ext.auth.models import User


def list_users():
    users = User.query.all()
    for usuarios in users:
        posicao = usuarios.admin
        if posicao == True:
            click.echo(f"Administradores cadastrados são {usuarios}")
        else:
            click.echo(f"lista de usuarios {usuarios}")


@click.option("--email", "-e")
@click.option("--passwd", "-p")
@click.option("--admin", "-a", is_flag=True, default=False)
def add_user(email, passwd, admin):
    """Adiciona novo usuario"""
    user = User(
        email=email,
        passwd=passwd,
        admin=admin
    )

    db.session.add(user)
    try:
        db.session.commit()
        if admin == True:
            click.echo(f"Administrador {email} cadastrado com sucesso!!")
        else:
            click.echo(f"Usuario {email}, Criado com Sucesso!!")

    except:
        click.echo("Deu Ruim")
        return False
