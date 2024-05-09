def handle(value, err_msg: str, *args, **kwargs):
    err_msg = (err_msg or '#label# must be integer.')
    if not isinstance(value, int):
        return False, err_msg
    return True, None