#!/bin/bash
echo 请确保本机已有lnmp_soft.tar.gz包!
echo 请将上述tar包放到/root下!
sleep 3
#判断yum源
a=`yum repolist | awk '/repolist/{print $2}' | sed 's/,//'`
if [ $a -eq 0 ];then
echo "[rhel7]
name=rhel7
baseurl=ftp://192.168.$1.254/rhel7
enabled=1
gpgcheck=0" > /etc/yum.repos.d/rhel7.repo
yum clean all > /dev/null
yum repolist > /dev/null
fi
#解包,安装Nginx软件
yum -y install gcc pcre-devel openssl-devel
useradd -s /sbin/nologin nginx > /dev/null
cd
tar -xf lnmp_soft.tar.gz > /dev/null
cd lnmp_soft
tar -xf nginx-1.12.2.tar.gz > /dev/null
cd nginx-1.12.2
#killall nginx > /dev/null
#rm -rf /sbin/nginx > /dev/null
#rm -rf /usr/local/nginx > /dev/null
./configure --user=nginx --group=nginx  --with-http_ssl_module --with-stream --with-http_stub_status_module > /dev/null
make && make install > /dev/null
cp /usr/local/nginx/sbin/nginx /sbin/ > /dev/null
nginx > /dev/null
yum -y install mariadb-server mariadb-devel php php-devel php-mysql
cd /root/lnmp_soft/
yum -y install php-fpm-5.4.16-42.el7.x86_64.rpm
nginx
systemctl restart mariadb
systemctl restart php-fpm
