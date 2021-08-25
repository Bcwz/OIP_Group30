from time import time

start_time = time()


def log(location: str, **msg: str) -> None:
    print(time() - start_time, location, msg)
