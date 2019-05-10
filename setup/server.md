### IPV6 해제  
 ifconfig -a | grep inet6
   
1. Append below lines in /etc/sysctl.conf:  
  
net.ipv6.conf.all.disable_ipv6 = 1  
net.ipv6.conf.default.disable_ipv6 = 1  


2. To make the settings affective, execute :  

sysctl -p  
  
### CetOS 방화벽 실행 확인  
service iptables status  
또는  
systemctl status iptables  
 
### 방화벽 정책 확인  
iptables -L
 
### 방화벽 일시 해제  

systemctl stop iptables  
systemctl stop ip6tables 
systemctl stop firewalld  


### 영구 해제(리부팅 이후에도 작동하지 않도록 설정)

systemctl disable iptables  
systemctl disable ip6tables 
systemctl disable firewalld  

## 방화벽 정책은 iwinv 콘솔에서 적용  
