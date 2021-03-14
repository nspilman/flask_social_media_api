from flask import Flask
from flask_restful import Api
from controllers.PostController import Post, Posts

app = Flask(__name__)
api = Api(app)

routes = [
    Post,
    Posts
]

for route in routes:
    api.add_resource(route, route.route)

if __name__ == '__main__':
    app.run(debug=True)