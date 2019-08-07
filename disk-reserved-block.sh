#!/bin/bash

# By default, ext2/3/4 filesystems reserve 5% of the space to be useable only by root. This is to avoid a normal user completely filling the disk which would then cause system components to fail whenever they next needed to write to the disk.
# You can see the number of reserved blocks (and lots of other information about the filesystem) by doing:

tune2fs -l /dev/sda8

# For a /home partition, it is probably safe to set the reserved fraction to zero:
tune2fs -m 0 /dev/sda8

# Which should make an additional ~5GB available.

