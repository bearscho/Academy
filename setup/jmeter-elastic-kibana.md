
## Elastic  
yum install elasticsearch  

### Bind IP 설정  
/etc/elasticsearch/elasticsearch.yml
#network.host: 192.168.0.1    => (주석해제)  =>   network.host: 0.0.0.0


### Bind IP 설정  
systemctl start elasticsearch  

### 자동실행
systemctl enable elasticsearch  


## Kibana  
yum install kibana  

sudo systemctl enable kibana
sudo systemctl start kibana

### Bind IP 설정  
/etc/kibana/kibana.yml
#server.host: "192.168.0.1"    => (주석해제)  =>   server.host: "0.0.0.0"
server.host: "0.0.0.0"


