def handle(value, err_msg: str, *args, **kwargs):
    err_msg = (err_msg or '#label# must be float.')
    if not isinstance(value, float):
        return False, err_msg
    return True, None