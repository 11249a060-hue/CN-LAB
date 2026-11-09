# Experiment 16: Analysis of RTP Packet Delay and Loss using Wireshark

## AIM
To capture Real-time Transport Protocol (RTP) traffic from a VoIP/streaming session and analyse packet delay (jitter), packet loss and out-of-order delivery using Wireshark.

## SOFTWARE REQUIRED
- Computer with an active Ethernet or Wi-Fi interface.
- Wireshark (version 3.x or later).
- WinPcap/Npcap on Windows.
- A suitable RTP/VoIP capture or an available VoIP session.

## THEORY
RTP carries audio and video for real-time communication and normally uses UDP. Each RTP packet contains a sequence number and timestamp.

- **Packet loss:** A gap in RTP sequence numbers indicates missing packets.
- **Jitter:** Variation in packet arrival time.
- **Out-of-order packets:** Packets that arrive in a different order from their sequence.

RTCP can report statistics such as packet loss and jitter.

Important measurements:
- **Jitter:** Variation in packet arrival time. The manual notes that mean jitter below 30 ms is good for voice.
- **Lost packets:** Missing RTP packets. The manual notes that below 1% is good and above 5% is poor.
- **Delta:** Time since the previous packet in the stream.
- **Skew:** Difference between expected and actual arrival timing.

## PROCEDURE
1. Start Wireshark and begin capturing on the interface carrying the call.
2. Place a VoIP call between two endpoints, or open an existing VoIP `.pcap` file using File → Open.
3. Allow the call to run for at least 20–30 seconds, then stop the capture.
4. If Wireshark does not recognise RTP automatically, right-click a UDP packet from the media stream, select Decode As, and choose RTP.
5. Open Telephony → RTP → RTP Streams.
6. Select the required stream and click Analyze.
7. Study the Sequence number, Delta, Jitter, Skew and Status columns.
8. Note the total packets, lost packets and percentage, maximum jitter and mean jitter.
9. If available, use Play Streams or Telephony → VoIP Calls for additional analysis.
10. Optionally apply the `rtcp` display filter to view RTCP control/report packets.

## USEFUL DISPLAY FILTERS
```text
rtp
rtcp
rtp.ssrc == 0x12345678
rtp.marker == 1
sip
```

## OBSERVATION TABLE
Enter the values shown by your own RTP Streams and Analyze windows.

| Parameter | Stream A → B | Stream B → A |
|---|---|---|
| Codec / Payload | | |
| Total packets | | |
| Lost packets (count / %) | | |
| Maximum jitter (ms) | | |
| Mean jitter (ms) | | |
| Maximum delta (ms) | | |
| Quality assessment | | |

## RESULT
Thus, an RTP stream was captured and analysed in Wireshark. Packet delay (jitter), packet loss and out-of-order delivery were examined using the RTP Streams tools.
