from flask_restful import Resource
from providers.post_provider import PostProvider

class Posts(Resource):
    def __init__(self, post_provider = None):
        if not post_provider:
            self.post_provider = PostProvider()
        else:
            self.post_provider = post_provider

    route = "/post"

    def get(self):
        posts = self.post_provider.get_posts()
        if len(posts) == 0:
            return {"message": "No posts found"}, 404
        return {"all_posts": posts}

class Post(Resource):
    route = "/post/<int:post_id>"
    def get(self, post_id):
        return {"post": post_id}

class Pioneer(Resource):
    route = "/pioneer"
    def get(self):
        return {'we': 'out here'}