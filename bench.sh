#!/bin/bash

mkdir -p result
cd result

uname -a > uname
cat /etc/os-release > os-release
gcc --version > gcc-version
cat /proc/cpuinfo > cpuinfo
cat /proc/meminfo > meminfo