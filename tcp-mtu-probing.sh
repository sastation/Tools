#!/bin/bash

echo 1 > /proc/sys/net/ipv4/tcp_mtu_probing

# tcp_mtu_probing (integer; default: 0; since Linux 2.6.17):
# This parameter controls TCP Packetization-Layer Path MTU Discovery. The following values may be assigned to the file:
#    0 Disabled
#    1 Disabled by default, enabled when an ICMP black hole detected
#    2 Always enabled, use initial MSS of tcp_base_mss.

