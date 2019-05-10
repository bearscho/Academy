### IPV6 해제  
 ifconfig -a | grep inet6
   
1. Append below lines in /etc/sysctl.conf:  
  
net.ipv6.conf.all.disable_ipv6 = 1  
net.ipv6.conf.default.disable_ipv6 = 1  


2. To make the settings affective, execute :  

# sysctl -p  
