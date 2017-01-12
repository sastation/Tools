#!/bin/bash

ns_svr=$1

fqdns=(
"vps.cnict.info"
"family.dynu.net"
"family.laowang.info"
"vps.laowang.info"
"addns.cnict.info"
)

fqdns=(
"wzxy.wangzhihai.net"
"news.sina.com.cn"
"fakedns.163.com"
)

ns_svrs=(
# CN
"上海电信:180.168.255.118"
"上海电信:116.228.111.18"
"上海电信:202.96.199.133"
"CNNIC:1.2.4.8"
"CNNIC:210.2.4.8"
"Ali:223.5.5.5"
"Ali:223.6.6.6"
"DNSPod:119.29.29.29"
"DNSPod:182.254.116.116"
"Baidu:180.76.76.76"
"114DNS:114.114.114.114"
"114DNS:114.114.115.115"
"中科大:202.38.93.153"
"中科大:202.141.162.123"
# US
"OneDNS:114.215.126.16"
"OneDNS:112.124.47.27"
"OpenDNS:208.67.222.222"
"OpenDNS:208.67.220.220"
"UltraDNS:156.154.70.1"
"UltraDNS:156.154.71.1"
"Norton:119.85.126.10"
"Norton:199.85.127.10"
"Google:8.8.4.4"
"Google:8.8.8.8"
)

function verify {
    for fqdn in ${fqdns[@]}
    do
        ds=`date +%s`
        host -t a $fqdn $ns_svr > /dev/null 2>&1
        if [ $? -eq 0 ]
        then
            status='true'
        else
            status="false"
        fi
        de=`date +%s`
        tm=`expr $de - $ds`
        echo $ns_dsc, $ns_svr, $fqdn, $status, $tm
    done
}

function scan {
    for ns in ${ns_svrs[@]}
    do
        IFS=':'; arrNS=($ns); unset IFS; # 拆分字符串
        ns_dsc=${arrNS[0]}
        ns_svr=${arrNS[1]}
        #echo $ns_dsc, $ns_svr
        verify
    done
}

# Main
if [ x$ns_svr == x ]
then
    scan
else
    ns_dsc='manual'
    #ns_svr='192.168.110.2'
    verify
fi
