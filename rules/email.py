import re

def handle(value, err_msg: str, *args, **kwargs):
    err_msg = (err_msg or '#label# must be email format.')
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, value):
        return True, None
    return False, err_msg
