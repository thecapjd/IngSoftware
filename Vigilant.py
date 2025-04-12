import re
from collections import defaultdict

LOG_FILE = "network.log"
THRESHOLD_BYTES = 5000

def parse_log_line(line):

    match = re.search(r"IP:\s*([\d\.]+).*Bytes:\s*(\d+)", line)
    if match:
        ip = match.group(1)
        bytes_transferred = int(match.group(2))
        return ip, bytes_transferred
    return None, 0




if __name__ == "__main__":
    analyze_log_file()
