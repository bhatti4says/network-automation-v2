from netmiko import ConnectHandler
import os

# Enable/disable real device execution
TEST_MODE = True

# Device info
device = {
    "device_type": "cisco_ios",
    "host": "192.168.1.1",
    "username": os.getenv("DEVICE_USER"),
    "password": os.getenv("DEVICE_PASS"),
}

# Config you want to push
config_commands = [
    "interface loopback10",
    "ip address 10.10.10.10 255.255.255.255",
    "description pushed via automation"
]

try:
    print("[+] Starting automation script...")

    if TEST_MODE:
        print("[+] TEST MODE ENABLED")
        print("[+] Simulating config push...")
        print(config_commands)
    else:
        connection = ConnectHandler(**device)

        output = connection.send_config_set(config_commands)
        print(output)

        connection.save_config()
        print("[+] Config pushed successfully")

        connection.disconnect()

except Exception as e:
    print(f"[!] Error: {e}")

