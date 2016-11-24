#!/bin/bash

# shrink git master branch

shrink() {
    git checkout --orphan temp $oid
    git commit -m "截取的历史记录起点"
    git rebase --onto temp $oid  master
    git branch -D temp
}

oid=$1

if [ x$oid == x ]; then
    echo "Need repo id."
    exit -1
fi

shrink

exit 0
