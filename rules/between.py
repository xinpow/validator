def handle(value, err_msg: str, *args, **kwargs):
    """范围对比
        可以对比字符串、整数、浮点数.
        对比字符串时比对的是字符串长度，对比整数、浮点数时比对的是数值大小.

    Args:
        value (str/int/float): 对比值
        err_msg (str, optional): 错误信息模板，默认 '#label# must be between #min# and #max#.'

    Returns:
        bool: 是否通过验证
        str or None: 错误信息
    """
    err_msg = (err_msg or '#label# must be between #min# and #max#.').replace('#min#', str(args[0])).replace('#max#', str(args[1]))
    
    if type(value) == str:
        value = len(value)
    try:
        value    = float(value)
        minValue = float(args[0])
        maxValue = float(args[1])
        if not (minValue <= value <= maxValue):
            return False, err_msg
    except ValueError:
        return False, err_msg
    return True, ''