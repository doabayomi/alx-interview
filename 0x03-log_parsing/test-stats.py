#!/usr/bin/python3
"""Printing stats from log"""
import re
import sys
import signal

stats = {
    'File size': 0,
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}


def print_stats():
    """Prints the stat of the read logs
    """
    print(f"File size: {stats['File size']}")
    codes = list(stats.keys())[1:]
    for code in sorted(codes):
        print(f"{code}: {stats[int(code)]}")


def handle_signal(signum, frame):
    """Handler for keyboard interrupt to print stats on logs

    Args:
        signum: Default signum
        frame: Default frame
    """
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, handle_signal)
line_count = 0

"""Log line pattern"""
pattern = (
    r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} "
    r"\- "
    r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\] "
    r"\"GET /projects/260 HTTP/1\.1\" "
    r"(\d{3}) "
    r"(\d+)$"
)

try:
    for line in sys.stdin:
        line_count += 1

        match = re.match(pattern, line)
        if match is None:
            continue

        status_code = int(match.group(1))
        file_size = int(match.group(2))
        # print(f"{file_size}, {status_code}")

        stats["File size"] += file_size
        if status_code in stats:
            stats[status_code] += 1

        if line_count % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    print_stats()