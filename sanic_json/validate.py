class MissingQueryException(Exception):
    pass


def valida_request_query(req, *args, **kwargs):
    q_args = []
    q_kwargs = {}
    for k in args:
        if k not in req.args:
            raise MissingQueryException("missing {}".format(k))
        else:
            # only need the first
            q_args.append(req.args[k][0])

    for k, default in kwargs.items():
        # only need the first
        value = req.args.get(k, default)
        if isinstance(default, bool):
            value = bool(parse_boolean_value(value))
        elif isinstance(default, int):
            value = int(value)
        elif isinstance(default, float):
            value = float(value)

        q_kwargs[k] = value

    return q_args, q_kwargs


def parse_boolean_value(v):
    if not v:
        return None

    types = [float, int]
    for t in types:
        try:
            return t(v)
        except Exception:
            pass

    if v.lower() in ["false", "null", "nil", "none"]:
        return False
    elif v.lower() == "true":
        return True
    return v
