from application_configuration.app import app
from routes.database_routes import database_bp
from routes.user_routes import user_bp
from routes.hacker_routes import hacker_bp

app.register_blueprint(database_bp)
app.register_blueprint(user_bp)
app.register_blueprint(hacker_bp)

if __name__ == "__main__":
    app.run(debug=True, port=8888)
