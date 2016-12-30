#!/bin

# clean old kernal
dpkg -l 'linux-*' | sed '/^ii/!d;/'"$(uname -r | sed "s/\(.*\)-\([^0-9]\+\)/\1/")"'/d;s/^[^ ]* [^ ]* \([^ ]*\).*/\1/;/[0-9]/!d' | xargs sudo apt-get -y purge

# list packages size
dpkg-query -W --showformat='${Installed-Size;10}\t${Package}\n' | sort -k1,1n
dpkg-query --show --showformat='${Package;-50}\t${Installed-Size}\n' | sort -k 2 -n

# query faild login via sshd
sudo cat /var/log/auth.log | grep -ia sshd | grep -ia Failed
