교육명 : 실전 성능테스트  
교육기간 : (1차) 2020년 5월 18일(월)~19일(화), 2일, 16시간  
교육장소: 한국정보통신기술협회(TTA) 9층 CHAMP교육장  



서울공공데이터 API키 : 774a4864586a756e353367626d5a6e


서울시 비만도 통계 API  
날씨누리 RSS  
금융결제원 테스트베드 오픈API 계좌실명조회  
서울특별시 전월세가 정보 API   


  
강사 : 조정일 bearscho@gmail.com   010-7119-0434    
실습 사이트 주소 : http://49.247.207.252/catalog  
[로그인 계정 - 10개]  
test01@email.com,test01  
test02@email.com,test02  
test03@email.com,test03  
test04@email.com,test04  
test05@email.com,test05  
test06@email.com,test06  
test07@email.com,test07  
test08@email.com,test08  
test09@email.com,test09  
test10@email.com,test10  



[시스템 성능수집]  
서버IP : 49.247.207.252     16 rCore /32 G
계정 : loadman / loadman  
명령어 : sar -u 1 1 | awk '/^Average:/{print 100-$8}'  
접속 확인 툴 : putty  


서버IP : 49.247.130.173       8 vCore  /8 G
계정 : loadman / loadman  
명령어 : sar -u 1 1 | awk '/^Average:/{print 100-$8}'  
접속 확인 툴 : putty  



Jenkins 접속 : http://49.247.207.252:8080/    loadman/loadman

IP 는 GCP에서 수시로 변동
http://34.75.208.110:3000/login
http://34.75.208.110:8086
