ERRORS = {
    'INVALID_CREDENTIALS': {
        'error_code': 2001,
        'error_description': 'The username or password provided is incorrect.'
    },
    'MISSING_CREDENTIALS': {
        'error_code': 2002,
        'error_description': 'The username or password is missing.'
    },
    'ACCOUNT_SUSPENDED': {
        'error_code': 2002,
        'error_description': 'The account is suspended. Please contact support.'
    },
    'ACCESS_DENIED': {
        'error_code': 2003,
        'error_description': 'You do not have the necessary permissions to access this resource.'
    },
    'INVALID_DOCUMENT_TYPE': {
        'error_code': 2004,
        'error_description': 'The uploaded document type is not supported.'
    },
    'DOCUMENT_SIZE_EXCEEDED': {
        'error_code': 2005,
        'error_description': 'The uploaded document exceeds the maximum allowed size.'
    },
    'DOCUMENT_UPLOAD_FAILED': {
        'error_code': 2006,
        'error_description': 'Failed to upload the document. Please try again later.'
    },
    'GRANT_NOT_FOUND': {
        'error_code': 2007,
        'error_description': 'The specified grant could not be found.'
    },
    'APPLICATION_ALREADY_SUBMITTED': {
        'error_code': 2008,
        'error_description': 'An application for this grant has already been submitted.'
    },
    'REQUIRED_FIELDS_MISSING': {
        'error_code': 2009,
        'error_description': 'One or more required fields are missing.'
    },
    'INVALID_APPLICATION_STATUS': {
        'error_code': 2010,
        'error_description': 'The application status is invalid or cannot be changed at this stage.'
    },
    'USER_NOT_AUTHENTICATED': {
        'error_code': 2011,
        'error_description': 'You must be logged in to perform this action.'
    },
    'INSUFFICIENT_PERMISSIONS': {
        'error_code': 2012,
        'error_description': 'You do not have the necessary permissions to perform this action.'
    },
    'EMAIL_ALREADY_REGISTERED': {
        'error_code': 2013,
        'error_description': 'An account with this email address already exists.'
    },
    'USERNAME_ALREADY_TAKEN': {
        'error_code': 2014,
        'error_description': 'The username is already taken. Please choose a different one.'
    },
    'DATABASE_ERROR': {
        'error_code': 2015,
        'error_description': 'An error occurred while accessing the database. Please try again later.'
    },
    'NETWORK_ERROR': {
        'error_code': 2016,
        'error_description': 'A network error occurred. Please try again later.'
    },
    'INVALID_API_REQUEST': {
        'error_code': 2017,
        'error_description': 'The API request is invalid. Please check the request format and try again.'
    },
    'SERVER_ERROR': {
        'error_code': 2222,
        'error_description': 'A server error occured.'
    },
    'SESSION_EXPIRED': {
        'error_code': 2019,
        'error_description': 'Your session has expired. Please log in again.'
    },
    'AUDIT_LOG_FAILURE': {
        'error_code': 2020,
        'error_description': 'Failed to record the action in the audit log.'
    },
    'LOGIN_FAILED': {
        'error_code': 2020,
        'error_description': 'Login failed. Please check your credentials and try again.'
    },
    'USER_ACCOUNT_ISSUE': {
        'error_code': 2021,
        'error_description': 'Your account has an issue. Please contact support.'
    },
}

def get_error_response(error_name):
    """
    Get the error response for a given error name.
    
    :param error_name: The name of the error as defined in the ERRORS dictionary
    :return: A dictionary with the error code and error_description
    """
    error = ERRORS.get(error_name, ERRORS['SERVER_ERROR'])  
    return {
        'error_code': error['error_code'],
        'error_message': error['error_description']
    }
