import socket
import subprocess


def scan_wifi_network():
    # Get the local IP address of the machine
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)

    # Split the IP address to get the network prefix
    network_prefix = ".".join(local_ip.split(".")[:-1]) + "."

    # Scan the Wi-Fi network for active devices
    active_devices = []
    for i in range(1, 256):  # Scan IP addresses from 1 to 255
        ip = network_prefix + str(i)
        response = subprocess.call(
            ["ping", "-c", "1", "-W", "1", ip],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        if response == 0:
            active_devices.append(ip)

    # Retrieve device information for active devices
    device_info = []
    for ip in active_devices:
        try:
            output = subprocess.check_output(
                ["adb", "-s", ip, "shell", "getprop", "ro.product.model"]
            )
            model = output.decode().strip()
            device_info.append((ip, model))
        except subprocess.CalledProcessError:
            pass

    return device_info


# Scan the Wi-Fi network and retrieve device information
devices = scan_wifi_network()
for ip, model in devices:
    print(f"Device IP: {ip} - Model: {model}")
