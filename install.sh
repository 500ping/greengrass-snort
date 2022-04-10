#! /bin/bash
apt-get purge --auto-remove snort -y
rm /tmp/alert

export DEBIAN_FRONTEND=noninteractive
apt-get update
apt-get -yq install snort=2.9.7.0-5build1 python3-pip

pip3 install -r $1/SnortInstall/requirements.txt

rm -rf /etc/snort
cp -R $1/SnortInstall/snort/ /etc/snort/

snort -D -A fast -l /tmp -c /etc/snort/snort.conf