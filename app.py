from flask import Flask 
from os import environ

app = Flask(__name__)



@app.route('/')
def index():
    env_var = environ.get('FLASK_SECRET')
    message = f"Hello Flask!, this is my openshift secret {env_var}"
    return message 

if __name__=="__main__":
    app.debug = True 
    app.run(host='0.0.0.0', port=8080)
