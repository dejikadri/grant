MESSAGES = {
    'ACCOUNT_CREATED': {
        'Message': 'Your account has been successfully created.'
    },
    'LOGON_SUCCESSFUL': {
        'Message': 'You have successfully logged in.'
    },
    'LOGOUT_SUCCESSFUL': {
        'Message': 'You have successfully logged out.'
    },
    'GRANT_CREATED': {
        'Message': 'The grant has been successfully created.'
    },
    'APPLICATION_SUBMITTED': {
        'Message': 'Your application has been successfully submitted.'
    },
    'APPLICATION_UPDATED': {
        'Message': 'Your application status has been successfully updated.'
    },
    'DOCUMENT_UPLOADED': {
        'Message': 'The document has been successfully uploaded.'
    },
    'PROFILE_UPDATED': {
        'Message': 'Your profile has been successfully updated.'
    },
    'PASSWORD_CHANGED': {
        'Message': 'Your password has been successfully changed.'
    },
    'EMAIL_VERIFIED': {
        'Message': 'Your email address has been successfully verified.'
    },
    'NOTIFICATION_SENT': {
        'Message': 'The notification has been sent successfully.'
    },
    'GRANT_DELETED': {
        'Message': 'The grant has been successfully deleted.'
    },
    'ACCOUNT_VERIFIED': {
        'Message': 'Your account has been successfully verified.'
    },
    'APPLICATION_WITHDRAWN': {
        'Message': 'Your application has been successfully withdrawn.'
    },
    'EMAIL_UPDATED': {
        'Message': 'Your email address has been successfully updated.'
    },
    'ROLE_ASSIGNED': {
        'Message': 'The role has been successfully assigned.'
    },
    'AUDIT_LOG_CREATED': {
        'Message': 'The action has been successfully recorded in the audit log.'
    },
    'DATA_EXPORT_INITIATED': {
        'Message': 'The data export has been successfully initiated.'
    },
    'GRANT_PUBLISHED': {
        'Message': 'The grant has been successfully published.'
    },
    'COMMENT_ADDED': {
        'Message': 'The comment has been successfully added.'
    },
    'USER_CREATED': {
        'Message': 'The user has been successfully created.'
    },
    'USER_UPDATED': {
        'Message': 'The user has been successfully updated.'
    },
    'USER_DELETED': {
        'Message': 'The user has been successfully deleted.'
    },
}

def get_message(message_name):
    return MESSAGES.get(message_name, )
