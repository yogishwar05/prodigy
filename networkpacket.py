from scapy.all import sniff, Ether, IP, TCP, UDP

def packet_handler(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto
        if protocol == 6 and TCP in packet:  # TCP
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            payload = packet[TCP].payload
            print(f"TCP packet: {src_ip}:{src_port} -> {dst_ip}:{dst_port}\nPayload: {payload}")
        elif protocol == 17 and UDP in packet:  # UDP
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
            payload = packet[UDP].payload
            print(f"UDP packet: {src_ip}:{src_port} -> {dst_ip}:{dst_port}\nPayload: {payload}")

def main():
    print("Packet sniffer started. Press Ctrl+C to stop.")
    try:
        sniff(iface="eth0", prn=packet_handler, store=0)
    except KeyboardInterrupt:
        print("Packet sniffer stopped.")

if __name__ == "__main__":
    main()