from flask_restful import Resource

class Banana(Resource):
    def get(self):
        return {'get': '🍌🍌🍌'}

    def post(self):
        return {'post': '💛💛💛'}