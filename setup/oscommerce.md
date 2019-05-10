서버 접속 주소 : 49.247.130.173  
OS : CentOS  

- Apache 설치  
yum -y install httpd    
yum -y install httpd                      !- 아파치 설치  
systemctl enable httpd.service            !- 부팅시 자동시작  
systemctl start httpd                     !- 아파치 서버 시작 

- PHP설치  
sudo yum install epel-release  
sudo rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-7.rpm
sudo yum --enablerepo=remi-php73 install php  
--- Module 설치
yum --enablerepo=remi-php73 install php-xml php-soap php-xmlrpc php-mbstring php-json php-gd php-mcrypt  

- Mysql 설치  
sudo rpm -ivh https://dev.mysql.com/get/mysql57-community-release-el7-11.noarch.rpm
sudo yum install mysql-community-server  
--- 기본 chracter-set 이 latin1 이므로 /etc/my.cnf 를 수정해서 utf-8 로 설정한다  
    character-set-server = utf8
    max_allowed_packet = 64M

sudo systemctl start mysqld  
--- 초기패스워드
[loadman@bearscho-57431 etc]$ grep 'password' /var/log/mysqld.log
2019-05-10T12:42:35.987573Z 1 [Note] A temporary password is generated for root@localhost: 47se?NeUwkK#

시스템 부팅시 자동 구동되도록 설정
systemctl enable mysqld
systemctl restart mysqld

mysql -uroot -p

UPDATE user set authentication_string=password('oscommerce') where user='root';
FLUSH PRIVILEGES;

