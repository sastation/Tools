#!/bin/bash
# function one: list all kernels
# function two: remove specific kernel packages

ver=$1

if [ x$ver == x ]; then
    echo "Current kernel list: "
    echo "================================"
    dpkg -l linux-* | awk '/^ii/{ print $2 }' | grep -e [0-9]
    #dpkg --list | grep linux-image | awk '{ print $2 }' | sort -V | sed -n '/'`uname -r`'/q;p'
    echo "================================"
    exit 0
fi

read -p "Do you really want to remove old knernal $ver?(y/n) " opt

if [ x$opt == xy ]; then
    echo "remove old kernel $ver"
    apt-get purge linux-headers-$ver
    apt-get purge linux-headers-$ver-generic
    apt-get purge linux-image-$ver-generic
    apt-get purge linux-image-extra-$ver-generic
    update-grub
fi

exit 0
