import socket
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return """
    <h1>My Flask in Docker</h1>
    <p>Sample web flask app running in docker</p>
    """
if __name__== '__main__':
    app.run(host= socket.gethostname(),port=5000)