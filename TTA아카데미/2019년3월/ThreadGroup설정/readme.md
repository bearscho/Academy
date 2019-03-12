ThreadGroup 설정 안내  

실습 자료 중 아래와 같은 ThreadGroup를 설정하는 부분이 있는데, 설명이 부족한 것 같아 추가 설정 관련 공유 드립니다.  
. 1분마다 5명 중가  
. 최대 10명 유입  
. 측정 시간 : 10분  

1번째 방법으로는 JMeter 기본 ThreadGroup를 사용하는 방법이 있습니다.  

- 최대 10명 유입 : Numer of Threads(users) 에 10 입력  
- 1분마다 5명 증가

<img src="https://github.com/bearscho/academy/blob/master/TTA%EC%95%84%EC%B9%B4%EB%8D%B0%EB%AF%B8/2019%EB%85%843%EC%9B%94/ThreadGroup%EC%84%A4%EC%A0%95/1.threadgroup.PNG?raw=true">

2.concurrencythreadgroup.PNG  

<img src=https://github.com/bearscho/academy/blob/master/TTA%EC%95%84%EC%B9%B4%EB%8D%B0%EB%AF%B8/2019%EB%85%843%EC%9B%94/ThreadGroup%EC%84%A4%EC%A0%95/2.concurrencythreadgroup.PNG?raw=true">
