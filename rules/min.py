def handle(value, err_msg: str, *args, **kwargs):
    err_msg = (err_msg or '#label# must be greater than or equal to #min#.').replace('#min#', str(args[0]))
    if type(value) == str:
        value = len(value)
    try:
        value   = float(value)
        length  = float(args[0])
        if value < length:
            return False, err_msg
    except ValueError:
        return False, err_msg
    return True, ''