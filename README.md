# py clogger

## Project Overview

py clogger is a lightweight Python logging utility library. It provides a set of simple functions for printing formatted log messages directly to the console.

## Installation

The library can be installed directly from its GitHub repository using pip:

```shell
pip install git+https://github.com/cyfney/py_clogger.git
```

## Core Functions (API)

The library exposes five main logging functions, each corresponding to a standard severity level:

- log_v(*args): Logs a **Verbose**​ message.
- log_i(*args): Logs an **Info**​ message.
- log_d(*args): Logs a **Debug**​ message.
- log_w(*args): Logs a **Warning**​ message.
- log_e(*args): Logs an **Error**​ message.

## Usage Example

```python
from clogger import log_v, log_i, log_d, log_w, log_e

def main():
    log_v("test")
    log_i("test")
    log_d("test")
    log_w("test")
    log_e("test")


if __name__ == "__main__":
    main()
```

## Log Output Format

When you run the example code, the output to the console will have the following consistent format:

```txt
YYYY-MM-DD HH:MM:SS.mmm {LEVEL} {filename}:{line_number} {function_name}] {message}
```

**Example Output**:

```log
2026-04-01 10:28:45.926 V main.py:4 main] test
2026-04-01 10:28:45.926 I main.py:5 main] test
2026-04-01 10:28:45.927 D main.py:6 main] test
2026-04-01 10:28:45.927 W main.py:7 main] test
2026-04-01 10:28:45.927 E main.py:8 main] test
```

Each log entry includes:

- **Timestamp**: With millisecond precision.
- **Log Level**: A single character (V, I, D, W, E).
- **Source Context**: The originating filename, line number, and function name.
- **User Message**: The content passed to the log function.
