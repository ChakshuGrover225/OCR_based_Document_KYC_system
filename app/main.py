from app import flask_app               # updated import

if __name__ == "__main__":
    # Run Flask server
    flask_app.run(host='0.0.0.0', port=5000, debug=True)
