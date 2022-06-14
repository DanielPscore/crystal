from flask import Flask, request, Response
app = Flask(__name__)
import datetime
app = Flask(__name__)


@app.route("/time", methods=['GET'])
def get_any():
    return str(datetime.datetime.now())


@app.route('/', methods=['GET', 'POST'])
def upload_file():

    return '''
    <h1>HELLO CRYSTAL</h1>

    '''

if __name__ == "__main__":
    app.run(debug=True)