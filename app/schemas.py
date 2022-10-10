from marshmallow import fields

from app import ma
from app.models import Inquiry, InquiryDetails

class InquirySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Inquiry
        ordered = True

class InquiryDetailsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = InquiryDetails
        ordered = True

class InquiryTrackerResponse(ma.SQLAlchemyAutoSchema):
    nik = fields.String()
    status = fields.String()
    response = fields.Raw()

    class Meta:
        ordered = True