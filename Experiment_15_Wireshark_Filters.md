# Experiment 15: Writing Wireshark Filter Expressions for Packet Capture

## AIM
To learn how to write and apply Wireshark capture filters and display filters so that only relevant packets are captured or shown during network analysis.

## SOFTWARE REQUIRED
- Computer with an active Ethernet or Wi-Fi interface.
- Wireshark (version 3.x or later).
- WinPcap/Npcap on Windows.
- Administrator/root privileges for packet capture.

## THEORY
Wireshark captures live network traffic and displays packet details. Filters help isolate useful packets.

| Feature | Capture filter | Display filter |
|---|---|---|
| When applied | Before capture starts | After packets are captured |
| Syntax | BPF/libpcap | Wireshark display-filter syntax |
| Effect | Non-matching packets are not captured | Non-matching packets are hidden, not deleted |
| Example | `tcp port 80` | `tcp.port == 80` |
| Where entered | Capture → Options | Display-filter bar |

Display-filter operators:
- `==` or `eq`: equal
- `!=` or `ne`: not equal
- `>` or `gt`: greater than
- `<` or `lt`: less than
- `&&` or `and`: logical AND
- `||` or `or`: logical OR
- `!` or `not`: logical NOT

## PROCEDURE
1. Open Wireshark and view the available network interfaces.
2. Select Capture → Options.
3. Enter a capture filter, for example `host 192.168.1.10`. A green indication means the syntax is valid.
4. Select the required interface and click Start.
5. Generate network traffic by opening a webpage or running a ping.
6. Enter a display filter such as `http.request` in the filter bar and press Enter.
7. Select a packet to view its decoded details and raw bytes.
8. Clear the display filter using the X button to view all captured packets.
9. Stop the capture. If required, save it using File → Save As in `.pcapng` format.

## SAMPLE FILTER EXPRESSIONS

### Capture filters
```text
host 192.168.1.10
net 192.168.1.0/24
src host 192.168.1.10
dst port 53
tcp port 443
udp
not arp and not broadcast
tcp port 80 and host 192.168.1.10
```

### Display filters
```text
ip.addr == 192.168.1.10
ip.src == 192.168.1.10
tcp.port == 80
http
dns
http.request.method == "GET"
tcp.flags.syn == 1 && tcp.flags.ack == 0
tcp.analysis.retransmission
ip.addr == 192.168.1.10 && tcp.port == 443
```

## SAMPLE OBSERVATION
| Filter applied | Purpose | Expected observation |
|---|---|---|
| `dns` | Isolate DNS traffic | DNS query and response packets |
| `tcp.flags.syn==1 && tcp.flags.ack==0` | Find connection starts | TCP SYN packets |
| `http.request` | View web requests | HTTP request packets, when present |
| `ip.addr==8.8.8.8` | Track one IP address | Packets to or from that address |

Record the actual observations from your own capture.

## RESULT
Thus, capture filters and display filters were applied in Wireshark, and their syntax, timing and effects were studied.
