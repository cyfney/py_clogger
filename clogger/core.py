import inspect
import datetime
from pathlib import Path


def _log(level, *args):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    caller_frame = inspect.currentframe().f_back.f_back  # 2 levels up
    caller_info = caller_frame.f_code
    filename = Path(caller_info.co_filename).name
    function_name = caller_info.co_name
    line_no = caller_frame.f_lineno
    print(f"{timestamp} {level} {filename}:{line_no} {function_name}]", *args)


def log_v(*args):
    _log("V", *args)


def log_i(*args):
    _log("I", *args)


def log_d(*args):
    _log("D", *args)


def log_w(*args):
    _log("W", *args)


def log_e(*args):
    _log("E", *args)
