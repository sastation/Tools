#!/bin/bash

echo "IOPS Write..."
sync; dd if=/dev/zero of=./test.img bs=8k count=100K oflag=direct; sync
echo "-------------"

echo "IOPS Read..."
sync; dd if=./test.img of=/dev/null bs=8k count=100K iflag=direct; sync
echo "-------------"

echo "Seq. Write..."
sync; dd if=/dev/zero of=./test.img bs=1M count=800 oflag=direct ; sync
echo "-------------"

echo "Seq. Read..."
sync; dd if=./test.img of=/dev/null bs=1M count=800 iflag=direct ; sync
echo "-------------"

echo "Seq./fdatasync  Write..."
sync; dd if=/dev/zero of=./test.img bs=1M count=800 conv=fdatasync; sync
echo "-------------"

echo "Seq./fdatasync Read..."
sync; dd if=./test.img of=/dev/null bs=1M count=800 ; sync
echo "-------------"

rm test.img
