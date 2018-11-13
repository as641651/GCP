from flask import Flask
#Edited this file in container
app = Flask(__name__)
app.debug=True

@app.route('/')
def index():
    return "<h1>Hi</h1>"

if __name__ == '__main__':
   app.run(host='0.0.0.0',port=8000)
