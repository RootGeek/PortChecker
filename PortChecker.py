
# Deine gewünschte ASCII Art
ascii_art = """
 ____    ___    ___   _____   ____  _____  _____  _  __
|  _ \  / _ \  / _ \ |_   _| / ___|| ____|| ____|| |/ /
| |_) || | | || | | |  | |  | |  _ |  _|  |  _|  | ' / 
|  _ < | |_| || |_| |  | |  | |_| || |___ | |___ | . \ 
|_| \_\ \___/  \___/   |_|   \____||_____||_____||_|\_\
"""

import socket
import time

def is_port_open(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # Setze eine Zeitüberschreitung für den Verbindungsaufbau
            result = s.connect_ex((ip, port))
            return result == 0
    except socket.error:
        return False

def main():
    print(ascii_art)
    print("\nWillkommen zum Port-Test von RootGeek!")
    ip = input("Gib die IP-Adresse ein: ")
    port = int(input("Gib den Port ein: "))

    while True:
        if is_port_open(ip, port):
            print(f"Der Port {port} auf {ip} ist geöffnet.")
        else:
            print(f"Der Port {port} auf {ip} ist geschlossen.")

        time.sleep(1)  # Warte 1 Sekunde
        user_input = input("Drücke zum Beenden die Taste strg und c gleichzeitig: ")
        if user_input.lower() == 'q':
            break

if __name__ == "__main__":
    main()
