"Default error handling module."
from flask import Blueprint, jsonify
from slib.json import SJson
from slib.log import SLog
from server.error.code import ErrCode, ErrMsg

handler = Blueprint('handler', __name__)

DEFAULT_HTTP_ERROR_CODE = 500

@handler.app_errorhandler(Exception)
def handle_all_exception(exp):
    '''Global error handler for all exceptions e.g. abort with 409 HTTP error code.'''

    SLog.error('Global error handler code: ' + str(exp.code))
    SLog.error('Global error handler message: ' + str(exp))

    return jsonify(SJson.make_error_json(ErrCode.UNKNOWN_ERROR,
        ErrMsg.UNKNOWN_ERROR)), DEFAULT_HTTP_ERROR_CODE

@handler.app_errorhandler(500)
def internal_server_error(exp):
    '''Global error handler for internal server error.'''

    SLog.error('Global error handler code: ' + str(exp.code))
    SLog.error('Global error handler message: ' + str(exp))

    return jsonify(SJson.make_error_json(ErrCode.INTERNAL_SERVER_ERROR,
        ErrMsg.INTERNAL_SERVER_ERROR)), DEFAULT_HTTP_ERROR_CODE

@handler.app_errorhandler(404)
def resource_not_found(exp):
    '''Global error handler for resource not found.'''

    SLog.error('Global error handler code: ' + str(exp.code))
    SLog.error('Global error handler message: ' + str(exp))

    return jsonify(SJson.make_error_json(ErrCode.RESOURCE_NOT_FOUND,
        ErrMsg.RESOURCE_NOT_FOUND)), DEFAULT_HTTP_ERROR_CODE

@handler.app_errorhandler(405)
def method_not_allowed(exp):
    '''Global error handler for method not allowed.'''

    SLog.error('Global error handler code: ' + str(exp.code))
    SLog.error('Global error handler message: ' + str(exp))

    return jsonify(SJson.make_error_json(ErrCode.METHOD_NOT_ALLOWED,
        ErrMsg.METHOD_NOT_ALLOWED)), DEFAULT_HTTP_ERROR_CODE
