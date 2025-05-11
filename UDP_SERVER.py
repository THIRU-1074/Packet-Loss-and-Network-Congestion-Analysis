import socket

# Replace with your PC's IP
UDP_IP = "192.168.254.168"  
UDP_PORT = 5005  # Must match the PC's receiving port

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for i in range(1000):
    message = f"Packet {i+1}".encode()
    sock.sendto(message, (UDP_IP, UDP_PORT))
    print(f"Sent: Packet {i+1}")

print("Transmission complete!")
