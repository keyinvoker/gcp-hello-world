from app import api
from app.resources.Banana import Banana
from app.resources.Eggplant import Eggplant
from app.resources.InquiryTracker import InquiryTracker

api.add_resource(Banana, '/')
api.add_resource(Eggplant, '/eggplant')
api.add_resource(InquiryTracker, '/track')