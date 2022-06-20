from flask import Flask, render_template, request
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


if __name__ == '__main__':
    billingdb = mysql.connector.connect(
        host="billingdb",
        user="root",
        password="1234!",
        database='billdb',
    )
    # connectdb = True
    # counter = 60 
    # while connectdb:
    #     counter -= 1
    #     time.sleep(1)
    #     if counter == 0:
    #         break
    #     try:
    #         billingdb = mysql.connector.connect(
    #             host="billingdb",
    #             user="root",
    #             password="1234!",
    #             database='billdb',
    #         )
    #         mycursor = billingdb.cursor()
    #         connectdb = False
    #     except:
    #         connectdb = True
    # print(billingdb)
    app.run(debug=True, host='0.0.0.0', port=5000)