def handle(value, err_msg: str, *args, **kwargs):
    err_msg = (err_msg or '#label# must be string.')
    if not isinstance(value, str):
        return False, err_msg
    return True, ''