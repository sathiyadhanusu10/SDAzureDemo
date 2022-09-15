from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "https://docs.microsoft.com/en-us/training/modules/migrate-app-service-migration-assistant/"
