#! /bin/bash
apt-get purge --auto-remove snort -y
rm /tmp/alert

export DEBIAN_FRONTEND=noninteractive
apt-get -yq install snort

# cp -R $1/* /opt
# rm -rf /etc/snort
# cp -R $1/SnortInstall/snort/ /etc/snort/
# cp -TR /opt/SnortInstall/snort/rules /etc/snort/rules
# rsync -a --delete $1/SnortInstall/snort/etc/ /etc/snort
# rsync -a --delete $1/SnortInstall/snort/rules/ /etc/snort/rules

# touch /etc/snort/rules/white_list.rules
# touch /etc/snort/rules/black_list.rules

snort -D -A fast -l /tmp -c /etc/snort/snort.conf