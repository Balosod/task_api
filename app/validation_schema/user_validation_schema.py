from marshmallow import Schema, fields, validate, ValidationError

class SignupValidationSchema(Schema):
    username = fields.Str(required=True, validate=validate.Length(min=4, max=25))
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=8))
    
    def validate(self, data, **kwargs):
        errors = {}
        if errors:
            raise ValidationError(errors)
        return super().validate(data, **kwargs)
    

class LoginValidationSchema(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True)
    
    def validate(self, data, **kwargs):
        errors = {}
        if errors:
            raise ValidationError(errors)
        return super().validate(data, **kwargs)
