""" Serving the app using wsgi """
from app import app


if __name__ == "__main__":
    app.run()
