#!/bin/bash

python collect.py
OS=`cat target_os`

mkdir -p result
cd result

uname -a > uname

if [[ "$OS" == "Linux" ]]; then
	cat /etc/os-release > os-release
	gcc --version > gcc-version
	cat /proc/cpuinfo > cpuinfo
	cat /proc/meminfo > meminfo
else
	sw_vers > os_release
	gcc-13 --version > gcc-version
	system_profiler SPHardwareDataType > cpuinfo
	sysctl hw > meminfo
fi