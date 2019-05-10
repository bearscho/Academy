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

