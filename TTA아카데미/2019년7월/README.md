.
교육명 : 실전 성능테스트
교육기간 : (2차) 2019년 7월 15일(월)~16일(화), 2일, 16시간
교육장소: 한국정보통신기술협회(TTA) 9층 CHAMP교육장

강사 : 조정일 bearscho@gmail.com
실습 사이트 주소 : http://49.247.130.173/catalog
[로그인 계정 - 10개]
test01@mail.com,test01
test02@mail.com,test02
test03@mail.com,test03
test04@mail.com,test04
test05@mail.com,test05
test06@mail.com,test06
test07@mail.com,test07
test08@mail.com,test08
test09@mail.com,test09
test10@mail.com,test10



[시스템 성능수집]
서버IP : 49.247.130.173
계정 : loadman / loadman
명령어 : sar -u 1 1 | awk '/^Average:/{print 100-$8}'
접속 확인 툴 : putty
