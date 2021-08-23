from time import time_ns


def log(location: str, **msg: str) -> None:
    print(time_ns, location, msg)
