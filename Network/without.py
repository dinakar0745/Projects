import socket

def get_open_ports(ip_address):
    open_ports = []
    for port in range(50, 500):  # ports range
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip_address, port))
        print("Testing Port:", port)
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

def get_protocol_banner(ip_address, port):
    try:
        with socket.create_connection((ip_address, port), timeout=2) as sock:
            banner = sock.recv(1024).decode('utf-8').strip()
            return banner
    except (socket.error, socket.timeout):
        return None

if __name__ == "__main__":
    target_ip = '14.192.0.9'

    open_ports = get_open_ports(target_ip)
    print(f"Open Ports: {open_ports}")

    print("\nPort Protocol Banners:")
    for port in open_ports:
        banner = get_protocol_banner(target_ip, port)
        print(f"  Port {port}: {banner if banner else 'No banner available'}")
