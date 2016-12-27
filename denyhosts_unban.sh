#!/bin/bash

if [ -z "$1" ]; then
    echo -e "Error:\n\tProvide IP as the first param"
    echo -e "Usage:\n\t$0 <IP>"
    exit 1
fi

/etc/init.d/denyhosts stop
echo '
/usr/share/denyhosts/data/hosts
/usr/share/denyhosts/data/hosts-restricted
/usr/share/denyhosts/data/hosts-root
/usr/share/denyhosts/data/hosts-valid
/usr/share/denyhosts/data/users-hosts
/etc/hosts.deny
' | grep -v "^$" | xargs sed -i "/$1/d"
/etc/init.d/denyhosts start
