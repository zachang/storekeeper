from werkzeug.security import safe_str_cmp
from user import User

user = [
    User(1, 'dunsin', 'password')
]  

username_mapping = {u.username: u for u in user}
userid_mapping = {u.id: u for u in user}

def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user


def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
