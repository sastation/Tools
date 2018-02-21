#!/bin/bash

setcap cap_net_bind_service=+ep ~/wall/caddy
setcap cap_net_bind_service=+ep ~/wall/gost
setcap cap_net_bind_service=+ep ~/wall/brook
#setcap cap_net_bind_service=+ep ~/ss/bin/

