import re

def handle(value, err_msg: str, *args, **kwargs):
    err_msg = (err_msg or '#label# must be url format (http:// or https://).')
    pattern = r'^(https?|http):\/\/[^\s/$.?#].[^\s]*$'
    if re.match(pattern, value):
        return True, None
    return False, err_msg
