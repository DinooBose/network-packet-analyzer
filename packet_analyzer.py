from scapy.all import *
import argparse

# Define a function to process each packet
def packet_callback(packet):
    # Check if the packet has a source and destination IP address
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        # Check if the packet has a source and destination port
        if packet.haslayer(TCP):
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            protocol = "TCP"
        elif packet.haslayer(UDP):
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
            protocol = "UDP"
        elif packet.haslayer(ICMP):
            protocol = "ICMP"
            src_port = ""
            dst_port = ""
        else:
            protocol = "Other"
            src_port = ""
            dst_port = ""
        # Print the packet information
        print(f"Source IP: {src_ip}, Destination IP: {dst_ip}, Source Port: {src_port}, Destination Port: {dst_port}, Protocol: {protocol}")

# Define a function to capture packets
def capture_packets(interface, count):
    print(f"Capturing {count} packets on interface {interface}...")
    packets = sniff(iface=interface, prn=packet_callback, count=count)
    print("Packet capture complete.")
    # Save the captured packets to a file
    wrpcap("captured_packets.pcap", packets)
    print("Captured packets saved to captured_packets.pcap")

# Define the main function
def main():
    # Parse the command-line arguments
    parser = argparse.ArgumentParser(description="Network Packet Analyzer")
    parser.add_argument("-i", "--interface", help="Network interface to capture packets from", required=True)
    parser.add_argument("-c", "--count", type=int, help="Number of packets to capture", required=True)
    args = parser.parse_args()
    # Capture packets
    capture_packets(args.interface, args.count)

# Run the main function
if __name__ == "__main__":
    main()
