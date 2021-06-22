def str_to_int_or_none(val):
    if not val:
        return None
    try:
        ret = int(val)
    except ValueError:
        ret = None
    return ret
