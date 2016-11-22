#!/bin/bash

dev=$1

if [ "x"$dev == "x" ]
then
    echo "Need dev name."
    exit 0
fi

ip link set arp off dev $dev
ip link set arp on dev $dev
