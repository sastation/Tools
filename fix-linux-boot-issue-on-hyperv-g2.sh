#!/bin/bash

# fix booting issue of Linux after move disk in Hyper-V Generation 2

# before moving disk
sudo -s
cd /boot/efi/EFI
cp -r ubuntu/ boot
cd boot
cp shimx64.efi bootx64.efi
