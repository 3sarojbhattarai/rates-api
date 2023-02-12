from flask_restx import fields


def input_validation_error_model(api):
    return api.model(
        'input_validation_error_model',
        {
            'status': fields.String,
            'reason': fields.String
        }
    )


def error_model(api):
    return api.model(
        'error_model',
        {
            'status': fields.String,
            'reason': fields.String
        }
    )


def success_model(api, data_model=None, model_name='success_model', is_list=False):

    return api.model(
        model_name,
        {
            'status': fields.String,
            'reason': fields.String,
            'data': fields.Nested(data_model) if is_list is False else fields.List(fields.Nested(data_model))
        }
    )
