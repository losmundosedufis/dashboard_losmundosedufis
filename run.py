from app import create_app

gunicorn_app = create_app()

if __name__ == "__main__":
    gunicorn_app.run(debug=True)