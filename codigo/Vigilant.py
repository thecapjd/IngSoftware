import re
from collections import defaultdict

LOG_FILE = "network.log"
THRESHOLD_BYTES = 5000

def parse_log_line(line):
    """
    Procesa una línea del log y extrae la IP de origen y la cantidad de bytes transferidos.

    Se espera que cada línea del log tenga el siguiente formato:
    "2025-04-11 15:37:12, IP: 192.168.1.10, Bytes: 2048"
    """
    match = re.search(r"IP:\s*([\d\.]+).*Bytes:\s*(\d+)", line)
    if match:
        ip = match.group(1)
        bytes_transferred = int(match.group(2))
        return ip, bytes_transferred
    return None, 0


def analyze_log_file():
    """
    Lee el archivo de log, acumula los bytes transferidos por cada IP
    y verifica si alguna supera el umbral definido.
    """
    ip_usage = defaultdict(int)

    try:
        with open(LOG_FILE, "r") as f:
            for line in f:
                ip, bytes_transferred = parse_log_line(line)
                if ip:
                    ip_usage[ip] += bytes_transferred
    except FileNotFoundError:
        print("El archivo de log no se encontró.")
        return

    for ip, total_bytes in ip_usage.items():
        if total_bytes > THRESHOLD_BYTES:
            print(
                f"[ALERTA] La IP {ip} ha transferido {total_bytes} bytes, superando el umbral de {THRESHOLD_BYTES} bytes.")
        else:
            print(f"La IP {ip} ha transferido {total_bytes} bytes.")


if __name__ == "__main__":
    analyze_log_file()
