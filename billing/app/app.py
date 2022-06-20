from flask import Flask, render_template, request
from GET_health import GET_health
import mysql.connector
import time

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="billing",
#   password="billing"
# )

# print(mydb)


app = Flask(__name__)

@app.route('/')
# @app.route('/index')
def index():
    return render_template('index.html')

@app.route("/health", methods=['GET','POST'])
def health():
    return GET_health()

if __name__ == '__main__':
    # billingdb = mysql.connector.connect(
    #     host="billingdb",
    #     user="root",
    #     password="1234!",
    #     database='billdb',
    # )
    app.run(debug=True, host='0.0.0.0', port=5000)