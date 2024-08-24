from users.models import User
# from ..common import error as err
from common import error as err

def check_user_exists(email):
    """
    Check if a user with the given email address exists.
    
    :param email: The email address of the user
    :return: True if the user exists, False otherwise
    """
    return User.objects.filter(email=email).exists()

def check_user_login(email, password):
    """
    Check if the user with the given email address and password exists and is valid.
    
    :param email: The email address of the user
    :param password: The password of the user
    :return: User object if the user exists and the password is correct, None otherwise
    """
    if not email or not password:
        return None
    
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return None
    
    if user.check_password(password):
        return user
    return None