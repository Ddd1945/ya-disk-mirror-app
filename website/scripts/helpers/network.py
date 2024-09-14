import socket


def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    s.settimeout(0)

    s.connect_ex(("10.254.254.254", 1))

    ip = s.getsockname()[0]

    ip = "127.0.0.1" if ip == "0.0.0.0" else ip

    s.close()

    return ip
