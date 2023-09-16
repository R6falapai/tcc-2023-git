

def init_app(app):
    @app.before_first_request  # Trigger
    def init_everything():
        print("Estou iniciando")
