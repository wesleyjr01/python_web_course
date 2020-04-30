from flask import Flask
from learning import learning_blueprint

app = Flask(__name__)

app.register_blueprint(learning_blueprint)

if __name__ == "__main__":
    app.run()
