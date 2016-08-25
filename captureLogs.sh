#! /bin/bash

logLocation=`pwd`/`uname -r`-`date +%s`

mkdir $logLocation

echo -e "Logs will be copied at $logLocation"

echo -e "Copying syslogs"
cp /var/log/messages $logLocation/

echo -e "Copying /proc/devices"
cp /proc/devices $logLocation/

echo -e "Copying OS version"
cp /etc/*-release $logLocation/

echo -e "Putting uname"
echo -e "Kernel version is :" > $logLocation/uname
uname -r > $logLocation/uname

echo -e "All kernel versions are listed : " > $logLocation/installedKernels
rpm -qa | grep -i kernel > $logLocation/installedKernels

echo -e "Copying cmdline file"
cp /proc/cmdline $logLocation/

echo -e "Copying history "
history > $logLocation/cmdHistory

echo -e "Checking UEFI"
efibootmgr  > $logLocation/uefi

echo -e "dmidecode"
dmidecode > $logLocation/dmidecode

echo -e "copying dmesg"
dmesg > $logLocation/dmesg

echo -e "Coying config file"
cp /boot/config-`uname -r` $logLocation/

echo -e "Recording RPM info"
rpm -qai > $logLocation/rpmqi

`df -h` > $logLocation/df-h

cp /proc/partitions $logLocation/
