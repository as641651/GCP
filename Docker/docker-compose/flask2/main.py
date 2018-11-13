from flask import Flask

import redis

r = redis.Redis(host='redis-server')
r.set('visits',0)

app = Flask(__name__)
app.debug=True

@app.route('/')
def index():
    v = r.get('visits')
    r.set('visits',int(v)+1)
    out = "<h1>Hi Flask2. <a href='http://localhost:4000'>Link</a></h1>"
    out += "<p>Visits : " + str(int(v))  + "</p>"
    return out

if __name__ == '__main__':
   app.run(host='0.0.0.0',port=8000)
