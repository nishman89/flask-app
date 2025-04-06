from app import create_app

# Create an instance of the Flask application
app = create_app()

if __name__ == '__main__':
    """
    Starts the Flask application on localhost at port 5000.
    Debug mode is enabled for easier development.
    """
    app.run(debug=True)
