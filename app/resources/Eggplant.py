from flask_restful import Resource

class Eggplant(Resource):
    def get(self):
        return {'get': '🍆🍆🍆'}

    def post(self):
        return {'post': '💜💜💜'}