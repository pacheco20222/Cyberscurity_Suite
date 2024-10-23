from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()
print(f"SECRET_KEY from env: {os.getenv('SECRET_KEY')}")

# Get the absolute path to the project's root directory
basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
dotenv_path = os.path.join(basedir, '.env')

# Load the .env file
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
    print(f"Loaded .env from {dotenv_path}")  # Debugging print
else:
    raise RuntimeError(f"Could not find .env file at {dotenv_path}")

def create_app():
    app = Flask(__name__)

    from .routes import main
    app.register_blueprint(main)

    # Set the secret key from the .env file
    secret_key = os.getenv('SECRET_KEY')
    if not secret_key:
        raise RuntimeError("SECRET_KEY not found in the environment!")
    
    app.secret_key = secret_key
    print(f"Loaded SECRET_KEY: {secret_key}")  # Debugging purpose

    return app