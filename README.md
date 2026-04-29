# Network Packet Analyzer
A Python script to capture and analyze network packets using Scapy.

## Table of Contents
* [Introduction](#introduction)
* [Features](#features)
* [Requirements](#requirements)
* [Installation](#installation)
* [Usage](#usage)
* [Example Use Cases](#example-use-cases)
* [Contributing](#contributing)
* [License](#license)

## Introduction
This script is designed to capture and analyze network packets from a specified interface. It uses Scapy to capture packets and displays their source and destination IP addresses, ports, and protocols.

## Features
* Capture packets from a specified network interface
* Display packet source and destination IP addresses, ports, and protocols
* Save captured packets to a file
* Support for TCP, UDP, and ICMP protocols

## Requirements
* Python 3.x
* Scapy library (install using `pip install scapy`)
* Root privileges to run the script

## Installation
1. Clone the repository using
  `git clone https://github.com/DinooBose/network-packet-analyzer.git`
2. Install Scapy using
  `pip install scapy`
3. Run the script using
  `python3 packet_analyzer.py -i wlan0 -c 10`

## Usage
The script can be run from the command line using the following syntax:
```bash
python3 packet_analyzer.py -i <interface> -c <count>
```
Replace <interface> with the name of the network interface you want to capture packets from, and <count> with the number of packets you want to capture.
## Example Use Cases

    Capture 10 packets from the wlan0 interface: python packet_analyzer.py -i wlan0 -c 10
    Capture 100 packets from the eth0 interface: python packet_analyzer.py -i eth0 -c 100

<img width="896" height="624" alt="Image" src="https://github.com/user-attachments/assets/8a364ca6-a66a-4185-a7c8-178d3b3d826e" />
<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/9d92a9b5-f1c2-48c6-ba6b-21923e432992" />

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request.
## License

This project is licensed under the MIT License. See the LICENSE file for details.

