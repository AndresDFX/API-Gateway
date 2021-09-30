from sanic import Sanic, response
from functions import *

app = Sanic(name='API_Rest_Sanic')

@app.route("/name/<name>")
def search_name_API(request, name, methods=['GET']):
   return response.json(search_name(name), status=200)

if __name__ == '__main__':
   app.run(host='127.0.0.1', port=5001, debug=True) 