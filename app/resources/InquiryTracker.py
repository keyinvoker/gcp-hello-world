from flask_restful import Resource
from flask import request

from app import session
from app.models import Inquiry, InquiryDetails
from app.schemas import InquiryTrackerResponse

class InquiryTracker(Resource):
    def get(self):
        id = int(request.args['id'])
        inquiry = session.query(Inquiry).filter_by(id=id).first()
        inquiry_details = session.query(InquiryDetails).filter_by(inquiry_id=id).order_by(InquiryDetails.id).all()
        if inquiry is not None:
            requester = inquiry.requester
            if requester=='-':
                requester = '(does not want to be emailed)'
            inquiry_details = InquiryTrackerResponse(many=True).dump(inquiry_details)
            return [{'requester':requester, 'inquiry_id': id, 'inquiry_details': inquiry_details}]