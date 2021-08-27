import time

start_time = time.time()


def log(location: str, **msg: str) -> None:
    print(time.time() - start_time, location, msg)

