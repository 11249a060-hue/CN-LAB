# Experiment 17: Use Wireshark to Inspect Packets on Your Network

## AIM
To capture live traffic from a network interface and inspect packets by examining protocol layers, following a TCP conversation and viewing traffic statistics.

## SOFTWARE REQUIRED
- Computer connected to a live network (Ethernet or Wi-Fi).
- Wireshark installed with Npcap/libpcap.
- Required capture permissions.
- Web browser or ping utility to generate traffic.

## THEORY
Network activities such as opening a webpage and resolving a domain name are carried as packets. Wireshark captures and decodes these packets.

| Network layer | Protocol example | Information shown |
|---|---|---|
| Data-link | Ethernet II | Source and destination MAC addresses |
| Network | IPv4 / IPv6 | Source and destination IP addresses, TTL |
| Transport | TCP / UDP | Port numbers, sequence and acknowledgement numbers, flags |
| Application | HTTP, DNS, TLS | Requests, responses and queries |

Wireshark has three main panes:
1. Packet list.
2. Packet details tree.
3. Packet bytes in hexadecimal and ASCII.

## PROCEDURE
1. Open Wireshark.
2. Double-click the active network interface to start capturing.
3. Generate traffic by opening a website or running these commands:
   ```text
   ping www.google.com
   nslookup www.google.com
   ```
4. Allow packets to appear, then stop the capture after a few seconds.
5. Apply a display filter such as `dns` or `icmp`.
6. Select a packet and expand the details tree to inspect Ethernet, IP, TCP/UDP and application layers.
7. Right-click a TCP packet and choose Follow → TCP Stream to view the conversation.
8. Open Statistics → Protocol Hierarchy to view protocol distribution.
9. Open Statistics → Conversations and Statistics → Endpoints to inspect communicating hosts and packet/byte counts.
10. Optionally open Statistics → I/O Graph to view traffic volume over time.
11. Save the capture using File → Save As if required.

## USEFUL DISPLAY FILTERS
```text
dns
icmp
tcp
udp
http
```

## SAMPLE OBSERVATION TABLE
The following is an example format. Enter the actual values from your own capture.

| Packet No. | Source IP | Destination IP | Protocol | Information |
|---|---|---|---|---|
| 1 | | | DNS | DNS query |
| 2 | | | DNS | DNS response |
| 3 | | | TCP | Connection request (SYN) |
| 4 | | | TCP | Connection accepted (SYN, ACK) |
| 5 | | | ICMP | Ping request/reply |

## RESULT
Thus, live packets were captured from the network interface and inspected in Wireshark. Protocol layers, TCP conversations and traffic statistics were studied.
